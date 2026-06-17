# Type I Polyketide Synthase의 링커 규명 및 취약 링커 탐색 자동화

---

## 1. Introduction

Polyketide Synthase(PKS) 중 Type I PKS는 여러 촉매 도메인이 하나의 긴 사슬 위에 선형으로 배열되어 있으며, 각 도메인은 유연한 링커(Linker)로 연결된다. 이 링커는 도메인 간의 유기적인 움직임을 보장하는 핵심 요소이지만, 대장균 등 이종 숙주에서 발현시킬 때 세포 내 프로테아제(Protease)에 의해 쉽게 분해되어 단백질 구조적 불안정성의 주요 원인이 된다(Walker et al., 2019). 또한 유용 물질 생산을 위해 도메인을 교환(Domain swapping)할 때, 부적절한 링커 설계는 효소 활성을 완전히 떨어뜨리거나 단백질 응집(Aggregation)을 유발한다(Englund et al., 2023). 따라서 정확한 링커 경계 식별과 취약성 평가는 PKS 대사공학에서 중요한 부분이다.

기존 연구들은 AlphaFold나 생성형 AI를 활용해 링커를 분석·재설계하려는 시도를 해왔으나, 모두 특정 PKS 한 종에만 수동적으로 적용된 사례였다. 데이터베이스에 존재하는 수만 개의 임의의 Type I PKS 서열을 입력했을 때, 도메인 경계를 정확히 구획하고 구조적으로 취약한 링커를 자동으로 찾아내는 범용 파이프라인은 아직 보고된 바 없다.

이에 본 연구에서는 통계적 도메인 탐지(HMM)와 구조적 비정형성 지표(이차구조, 압축도)를 결합하여 링커 경계를 정확히 도출하고, AlphaFold의 구조 신뢰도 지표(pLDDT, PAE)를 적용하여 구조적으로 취약한 링커를 자동으로 식별하는 파이프라인을 구축하고자 한다. 이 연구의 출발점은 다음 두 질문이다.

> **Research Question 1.** 여러 도메인을 가지는 임의의 Type I PKS에서, 통계적으로 검증된 도메인 탐지(HMM)와 구조적 비정형성 지표(이차구조, 구조적 압축도)를 결합하여 도메인 간 링커를 찾을 수 있는가?
>
> **Research Question 2.** 식별된 링커에 AlphaFold 구조 신뢰도 지표(pLDDT, PAE)를 적용하여 취약한 링커를 구별하고, 이를 자동화 파이프라인으로 구현할 수 있는가?

### 분석 흐름 overview

```
입력: FASTA(또는 CDS) + AlphaFold PDB + AlphaFold PAE JSON
        │
        ▼
[1] HMM 도메인 탐지 (i-evalue < 1e-5)
        │  → "이 단백질이 실제로 가진 도메인"을 사전 가정 없이 확정
        ▼
[2] 도메인 사이 gap 추출 → DSSP 이차구조 분석
        │  → Helix/Strand 비율 30% 이상이면 구조적 압축도 추가 검증
        │     (compaction ratio < 0.20 → 링커가 아닌 미식별 도메인으로 재분류)
        ▼
[3] 고신뢰 링커 확정 → pLDDT·PAE로 취약도 점수화
        ▼
[4] 촉매 잔기 위치와 대조 → REDESIGN / SKIP / NO-NEED 판정
        ▼
출력: 링커 좌표, 취약도, 재설계 대상 목록
```

검증은 두 단계로 진행하였다. 1차로 *Neonothopanus nambi* 유래 Hispidin synthase(NnHispS)에 전체 방법론을 적용하였고, 2차로 도메인 구성이 전혀 다른 *Dictyostelium discoideum* 유래 Probable polyketide synthase 25(PKS25)에 동일한 방법론을 적용해 교차 검증하였다. 마지막으로 전체 절차를 자동화 스크립트로 구현하여 수동 분석과 동일한 결과를 산출하는지 확인하였다.

---

## 2. Materials and Methods

### 2.1 서열 및 구조 데이터 확보

CDS로 확보한 서열은 Biopython으로 단백질 서열로 번역하였다. AlphaFold PDB의 B-factor 컬럼은 잔기별 pLDDT, PAE JSON은 (서열길이)×(서열길이) 위치 불확실성 행렬이다.

**Workflow**
- **Input**:
  - NnHispS CDS FASTA
  - [AF-A0A3G9K3K9 PDB / PAE JSON](#)
  - PKS25 UniProt Q54KU3 단백질 FASTA
  - [AF-Q54KU3 PDB / PAE JSON](#)
- **Tool**:
  - [Biopython](https://biopython.org/)
- **Output**:
  - [NnHispS.fasta](#)
  - [PKS25.fasta](#)

### 2.2 도메인 경계 탐지 (HMM)

antiSMASH 저장소의 PKS/NRPS 전용 HMM 4종(총 166개 모델)을 pyhmmer로 스캔하고, **i-evalue < 1e-5**를 통과한 매칭만 도메인으로 채택하였다. 이 임계값은 예비 스캔에서 가짜 양성(i-evalue > 1)과 신뢰 가능한 매칭(i-evalue < 1e-10) 사이에 뚜렷한 간극이 관찰되어, 이를 가르는 보수적 경계로 설정한 것이다. 이 절차는 "PKS는 어떤 도메인을 가져야 한다"는 사전 가정을 두지 않으므로, 입력 서열마다 다른 도메인 구성이 자동으로 도출된다. 좌표가 겹치는 매칭은 하나의 도메인으로 병합하고(대표 명칭은 i-evalue 최솟값 모델), 단순히 인접한 매칭은 병합하지 않는다.

**Workflow**
- **Input**:
  - NnHispS.fasta / PKS25.fasta
  - [nrpspksdomains.hmm, ksdomains.hmm, dockingdomains.hmm, abmotifs.hmm](#)
- **Tool**:
  - [pyhmmer](https://github.com/althonos/pyhmmer) (`hmmscan`)
  - [antiSMASH HMM library](https://github.com/antismash/antismash)
- **Output**:
  - [NnHispS_domains.csv](#)
  - [PKS25_domains.csv](#)

### 2.3 링커 후보 정의 (이차구조 + 구조적 압축도)

도메인 사이 gap을 곧바로 링커로 보지 않고 두 단계로 검증하였다.

**1단계 — DSSP 이차구조.** mkdssp로 잔기별 이차구조를 H(helix)/E(strand)/C(coil)로 단순화하고, 각 gap의 Helix·Strand 비율을 계산한다. 비율이 약 30% 이상이면 정형 구조 혼재로 보고 2단계로 넘긴다. PKS 링커 길이는 문헌상 20~550 aa로 편차가 커서, 길이나 coil 비율에 고정 숫자 기준을 두지 않고 이 정성적 신호만 사용하였다.

**2단계 — 구조적 압축도.** 1단계에서 넘어온 gap에 대해서만 CA 좌표로 compaction ratio(End-to-end distance / [(잔기 수 − 1) × 3.8 Å])를 계산한다. 비율이 1에 가까우면 펴진 구조(링커), 0에 가까우면 되돌아오는 globular 구조(도메인)로 해석한다. 도메인 대조군(ratio 0.01)과 링커 대조군(ratio 0.60) 사이에서 **0.20 미만**이면 링커가 아닌 미식별 도메인으로 재분류한다.

**Workflow**
- **Input**:
  - NnHispS_domains.csv / PKS25_domains.csv
  - AF-A0A3G9K3K9 PDB / AF-Q54KU3 PDB
- **Tool**:
  - [mkdssp (DSSP v4.2.2)](https://github.com/PDB-REDO/dssp)
- **Output**:
  - [NnHispS_linkers.csv](#)
  - [PKS25_linkers.csv](#)

### 2.4 취약도 평가 (pLDDT, PAE)

확정된 링커에 대해서만 다음 점수를 계산한다.

```
취약도 점수 = 0.5 × (100 − 평균 pLDDT)/100 × 100  +  0.5 × (도메인 간 PAE / 해당 단백질 최대 PAE) × 100
```

도메인 간 PAE는 링커 양옆 60 aa flank 범위의 PAE 평균이다(인접 도메인의 영향은 포함하되 먼 도메인까지 포함시켜 신호가 희석되지 않도록 한 절충값).

**Workflow**
- **Input**:
  - NnHispS_linkers.csv
  - AF-A0A3G9K3K9 PAE JSON
- **Tool**:
  - NumPy
- **Output**:
  - [NnHispS_vulnerability.csv](#)

### 2.5 촉매 잔기 검증 및 판정

KS-Cys(`HGTGT` 인접), AT-Ser(`GHSxG`/`AFSGQGT`), ACP-Ser(`LGxDS`/`LGxTS`/`LGxES`) 모티프로 촉매 잔기를 탐지하고, HMM 도메인 좌표와 대조하여 다음 판정을 적용한다.

```
취약도 < 30                         →  NO-NEED
취약도 ≥ 30  AND  촉매 잔기 포함      →  SKIP
취약도 ≥ 30  AND  촉매 잔기 미포함    →  REDESIGN
```

임계값 30은 6개 gap의 실제 취약도 분포(9.5~62.9)에서 안정 구간(9~25)과 취약 구간(35 이상)이 갈리는 지점이다.

**Workflow**
- **Input**:
  - NnHispS_vulnerability.csv
- **Tool**:
  - Python `re`
- **Output**:
  - [NnHispS_final_verdict.csv](#)

---

## 3. Results

### Result I — 링커 찾기 (NnHispS)

NnHispS의 FASTA 서열을 입력으로 PKS/NRPS HMM 라이브러리를 대상으로 hmmscan을 수행하였고, i-evalue < 1e-5를 기준으로 6개 도메인이 채택되었다(AMP-binding, ACP_1, KS, Docking domain, AT, ACP_2). 총 6개 도메인이 확인됨에 따라 5개의 도메인 간 gap이 정의되었으며, 이들을 잠재적 링커 후보로 간주하여 DSSP 기반 이차구조 조성을 분석하였다.

Helix 비율이 30% 이상인 두 gap(AMP–ACP_1, AT–ACP_2)은 compaction ratio를 계산한 결과 둘 다 0.09로, 도메인 대조군(0.01)에 가깝고 링커 대조군(0.60)과는 뚜렷이 구분되어 미식별 도메인으로 재분류하였다. PKS/NRPS HMM 라이브러리 재스캔에서도 매칭되는 모델이 없어 정확한 정체는 확인하지 못했다.

**Figure 1.** NnHispS의 HMM으로 확인한 도메인과 DSSP coil 기반 링커 후보 부위 map.

<img width="2365" height="664" alt="image" src="https://github.com/user-attachments/assets/fe902897-1be7-4dde-94fa-1e25ec9d403d" />

Figure 1을 통해 확인한 결과, 총 5개의 도메인 간 gap 중 2개 구간은 gap처럼 보이지만 높은 helix 비율과 낮은 compaction ratio로 인해 링커는 아닌 것으로 판단되었다. 나머지 L1(ACP_1–KS), L2(KS–Docking), L3(Docking–AT)는 gap이자 링커적인 특징을 모두 보여 링커로 최종 확정하였다.

### Result II — 취약 부위 도출 (NnHispS)

확정된 3개 링커가 동일한 수준의 구조적 취약성을 가지는지 확인하고자 하였다. 일부 링커만 구조적 불안정성을 나타낸다면 재설계의 우선순위를 결정할 수 있다. AlphaFold의 pLDDT와 PAE로 각 링커의 취약도를 정량화한 결과는 다음과 같다.

**Figure 2.** 확정된 링커 3개의 pLDDT 프로파일 및 도메인 간 PAE·취약도 비교.

<img width="2254" height="1125" alt="image" src="https://github.com/user-attachments/assets/93721d7c-52b6-4d30-848d-912908c44523" />


6개 도메인 자체의 평균 pLDDT는 78.5–93.5로 모두 안정적이었고, 링커 구간에서만 뚜렷한 저하가 관찰되어 도메인-링커 경계 확정이 구조적으로도 타당함을 추가로 확인하였다. 특히 L1은 가장 낮은 pLDDT와 높은 PAE를 나타내어 세 링커 중 가장 취약한 부위로 확인되었다.

### Result III — 검증: 촉매 잔기 확인 및 재설계 판정

취약성이 높은 링커라도 해당 부위가 촉매 활성에 직접 관여한다면 재설계는 오히려 효소 기능을 손상시킬 수 있다. 따라서 보존된 촉매 잔기의 위치를 탐색하고 링커 좌표와 비교하였다.

**Figure 3.** 촉매 잔기(보존 위치) 표시를 포함한 NnHispS 최종 검증 맵.

<img width="2512" height="770" alt="image" src="https://github.com/user-attachments/assets/dfca8cdc-0ef7-4ea5-a6b1-b15d03bd5591" />

모든 촉매 잔기는 각 도메인 내부에 위치하였으며 고신뢰 링커와 중복되지 않았다. L1과 L2는 취약도 임계값을 넘으면서 촉매 잔기도 없어 REDESIGN으로, L3는 취약도가 낮아 NO-NEED로 판정되었다. 취약성이 높으면서도 촉매 기능을 직접 교란하지 않는 링커를 재설계 대상으로 우선 선정할 수 있었다.

### Result IV — 교차 검증 (PKS25)

NnHispS를 기반으로 구축된 링커 탐색 기준이 특정 단백질에만 최적화된 결과일 가능성을 배제하기 위해, 도메인 구성이 다른 PKS25(KS-AT-DH-ER-KR, 환원형 모듈형 PKS)에 동일한 방법론을 적용해 교차 검증하였다. NnHispS와 달리 DH, ER이 확정되었고 AMP-binding, docking domain은 검출되지 않아, 도메인 구성이 입력 서열에 따라 자동으로 달라짐을 보였다.

**Figure 4.** PKS25(*Dictyostelium discoideum*, UniProt Q54KU3 / AlphaFold AF-Q54KU3)의 HMM 확정 도메인과 링커.

<img width="2525" height="831" alt="image" src="https://github.com/user-attachments/assets/c321415d-a8c4-49d1-85a0-3c5e101e8610" />


도메인 탐지 이후 구조 검증을 통해 실제 링커와 미식별 구조 영역이 구분되었으며, NnHispS에서 관찰된 의사결정 흐름이 동일하게 재현되었다. DH–ER 사이 521 aa gap은 NnHispS의 미식별 구간과 동일하게 Helix/Strand 비율이 30% 내외로 높아 같은 기준으로 분류되었다. 이는 "짧은 gap은 coil 우세, 긴 gap은 정형 구조 혼재"라는 판단 기준이 진균 비환원형 PKS와 아메바 환원형 모듈형 PKS라는 진화적으로 거리가 먼 두 단백질에서 공통적으로 관찰됨을 보여주며, 본 연구의 프레임워크가 특정 PKS에 대한 경험적 규칙이 아니라 Type I PKS가 공유하는 구조적 특성을 반영하는 범용적 접근법일 가능성을 시사한다.

### Result V — 자동화 파이프라인 검증

본 연구에서 구축한 분석 체계는 여러 단계를 거치는 순차적 과정으로 이루어져 있어, 대량의 PKS 분석에 수동으로 적용하기에는 현실적인 한계가 있다. 따라서 전체 과정을 자동화하더라도 전문가 수준의 결과를 재현할 수 있는지를 검증하고자 하였다.

**Figure 5.** NnHispS, PKS25 각각에서 수동 분석(상단)과 자동화 결과(하단) 링커 좌표 페어 비교.

<img width="2383" height="1093" alt="image" src="https://github.com/user-attachments/assets/a5b14c9c-3bdb-40b2-ae19-9c936af45e67" />

유일한 차이는 NnHispS L1 링커의 끝 좌표(수동 685, 자동화 684)로, 같은 DSSP 출력에서 가장 긴 연속 coil run을 추출하는 동일 절차이므로 round-off 수준의 사소한 차이로 판단된다. 도메인 경계, 미식별 구간, 링커 좌표(1 aa 이내), 최종 판정 모두에서 자동화 결과가 수동 분석과 일치하였다.

본 연구의 자동화 파이프라인은 분석 정확도를 유지하면서도 재현성과 확장성을 크게 향상시킬 수 있음을 확인하였다. 이는 개별 PKS 사례 분석을 넘어, 다양한 Type I PKS를 대상으로 한 고처리량(high-throughput) 링커 탐색 및 재설계 플랫폼으로 활용될 가능성을 보여준다.

**Workflow**
- **Input**:
  - NnHispS.fasta / PKS25.fasta / AlphaFold PDB / AlphaFold PAE JSON
- **Tool**:
  - [pks_linker_pipeline.py](#)
- **Output**:
  - [NnHispS_linker_report.csv](#)
  - [PKS25_linker_report.csv](#)

---

## 4. Conclusion

**Research Question 1**
HMM 기반 도메인 탐지(i-evalue < 1e-5)와 이차구조·구조적 압축도 검증을 결합하면 임의의 Type I PKS에서 도메인 간 링커를 찾을 수 있다는 것을 확인하였다. 도메인 구성과 진화적 기원이 전혀 다른 NnHispS와 PKS25 모두에서, 짧은 gap은 링커로 확정되고 긴 gap은 압축도 검증을 거쳐 미식별 영역으로 분류되는 동일한 패턴이 재현되었다.

**Research Question 2**
pLDDT·PAE로 취약 링커를 구별하고 이를 자동화할 수 있다는 것을 확인하였다. NnHispS에서 L1이 가장 취약한 링커로 식별되었고, 촉매 잔기 대조 결과 L1·L2는 재설계 대상, L3는 재설계 불필요로 판정되었다. 전체 절차를 스크립트(`pks_linker_pipeline.py`)로 구현해 NnHispS와 PKS25에 실행한 결과, 도메인 경계·미식별 구간·링커 좌표·최종 판정 모두 수동 분석과 일치하였다.

본 연구는 두 PKS의 링커를 찾은 것을 넘어, FASTA(또는 CDS), AlphaFold PDB, AlphaFold PAE JSON 세 파일만 주어지면 도메인 경계 탐지부터 재설계 대상 판정까지 자동으로 수행하는 재현 가능한 파이프라인을 구축하고, 이를 독립적인 두 PKS 사례로 검증했다는 데 의의가 있다.

---

## 5. Discussion

**범용화의 의의.** 
본 연구의 핵심 기여는 특정 PKS 한 종의 링커를 정확히 찾은 것이 아니라, 그 절차 자체가 진화적으로 거리가 먼 PKS에도 동일하게 적용된다는 것을 검증했다는 점에 있다. NnHispS와 PKS25는 도메인 구성, 환원 여부, 생물학적 기원이 모두 다름에도 동일한 임계값과 절차가 작동했다는 것은, 이 방법론이 특정 서열에 맞춰 조정된 것이 아니라 Type I PKS가 공유하는 더 일반적인 구조적 특징(도메인은 globular하고 링커는 펴져 있다)에 기반함을 시사한다. 다만 검증 사례가 2개에 불과하므로, 더 많은 PKS, 특히 도메인 수가 훨씬 많은 다중 모듈 어셈블리 라인에 대한 추가 검증이 필요하다.

**파라미터 근거 수준에 대한 한계.** 
Methods의 수치형 파라미터들은 근거 수준이 균일하지 않다. i-evalue 임계값(1e-5)과 취약도 임계값(30)은 실제 데이터 분포에서 관찰된 간극에 근거하여 비교적 견고하다. 반면 helix/strand 검토 임계값(30%), 압축도 cutoff(0.20), PAE flank(60 aa)는 외부 문헌으로 검증된 표준값이 아니라, 본 연구가 NnHispS·PKS25 두 사례를 분석하며 시행착오를 거쳐 정착시킨 잠정적 기준이다. 더 많은 PKS 사례가 누적되면 이 값들을 통계적으로 재추정하거나, 고정 임계값 대신 데이터 분포 기반의 적응적 기준으로 대체하는 것이 바람직하다.

---

## Reference

1. Blin, K., Shaw, S., Augustijn, H. E., Reitz, Z. L., Biermann, F., Alanjary, M., Fetter, A., Terlouw, B. R., Metcalf, W. W., Helfrich, E. J. N., van Wezel, G. P., Medema, M. H., & Weber, T. (2023). antiSMASH 7.0: new and improved predictions for detection, regulation, chemical structures and visualisation. *Nucleic Acids Research*, 51(W1), W46–W50. https://doi.org/10.1093/nar/gkad344
2. Varadi, M., Anyango, S., Deshpande, M., et al. (2022). AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models. *Nucleic Acids Research*, 50(D1), D439–D444.
3. Walker, M. C., et al. (2019). Expanding the structural diversity of polyketides by ​combinatorial biosynthesis. *Nature Reviews Chemistry*.
4. Englund, E., et al. (2023). Robust expression of engineered polyketide synthases via linker engineering. (관련 문헌)

---

## 사용 파일

| 파일 | 설명 |
|---|---|
| [`pks_linker_pipeline.py`](#) | Result V에서 검증한 자동화 스크립트 (Methods 2.2–2.5 구현) |
| [`hmm_data/`](#) | 스크립트 실행에 필요한 HMM 라이브러리 4종 |
| [`QnA.md`](#) | 방법론 정립 과정의 시행착오 전체 기록 |
