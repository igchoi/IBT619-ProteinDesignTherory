## 1. 후보 서열 파일

분석에 사용한 후보 서열은 FASTA 형식으로 정리하였다.

| 파일 | 내용 |
|---|---|
| `candidates.fasta` | Design A-E 전체 후보 서열 |
| `candidate_B.fasta` | 최종 후보 Design B 서열 |

Design B 서열은 다음과 같다.

```text
>Design_B_amp_helix_moderate
KLAKQLSEKLKQALSKQLAELKQALSKQLAELKKQS
```

## 2. ColabFold 1차 구조 예측

전체 후보 5개에 대해 ColabFold를 이용해 1차 구조 예측을 수행하였다. 이 단계는 후보들을 빠르게 비교하기 위한 screening 목적이었다.

```bash
/tmp/codex-install/envs/colabfold/bin/colabfold_batch \
  candidates.fasta colabfold_results \
  --msa-mode single_sequence \
  --num-models 1 \
  --num-recycle 1 \
  --overwrite-existing-results
```

주요 출력 파일은 `colabfold_results/`에 생성되었고, 이후 분석에 사용할 PDB 파일은 `predicted_structures/` 폴더로 정리하였다.

## 3. 구조 평가 코드

예측된 PDB 구조에서 pLDDT, radius of gyration, helix-like fraction 등을 계산하기 위해 아래 Python script를 사용하였다.

| 파일 | 역할 |
|---|---|
| `evaluate_predicted_structures.py` | 예측 PDB 구조를 읽고 구조 기반 평가 지표 계산 |
| `structure_evaluation.csv` | 구조 평가 결과 표 |
| `structure_evaluation.md` | 구조 평가 결과 Markdown 요약 |

실행 방식은 다음과 같다.

```bash
/tmp/codex-install/envs/colabfold/bin/python evaluate_predicted_structures.py
```

이 분석에서 계산한 주요 지표는 다음과 같다.

- 평균 pLDDT
- 최소 pLDDT
- Low-confidence residue fraction
- Radius of gyration
- Helix-like fraction
- Priority score

## 4. Figure 1-5 생성 코드

초기 보고서용 figure는 아래 script로 생성하였다.

| 파일 | 역할 |
|---|---|
| `make_figures.py` | Figure 1-5 생성 |

실행 명령은 다음과 같다.

```bash
MPLCONFIGDIR=/tmp/codex-install/.mplconfig \
/tmp/codex-install/envs/colabfold/bin/python make_figures.py
```

생성된 figure는 다음과 같다.

| Figure | 파일 | 내용 |
|---|---|---|
| Figure 1 | `figures/Fig1_sequence_evaluation.png` | 후보 서열 기반 평가 |
| Figure 2 | `figures/Fig2_colabfold_plddt.png` | 후보별 ColabFold pLDDT 비교 |
| Figure 3 | `figures/Fig3_structure_heatmap.png` | 구조 기반 평가 heatmap |
| Figure 4 | `figures/Fig4_design_b_structure.png` | Design B 3D 구조 기본 시각화 |
| Figure 5 | `figures/Fig5_design_b_plddt_profile.png` | Design B residue별 pLDDT profile |

## 5. PyMOL 기반 Figure 4 생성

Design B 구조를 논문/보고서용 cartoon representation으로 다시 렌더링하기 위해 PyMOL을 사용하였다.

| 파일 | 역할 |
|---|---|
| `render_design_b_pymol.pml` | Design B PyMOL cartoon 구조 렌더링 |
| `annotate_figure4.py` | Figure 4에 제목, N/C label, pLDDT color bar 추가 |

PyMOL 렌더링 명령은 다음과 같다.

```bash
LIBGL_ALWAYS_SOFTWARE=1 \
/tmp/codex-install/envs/colabfold/bin/pymol -cq render_design_b_pymol.pml
```

Figure 4 주석 추가 명령은 다음과 같다.

```bash
/tmp/codex-install/envs/colabfold/bin/python annotate_figure4.py
```

최종 Figure 4로 사용할 파일은 다음과 같다.

```text
figures/Fig4_design_b_structure_pymol_annotated.png
```

## 6. Design B 추가 분석 코드

최종 후보 Design B에 대해 helical wheel plot과 residue별 pLDDT 상세 plot을 추가로 생성하였다.

| 파일 | 역할 |
|---|---|
| `make_design_b_followup.py` | Figure 6, Figure 7 생성 및 Design B pLDDT 요약 작성 |
| `design_b_followup_analysis.md` | Design B 추가 분석 결과 요약 |

실행 명령은 다음과 같다.

```bash
MPLCONFIGDIR=/tmp/codex-install/.mplconfig \
/tmp/codex-install/envs/colabfold/bin/python make_design_b_followup.py
```

생성된 figure는 다음과 같다.

| Figure | 파일 | 내용 |
|---|---|---|
| Figure 6 | `figures/Fig6_design_b_helical_wheel.png` | Design B helical wheel projection |
| Figure 7 | `figures/Fig7_design_b_plddt_detail.png` | Design B residue별 pLDDT 상세 plot |

## 7. Design B 표면 특성 시각화

PyMOL을 이용해 Design B의 표면을 residue 특성별로 색칠하였다. 양전하 residue, 음전하 residue, 소수성 residue, 극성 residue를 서로 다른 색으로 표시하였다.

| 파일 | 역할 |
|---|---|
| `render_design_b_surface_pymol.pml` | Design B residue-property surface 렌더링 |
| `annotate_design_b_surface.py` | Figure 8에 제목과 색상 범례 추가 |

PyMOL 렌더링 명령은 다음과 같다.

```bash
LIBGL_ALWAYS_SOFTWARE=1 \
/tmp/codex-install/envs/colabfold/bin/pymol -cq render_design_b_surface_pymol.pml
```

Figure 8 주석 추가 명령은 다음과 같다.

```bash
/tmp/codex-install/envs/colabfold/bin/python annotate_design_b_surface.py
```

생성된 figure는 다음과 같다.

```text
figures/Fig8_design_b_residue_surface_annotated.png
```

색상 구분은 다음과 같이 설정하였다.

| 색 | 의미 |
|---|---|
| 파란색 | positive Lys |
| 빨간색 | negative Glu |
| 노란색 | hydrophobic Ala/Leu |
| 초록색 | polar Ser/Gln |

## 8. Design B refined ColabFold 재예측

최종 후보 Design B에 대해 ColabFold 조건을 높여 재예측하였다. 이 단계는 Design B의 구조 예측이 여러 model에서도 일관적으로 유지되는지 확인하기 위한 것이다.

```bash
/tmp/codex-install/envs/colabfold/bin/colabfold_batch \
  candidate_B.fasta colabfold_designB_refined \
  --msa-mode single_sequence \
  --num-models 5 \
  --num-recycle 3 \
  --overwrite-existing-results
```

재예측 결과는 `colabfold_designB_refined/` 폴더에 저장되었다.

주요 결과는 다음과 같다.

| Rank | Model | Mean pLDDT | pTM |
|---:|---|---:|---:|
| 1 | alphafold2_ptm_model_5_seed_000 | 97.1 | 0.59 |
| 2 | alphafold2_ptm_model_3_seed_000 | 97.1 | 0.61 |
| 3 | alphafold2_ptm_model_4_seed_000 | 96.8 | 0.57 |
| 4 | alphafold2_ptm_model_1_seed_000 | 94.5 | 0.53 |
| 5 | alphafold2_ptm_model_2_seed_000 | 92.3 | 0.49 |

## 9. Refined 구조 Figure 9 생성

Design B refined ColabFold rank 1 구조를 PyMOL로 렌더링하고, 보고서용으로 주석을 추가하였다.

| 파일 | 역할 |
|---|---|
| `render_design_b_refined_pymol.pml` | refined ColabFold rank 1 구조 PyMOL 렌더링 |
| `annotate_figure9.py` | Figure 9에 제목, 조건, N/C label, pLDDT color bar 추가 |

PyMOL 렌더링 명령은 다음과 같다.

```bash
LIBGL_ALWAYS_SOFTWARE=1 \
/tmp/codex-install/envs/colabfold/bin/pymol -cq render_design_b_refined_pymol.pml
```

Figure 9 주석 추가 명령은 다음과 같다.

```bash
/tmp/codex-install/envs/colabfold/bin/python annotate_figure9.py
```

최종 Figure 9로 사용할 파일은 다음과 같다.

```text
figures/Fig9_design_b_refined_structure_annotated.png
```

## 10. 보고서 작성 파일

최종적으로 분석 결과를 정리한 보고서 Markdown 파일은 다음과 같다.

| 파일 | 내용 |
|---|---|
| `protein_design_report_draft.md` | 영문 보고서 초안 |
| `protein_design_report_draft_kr.md` | 국문 보고서 초안 |
| `protein_design_report_draft_kr_naive.md` | 최종 제출용에 가까운 자연스러운 국문 보고서 |

최종 보고서로는 아래 파일을 사용하면 된다.

```text
protein_design_report_draft_kr_naive.md
```

## 11. 전체 분석 흐름 요약

전체 분석은 다음 순서로 진행하였다.

1. 항균 펩타이드 유사 후보 5개 설계
2. 후보 서열의 전하, 소수성, helix propensity, hydrophobic moment 평가
3. ColabFold를 이용한 후보별 1차 구조 예측
4. PDB 구조 기반 pLDDT, radius of gyration, helix-like fraction 평가
5. Design B를 최종 후보로 선정
6. Design B 구조를 PyMOL로 시각화
7. Design B helical wheel plot 생성
8. Design B 표면 residue-property 시각화
9. Design B를 더 높은 ColabFold 조건으로 재예측
10. 최종 보고서 Markdown에 결과 통합

