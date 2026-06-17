#!/usr/bin/env python3
"""
PKS Linker Identification & Vulnerability Pipeline
=====================================================
README.md의 Methods 2.2-2.5를 그대로 구현한 자동화 스크립트.

어떤 Type I PKS든 FASTA(단백질 또는 CDS), AlphaFold PDB, AlphaFold PAE JSON
세 파일만 넣으면 도메인 경계 → 링커 식별 → 취약도 평가 → 재설계 판정까지 자동 실행한다.

사용법:
    python pks_linker_pipeline.py --fasta seq.fasta --pdb model.pdb --json pae.json --output results/

필요 파일(같은 폴더에 위치):
    hmm_data/nrpspksdomains.hmm
    hmm_data/ksdomains.hmm
    hmm_data/dockingdomains.hmm
    hmm_data/abmotifs.hmm
    (출처: antiSMASH, Blin et al. 2023, Nucleic Acids Research)

필요 패키지:
    pip install biopython pyhmmer numpy --break-system-packages
    mkdssp (apt install dssp, 또는 mkdssp 바이너리가 PATH에 있어야 함)
"""

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

try:
    from Bio.Seq import Seq
except ImportError:
    sys.exit("biopython이 필요합니다: pip install biopython --break-system-packages")

try:
    import pyhmmer
    from pyhmmer.easel import Alphabet, TextSequence
except ImportError:
    sys.exit("pyhmmer가 필요합니다: pip install pyhmmer --break-system-packages")


# ============================================================
# Methods 2.2 — 파라미터 (README.md 근거 그대로)
# ============================================================
HMM_IEVALUE_THRESHOLD = 1e-5
# 근거: 무작위 약한 매칭(i-evalue > 1)과 통계적으로 유의한 매칭(i-evalue < 1e-10)
# 사이의 간극을 가르는 보수적 경계값 (README Methods 2.2)

DOMAIN_MERGE_OVERLAP_ONLY = True
# 근거: 좌표가 "겹치는" 매칭만 같은 도메인 인스턴스로 병합한다.
# 단순 인접(gap>0)은 병합하지 않는다 — 별개 도메인을 하나로 합치는 오류를 방지.

# Methods 2.3 — 파라미터
HELIX_STRAND_REVIEW_THRESHOLD = 0.30
# 근거: helix 또는 strand 비율이 약 30% 이상이면 "정형 구조 혼재"로 보고
# 구조적 압축도 검증으로 넘긴다 (README Methods 2.3, 고정 coil% 임계값은 사용하지 않음)

CA_CA_BOND_LENGTH = 3.8  # Angstrom, 인접 CA 원자 간 평균 결합 거리
COMPACTION_DOMAIN_LIKE_CUTOFF = 0.20
# 근거: 대조군 compaction ratio가 도메인(KS, ratio 0.01)과 링커(확정 링커, ratio 0.60)
# 사이에서 뚜렷이 갈렸으므로(README Result I, 3.2), 두 값의 중간 지점보다도
# 도메인 쪽에 가깝게 0.20을 보수적 경계로 사용한다. 0.20 미만이면 도메인으로 재분류.

# Methods 2.4 — 파라미터
PAE_FLANK = 60
# 근거: 인접 도메인의 구조적 영향을 충분히 포함하면서 먼 도메인까지 포함시켜
# 신호를 희석시키지 않는 절충 범위 (README Methods 2.4)

VULN_NO_NEED_CUTOFF = 30
# 근거: 6개 gap 전체 취약도 점수 분포(9.5~62.9)에서 안정적인 링커(9~25)와
# 취약한 링커(35 이상) 사이에 위치하는 값 (README Methods 2.5)

MIN_LINKER_LENGTH = 5

# Methods 2.2 — 도메인 모델명 정규화용 (같은 위치 다중 매칭 시 대표명 선택은 i-evalue 최솟값 기준)
MERGE_DISTANCE_FOR_SAME_DOMAIN = 0  # overlap 기준만 사용 (겹치지 않으면 병합 안 함)

# Methods 2.5 — 촉매 잔기 모티프
CATALYTIC_MOTIFS = {
    "KS-Cys": [(r"[ILVMF]C[A-Z]{1,4}[AG]", 1), (r"HGTGT", 0)],
    "AT-Ser": [(r"GHS[A-Z]G", 2), (r"AFSGQGT", 3)],
    "ACP-Ser": [(r"LG[A-Z]DS", 4), (r"LG[A-Z]TS", 4), (r"LG[A-Z]ES", 4)],
}


# ============================================================
# 입력 로드
# ============================================================

def load_protein_sequence(fasta_path: str) -> str:
    with open(fasta_path) as f:
        lines = f.readlines()
    seq = "".join(l.strip() for l in lines if not l.startswith(">")).upper().replace(" ", "")
    dna_chars = set("ACGT")
    is_dna = len(seq) > 0 and all(c in dna_chars for c in seq[:200])
    if is_dna:
        protein = str(Seq(seq).translate(to_stop=True))
        print(f"[입력] DNA(CDS) 감지 → 번역 완료 ({len(protein)} aa)")
        return protein
    print(f"[입력] 단백질 서열 감지 ({len(seq)} aa)")
    return seq


def load_plddt(pdb_path: str) -> dict:
    residues = {}
    with open(pdb_path) as f:
        for line in f:
            if line.startswith("ATOM") and line[12:16].strip() == "CA":
                res_num = int(line[22:26].strip())
                residues[res_num] = float(line[60:66].strip())
    if not residues:
        sys.exit(f"[오류] {pdb_path}에서 CA 원자를 찾을 수 없습니다.")
    print(f"[입력] pLDDT 추출 완료 ({len(residues)} 잔기, 평균 {np.mean(list(residues.values())):.1f})")
    return residues


def load_ca_coords(pdb_path: str) -> dict:
    coords = {}
    with open(pdb_path) as f:
        for line in f:
            if line.startswith("ATOM") and line[12:16].strip() == "CA":
                res_num = int(line[22:26].strip())
                x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])
                coords[res_num] = np.array([x, y, z])
    return coords


def load_pae(json_path: str) -> np.ndarray:
    with open(json_path) as f:
        data = json.load(f)
    pae = np.array(data[0]["predicted_aligned_error"]) if isinstance(data, list) else np.array(data["predicted_aligned_error"])
    print(f"[입력] PAE 행렬 로드 완료 {pae.shape}")
    return pae


def run_dssp(pdb_path: str, work_dir: Path) -> dict:
    """mkdssp 실행 후 잔기별 단순화된 이차구조(H/E/C) 반환. Methods 2.3 (1)."""
    dssp_out = work_dir / "structure.dssp"
    try:
        subprocess.run(["mkdssp", str(pdb_path), str(dssp_out)], check=True,
                        capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit("[오류] mkdssp 바이너리를 찾을 수 없습니다. 'apt-get install dssp'로 설치하세요.")
    except subprocess.CalledProcessError as e:
        sys.exit(f"[오류] mkdssp 실행 실패: {e.stderr}")

    with open(dssp_out) as f:
        lines = f.readlines()
    start_idx = None
    for i, l in enumerate(lines):
        if l.startswith("  #  RESIDUE"):
            start_idx = i + 1
            break
    ss_raw = {}
    for line in lines[start_idx:]:
        if len(line) < 17:
            continue
        try:
            resnum = int(line[5:10].strip())
        except ValueError:
            continue
        ss_raw[resnum] = line[16]

    def simplify(ss):
        if ss in "HGI":
            return "H"
        elif ss in "EB":
            return "E"
        return "C"

    return {r: simplify(ss) for r, ss in ss_raw.items()}


# ============================================================
# Methods 2.2 — HMM 기반 도메인 경계 탐지
# ============================================================

def load_hmm_library(hmm_dir: Path) -> list:
    hmm_files = ["abmotifs.hmm", "dockingdomains.hmm", "nrpspksdomains.hmm", "ksdomains.hmm"]
    all_hmms = []
    for fname in hmm_files:
        path = hmm_dir / fname
        if not path.exists():
            sys.exit(f"[오류] HMM 파일을 찾을 수 없습니다: {path}")
        with pyhmmer.plan7.HMMFile(path) as f:
            all_hmms.extend(list(f))
    print(f"[Module 2.2] HMM 라이브러리 로드 완료 ({len(all_hmms)}개 모델, 출처: antiSMASH)")
    return all_hmms


def scan_domains(protein: str, hmms: list) -> list:
    """전체 HMM 라이브러리 스캔 후 i-evalue < threshold 통과 매칭만 반환."""
    alphabet = Alphabet.amino()
    seq = TextSequence(name=b"query", sequence=protein)
    digital_seq = seq.digitize(alphabet)
    results = list(pyhmmer.hmmer.hmmscan([digital_seq], hmms, cpus=2))

    hits = []
    for top_hits in results:
        for hit in top_hits:
            hmm_name = hit.name if isinstance(hit.name, str) else hit.name.decode()
            for domain in hit.domains:
                a = domain.alignment
                hits.append((a.target_from, a.target_to, hmm_name, domain.i_evalue))
    hits.sort()

    accepted = [h for h in hits if h[3] < HMM_IEVALUE_THRESHOLD]
    print(f"[Module 2.2] i-evalue < {HMM_IEVALUE_THRESHOLD} 통과: {len(accepted)}/{len(hits)} 매칭")
    return accepted


def merge_domains(hits: list) -> list:
    """좌표가 겹치는 매칭만 병합. 인접(겹치지 않음)은 별개 도메인으로 유지."""
    hits.sort()
    clusters = []
    for s, e, name, ie in hits:
        placed = False
        for c in clusters:
            cs, ce = c["start"], c["end"]
            if s <= ce and e >= cs:  # 좌표가 실제로 겹칠 때만
                c["start"] = min(c["start"], s)
                c["end"] = max(c["end"], e)
                c["members"].append((name, ie))
                placed = True
                break
        if not placed:
            clusters.append({"start": s, "end": e, "members": [(name, ie)]})

    domains = []
    for c in clusters:
        best_name = min(c["members"], key=lambda x: x[1])[0]
        domains.append({"name": best_name, "start": c["start"], "end": c["end"]})
    domains.sort(key=lambda d: d["start"])

    # 동일 도메인명이 여러 번 등장하면 순번 부여
    name_counts = {}
    for d in domains:
        name_counts[d["name"]] = name_counts.get(d["name"], 0) + 1
    seen = {}
    for d in domains:
        if name_counts[d["name"]] > 1:
            seen[d["name"]] = seen.get(d["name"], 0) + 1
            d["label"] = f"{d['name']}_{seen[d['name']]}"
        else:
            d["label"] = d["name"]

    print(f"[Module 2.2] 최종 확정 도메인: {[(d['label'], d['start'], d['end']) for d in domains]}")
    return domains


# ============================================================
# Methods 2.3 — 링커 후보 정의 (이차구조 + 구조적 압축도)
# ============================================================

def compaction_ratio(coords: dict, s: int, e: int) -> float:
    pts = np.array([coords[r] for r in range(s, e + 1) if r in coords])
    n = len(pts)
    if n < 3:
        return 1.0  # 데이터 부족 시 링커로 간주(보수적 처리)
    end_to_end = np.linalg.norm(pts[-1] - pts[0])
    max_extended = (n - 1) * CA_CA_BOND_LENGTH
    return end_to_end / max_extended if max_extended > 0 else 1.0


def identify_linkers(domains: list, ss_map: dict, ca_coords: dict, total_len: int) -> tuple:
    """도메인 사이 gap을 검증하여 (고신뢰 링커 목록, 미식별 도메인 목록) 반환.

    Methods 2.3: gap 전체를 링커로 보지 않고, gap 내에서 가장 긴 연속 coil
    구간(run)의 좌표를 링커의 최종 좌표로 사용한다. 이는 수동 분석(README
    Result I, 3.1-3.2)에서 도메인 경계에 가장 가까운 순수 coil 구간만을
    링커로 확정한 절차와 동일하다.
    """
    gaps = []
    for i in range(len(domains) - 1):
        d1, d2 = domains[i], domains[i + 1]
        gaps.append({"label": f"{d1['label']}-{d2['label']}", "start": d1["end"], "end": d2["start"]})

    linkers = []
    unassigned = []

    for g in gaps:
        gs, ge = g["start"], g["end"]
        residues = [r for r in range(gs + 1, ge) if r in ss_map]
        if not residues:
            continue
        h = sum(1 for r in residues if ss_map[r] == "H") / len(residues)
        e = sum(1 for r in residues if ss_map[r] == "E") / len(residues)

        needs_review = (h >= HELIX_STRAND_REVIEW_THRESHOLD) or (e >= HELIX_STRAND_REVIEW_THRESHOLD)

        if needs_review:
            ratio = compaction_ratio(ca_coords, gs, ge)
            if ratio < COMPACTION_DOMAIN_LIKE_CUTOFF:
                g["compaction_ratio"] = ratio
                g["helix_frac"] = h
                g["strand_frac"] = e
                unassigned.append(g)
                continue

        # gap 내 가장 긴 연속 coil run을 찾아 링커의 최종 좌표로 사용
        runs = []
        cur_start, cur_type = None, None
        for i, r in enumerate(residues):
            t = ss_map[r]
            if cur_type is None:
                cur_start, cur_type = r, t
            elif t != cur_type or r != residues[i - 1] + 1:
                runs.append((cur_type, cur_start, residues[i - 1]))
                cur_start, cur_type = r, t
        runs.append((cur_type, cur_start, residues[-1]))

        coil_runs = [(s, e) for t, s, e in runs if t == "C"]
        if not coil_runs:
            continue
        longest = max(coil_runs, key=lambda x: x[1] - x[0])

        g["start"], g["end"] = longest[0], longest[1]
        g["helix_frac"] = h
        g["strand_frac"] = e
        linkers.append(g)

    print(f"[Module 2.3] 고신뢰 링커 {len(linkers)}개, 미식별 도메인 {len(unassigned)}개로 분류")
    return linkers, unassigned


# ============================================================
# Methods 2.4 — 취약도 평가
# ============================================================

def evaluate_vulnerability(linkers: list, plddt: dict, pae: np.ndarray, total_len: int) -> list:
    max_pae = float(pae.max()) if pae.size else 31.0
    for lk in linkers:
        ls, le = lk["start"], lk["end"]
        vals = [plddt[r] for r in range(ls, le + 1) if r in plddt]
        avg_plddt = round(float(np.mean(vals)), 1) if vals else 0.0
        min_plddt = round(float(np.min(vals)), 1) if vals else 0.0

        left = max(0, ls - PAE_FLANK)
        right = min(total_len, le + PAE_FLANK)
        avg_pae = round(float(np.mean(pae[left:ls, le:right])), 1) if ls > left and right > le else 0.0

        vuln = round((100 - avg_plddt) / 100 * 50 + (avg_pae / max_pae) * 50, 1)
        lk.update(avg_plddt=avg_plddt, min_plddt=min_plddt, avg_pae=avg_pae, vuln_score=vuln)
    return linkers


# ============================================================
# Methods 2.5 — 촉매 잔기 검증 및 재설계 판정
# ============================================================

def find_catalytic_residues(protein: str) -> set:
    positions = set()
    for motifs in CATALYTIC_MOTIFS.values():
        for pattern, offset in motifs:
            for m in re.finditer(pattern, protein):
                positions.add(m.start() + 1 + offset)
    return positions


def make_verdict(linkers: list, catalytic_positions: set) -> list:
    for lk in linkers:
        cat_in = sorted(p for p in catalytic_positions if lk["start"] <= p <= lk["end"])
        lk["catalytic_in_linker"] = cat_in
        length = lk["end"] - lk["start"]
        if lk["vuln_score"] < VULN_NO_NEED_CUTOFF:
            lk["verdict"] = "NO-NEED"
        elif cat_in:
            lk["verdict"] = "SKIP"
        elif length < MIN_LINKER_LENGTH:
            lk["verdict"] = "SKIP"
        else:
            lk["verdict"] = "REDESIGN"
    return linkers


# ============================================================
# 출력
# ============================================================

def save_results(linkers: list, unassigned: list, out_dir: Path, protein_name: str, protein: str):
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / f"{protein_name}_linker_report.csv"
    fields = ["label", "start", "end", "helix_frac", "strand_frac",
              "avg_plddt", "min_plddt", "avg_pae", "vuln_score",
              "catalytic_in_linker", "verdict"]
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for lk in linkers:
            row = dict(lk)
            row["catalytic_in_linker"] = ";".join(map(str, lk.get("catalytic_in_linker", [])))
            w.writerow(row)
    print(f"[출력] {csv_path}")

    unassigned_path = out_dir / f"{protein_name}_unassigned_regions.csv"
    with open(unassigned_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["label", "start", "end", "compaction_ratio", "helix_frac", "strand_frac"])
        w.writeheader()
        w.writerows(unassigned)
    print(f"[출력] {unassigned_path}")

    fasta_path = out_dir / f"{protein_name}_redesign_targets.fasta"
    with open(fasta_path, "w") as f:
        for lk in linkers:
            if lk["verdict"] == "REDESIGN":
                f.write(f">{protein_name}_{lk['label']}_aa{lk['start']}-{lk['end']}\n")
                f.write(protein[lk["start"] - 1:lk["end"]] + "\n")
    print(f"[출력] {fasta_path}")


# ============================================================
# 메인
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="PKS Linker Identification & Vulnerability Pipeline")
    parser.add_argument("--fasta", required=True)
    parser.add_argument("--pdb", required=True)
    parser.add_argument("--json", required=True)
    parser.add_argument("--output", default="./results")
    parser.add_argument("--name", default=None)
    parser.add_argument("--hmm-dir", default=str(Path(__file__).parent / "hmm_data"))
    args = parser.parse_args()

    out_dir = Path(args.output)
    work_dir = out_dir / "_work"
    work_dir.mkdir(parents=True, exist_ok=True)
    protein_name = args.name or Path(args.fasta).stem

    print(f"\n{'='*60}\nPKS Linker Pipeline — {protein_name}\n{'='*60}\n")

    protein = load_protein_sequence(args.fasta)
    plddt = load_plddt(args.pdb)
    ca_coords = load_ca_coords(args.pdb)
    pae = load_pae(args.json)
    ss_map = run_dssp(args.pdb, work_dir)
    total_len = len(plddt)

    hmms = load_hmm_library(Path(args.hmm_dir))
    raw_hits = scan_domains(protein, hmms)
    domains = merge_domains(raw_hits)

    if len(domains) < 2:
        sys.exit("[종료] 확정된 도메인이 2개 미만이라 링커를 정의할 수 없습니다.")

    linkers, unassigned = identify_linkers(domains, ss_map, ca_coords, total_len)
    if not linkers:
        sys.exit("[종료] 고신뢰 링커를 찾지 못했습니다.")

    linkers = evaluate_vulnerability(linkers, plddt, pae, total_len)
    catalytic_positions = find_catalytic_residues(protein)
    linkers = make_verdict(linkers, catalytic_positions)

    print(f"\n[최종 판정]")
    for lk in linkers:
        print(f"  {lk['verdict']:10s} {lk['label']:25s} aa{lk['start']}-{lk['end']}  "
              f"pLDDT={lk['avg_plddt']}  PAE={lk['avg_pae']}  score={lk['vuln_score']}")

    save_results(linkers, unassigned, out_dir, protein_name, protein)
    print(f"\n완료. 결과 폴더: {out_dir}\n")


if __name__ == "__main__":
    main()
