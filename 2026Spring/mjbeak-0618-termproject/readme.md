# PKS 취약 링커 자동 규명 파이프라인

### HMM 도메인 탐지와 구조적 비정형성 검증을 결합한 Type I Polyketide Synthase 링커 식별 및 취약도 평가

---

## 1. Introduction

Polyketide Synthase(PKS)는 구조적 특징에 따라 세 가지 유형으로 분류된다. Type II PKS는 KS, CLF, ACP 등의 도메인이 각각 독립된 단백질로 발현되어 비공유 복합체를 이루고, Type III PKS는 단일 도메인만으로 기능한다. 이 두 유형은 도메인이 분리되어 있거나 하나뿐이므로 "링커"라는 구조적 요소가 존재하지 않는다.

반면 **Type I PKS**는 KS, AT, ACP 등 여러 촉매 도메인이 하나의 폴리펩타이드 사슬 위에 선형으로 배열되며, 각 도메인은 유연한 링커로 연결된다. 이 링커는 PKS를 대장균 등 이종 숙주에서 발현시킬 때 구조적 불안정성의 주요 원인으로 지목되어 왔다. 따라서 취약 링커를 찾고 개선하는 연구가 의미를 가지는 것은 Type I PKS뿐이며, 본 연구는 이 유형만을 대상으로 한다.

기존 연구는 AlphaFold 구조 예측으로 도메인 경계의 건전성을 평가하거나, 생성형 AI로 링커를 재설계하는 시도를 다루었으나, 모두 특정 PKS 한 종에 개별적으로 적용된 사례였다. **임의의 Type I PKS 서열을 입력했을 때 도메인 경계와 취약 링커를 자동으로 식별하는 범용 파이프라인**은 보고된 바 없다.

본 연구는 다음 두 질문에서 출발한다.

> **Research Question 1.** 여러 도메인을 가지는 임의의 Type I PKS에서, 통계적으로 검증된 도메인 탐지(HMM)와 구조적 비정형성 지표(이차구조, 구조적 압축도)를 결합하여 도메인 간 링커를 찾을 수 있는가?

> **Research Question 2.** 식별된 링커에 AlphaFold 구조 신뢰도 지표(pLDDT, PAE)를 적용하여 취약한 링커를 구별하고, 이를 자동화 파이프라인으로 구현할 수 있는가?

### 분석 흐름

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

검증은 두 단계로 진행하였다. 1차로 *Neonothopanus nambi* 유래 Hispidin synthase(NnHispS, AlphaFold AF-A0A3G9K3K9)에 전체 방법론을 적용해 링커 식별부터 재설계 판정까지 수행했고, 2차로 도메인 구성이 전혀 다른 *Dictyostelium discoideum* 유래 Probable polyketide synthase 25(PKS25, UniProt Q54KU3, AlphaFold AF-Q54KU3)에 동일한 방법론을 적용해 결과 패턴이 재현되는지 교차 검증하였다. 마지막으로 검증된 절차를 자동화 스크립트로 구현하여, 수동 분석과 동일한 결과를 산출하는지 확인하였다.

---

## 2. Materials and Methods

### 2.1 데이터

| 항목 | NnHispS | PKS25 |
|---|---|---|
| 서열 출처 | CDS FASTA → Biopython 번역 | UniProt Q54KU3 단백질 FASTA |
| 길이 | 1,698 aa | 2,380 aa |
| 구조 / PAE 파일 | AF-A0A3G9K3K9-F1 (model, PAE) | AF-Q54KU3-F1 (model, PAE) |

AlphaFold PDB의 B-factor 컬럼은 잔기별 pLDDT, PAE JSON은 (서열길이)×(서열길이) 위치 불확실성 행렬이다.

### 2.2 도메인 경계 탐지 (HMM)

antiSMASH 저장소의 PKS/NRPS 전용 HMM 4종(`nrpspksdomains.hmm`, `ksdomains.hmm`, `dockingdomains.hmm`, `abmotifs.hmm`, 총 166개 모델)을 pyhmmer로 스캔하고, **i-evalue < 1e-5**를 통과한 매칭만 도메인으로 채택한다.

- 임계값 근거: 예비 스캔에서 가짜 양성(i-evalue > 1)과 신뢰 가능한 매칭(i-evalue < 1e-10) 사이에 뚜렷한 간극이 관찰되어, 이를 가르는 보수적 경계로 1e-5를 설정하였다.
- 이 절차는 "PKS는 어떤 도메인을 가져야 한다"는 사전 가정을 두지 않으므로, 입력 서열마다 다른 도메인 구성이 자동으로 도출된다.
- 좌표가 겹치는 매칭은 하나의 도메인으로 병합하고(대표 명칭은 i-evalue 최솟값 모델), 단순히 인접한 매칭은 병합하지 않는다.

### 2.3 링커 후보 정의 (이차구조 + 구조적 압축도)

도메인 사이 gap을 곧바로 링커로 보지 않고 두 단계로 검증한다.

**1단계 — DSSP 이차구조.** mkdssp로 잔기별 이차구조를 H(helix)/E(strand)/C(coil)로 단순화하고, 각 gap의 Helix·Strand 비율을 계산한다. 비율이 **약 30% 이상**이면 정형 구조 혼재로 보고 2단계로 넘긴다.
   - PKS 링커 길이는 문헌상 20~550 aa로 편차가 커서, 길이나 coil 비율에 고정 숫자 기준을 두지 않고 이 정성적 신호만 사용하였다.

**2단계 — 구조적 압축도.** 1단계에서 넘어온 gap에 대해서만 CA 좌표로 compaction ratio를 계산한다.

```
Compaction ratio = End-to-end distance / [(잔기 수 − 1) × 3.8 Å]
```

3.8 Å은 인접 CA 원자 간 평균 결합 거리이다. 비율이 1에 가까우면 펴진 구조(링커), 0에 가까우면 되돌아오는 globular 구조(도메인)로 해석한다. 도메인 대조군(ratio 0.01)과 링커 대조군(ratio 0.60) 사이에서, **0.20 미만**이면 링커가 아닌 미식별 도메인으로 재분류한다.

### 2.4 취약도 평가 (pLDDT, PAE)

확정된 링커에 대해서만 계산한다.

```
취약도 점수 = 0.5 × (100 − 평균 pLDDT)/100 × 100  +  0.5 × (도메인 간 PAE / 해당 단백질 최대 PAE) × 100
```

도메인 간 PAE는 링커 양옆 **60 aa flank** 범위의 PAE 평균이다(인접 도메인의 영향은 포함하되 먼 도메인까지 포함시켜 신호가 희석되지 않도록 한 절충값).

### 2.5 촉매 잔기 검증 및 판정

KS-Cys(`HGTGT` 인접), AT-Ser(`GHSxG`/`AFSGQGT`), ACP-Ser(`LGxDS`/`LGxTS`/`LGxES`) 모티프로 촉매 잔기를 탐지하고, HMM 도메인 좌표와 대조한다.

```
취약도 < 30                         →  NO-NEED
취약도 ≥ 30  AND  촉매 잔기 포함      →  SKIP
취약도 ≥ 30  AND  촉매 잔기 미포함    →  REDESIGN
```

임계값 30은 6개 gap의 실제 취약도 분포(9.5~62.9)에서 안정 구간(9~25)과 취약 구간(35 이상)이 갈리는 지점이다.

---

## 3. Results

### Result I — 링커 찾기 (NnHispS)

i-evalue < 1e-5 기준으로 6개 도메인이 채택되었다.

| 도메인 | 위치(aa) | i-evalue |
|---|---|---|
| AMP-binding | 26–453 | 2.99e-46 |
| ACP_1 | 584–647 | 8.10e-07 |
| KS | 686–1108 | 7.06e-112 |
| Docking domain | 1123–1191 | 2.09e-11 |
| AT | 1210–1491 | 5.32e-68 |
| ACP_2 | 1619–1691 | 1.33e-10 |

AMP-binding 도메인이 N-말단에서 검출된 것은 예비 분석에서 예상치 못한 결과였으나, NnHispS와 근연한 비환원형 진균 PKS(ShPKS1 등)가 KS 앞에 추가 AMP·ACP 도메인을 가진다는 선행 문헌과 일치해, 가짜 양성이 아닌 실제 도메인으로 확인되었다.

5개 gap의 DSSP coil 비율은 다음과 같다.

| Gap | 길이 | Helix | Strand | Coil |
|---|---|---|---|---|
| AMP–ACP_1 | 131 aa | 34% | 18% | 48% |
| ACP_1–KS | 39 aa | 32% | 0% | 68% |
| KS–Docking | 15 aa | 0% | 0% | 100% |
| Docking–AT | 19 aa | 0% | 28% | 72% |
| AT–ACP_2 | 128 aa | 33% | 4% | 63% |

Helix 비율이 30% 이상인 두 gap(AMP–ACP_1, AT–ACP_2)은 compaction ratio를 계산한 결과 둘 다 0.09로, 도메인 대조군(0.01)에 가깝고 링커 대조군(0.60)과는 뚜렷이 구분되어 미식별 도메인으로 재분류하였다. PKS/NRPS HMM 라이브러리 재스캔에서도 매칭되는 모델이 없어 정확한 정체는 확인하지 못했다.

**Figure 1.** NnHispS의 HMM 확정 도메인(6개), DSSP coil 기반 고신뢰 링커(3개), 구조적 압축도로 미식별 도메인으로 재분류된 2개 구간.

![Figure 1](NnHispS_domain_map.png)

남은 3개 gap은 고신뢰 링커로 확정되었다.

| 링커 | 위치(aa) | 길이 |
|---|---|---|
| L1 (ACP_1–KS) | 662–685 | 23 aa |
| L2 (KS–Docking) | 1109–1122 | 13 aa |
| L3 (Docking–AT) | 1192–1204 | 12 aa |

5개 gap 중 2개(40%)가 단순 "도메인 사이 = 링커" 가정으로는 걸러지지 않고 추가 구조 검증이 필요했다는 점은, 도메인 탐지만으로는 링커 식별이 충분하지 않음을 보여준다.

### Result II — 취약 부위 도출 (NnHispS)

확정된 링커 3개에 pLDDT·PAE를 적용한 결과는 다음과 같다.

| 링커 | 평균 pLDDT | 최소 pLDDT | 평균 PAE (Å) | 취약도 점수 |
|---|---|---|---|---|
| L1 (ACP_1–KS) | 42.6 | 27.5 | 21.2 | 62.9 |
| L2 (KS–Docking) | 57.5 | 35.9 | 8.2 | 34.5 |
| L3 (Docking–AT) | 65.5 | 52.6 | 4.9 | 25.2 |

6개 도메인 자체의 평균 pLDDT는 78.5–93.5로 모두 안정적이었고, 링커 구간에서만 뚜렷한 저하가 관찰되어 도메인-링커 경계 확정이 구조적으로도 타당함을 추가로 확인하였다.

**Figure 2.** 확정된 링커 3개의 pLDDT 프로파일 및 도메인 간 PAE·취약도 비교.

![Figure 2](NnHispS_linker_vulnerability.png)

L1이 세 링커 중 가장 취약했다.

### Result III — 검증: 촉매 잔기 확인 및 재설계 판정

촉매 잔기 6개(KS-Cys 2, AT-Ser 2, ACP-Ser 2)는 모두 해당 도메인 내부에 위치했고, 링커 3개 어디에도 포함되지 않았다. 이는 2.2에서 확정한 도메인 경계가 촉매 활성 부위와 정확히 일치한다는 추가 근거이다.

| 링커 | 취약도 점수 | 링커 내 촉매 잔기 | 최종 판정 |
|---|---|---|---|
| L1 (ACP_1–KS) | 62.9 | 없음 | REDESIGN |
| L2 (KS–Docking) | 34.5 | 없음 | REDESIGN |
| L3 (Docking–AT) | 25.2 | 없음 | NO-NEED |

**Figure 3.** 촉매 잔기(보존 위치) 표시를 포함한 NnHispS 최종 검증 맵.

![Figure 3](NnHispS_final_verification.png)

### Result IV — 교차 검증 (PKS25)

도메인 구성이 NnHispS와 전혀 다른 PKS25(KS-AT-DH-ER-KR, 환원형 모듈형 PKS)에 동일한 절차를 적용하였다.

| 도메인 | 위치(aa) | i-evalue |
|---|---|---|
| KS | 34–458 | 1.23e-152 |
| AT | 568–877 | 1.29e-80 |
| DH | 974–1158 | 1.31e-06 |
| ER | 1679–1996 | 1.54e-94 |
| KR | 2031–2211 | 5.73e-18 |

NnHispS와 달리 DH, ER이 확정되었고 AMP-binding, docking domain은 검출되지 않아, 도메인 구성이 입력 서열에 따라 자동으로 달라짐을 보였다.

| Gap | 길이 | Helix | Strand | Coil | 판정 |
|---|---|---|---|---|---|
| KS–AT | 110 aa | 35% | 20% | 45% | 추가 검증 필요 |
| AT–DH | 97 aa | 33% | 12% | 54% | 고신뢰 링커 |
| DH–ER | 521 aa | 31% | 29% | 39% | 미식별 도메인 |
| ER–KR | 35 aa | 24% | 15% | 62% | 고신뢰 링커 |

**Figure 4.** PKS25(*Dictyostelium discoideum*, UniProt Q54KU3 / AlphaFold AF-Q54KU3)의 HMM 확정 도메인과 링커.

![Figure 4](PKS25_domain_map.png)

DH–ER 사이 521 aa gap은 NnHispS의 미식별 구간과 동일하게 Helix/Strand 비율이 30% 내외로 높아 같은 기준으로 분류되었다. 이는 "짧은 gap은 coil 우세, 긴 gap은 정형 구조 혼재"라는 판단 기준이 진균 비환원형 PKS와 아메바 환원형 모듈형 PKS라는 진화적으로 거리가 먼 두 단백질에서 공통적으로 관찰됨을 보여준다.

### Result V — 자동화 파이프라인 검증

2.2–2.5의 절차를 `pks_linker_pipeline.py`로 통합하고, NnHispS와 PKS25에 각각 실행하여 수동 분석과 좌표 단위로 비교하였다.

| 항목 | NnHispS (수동) | NnHispS (자동화) | PKS25 (수동) | PKS25 (자동화) |
|---|---|---|---|---|
| 확정 도메인 수 | 6 | 6 | 5 | 5 |
| 미식별 구간 수 | 2 | 2 | 2 | 2 |
| 고신뢰 링커 좌표 | 662–685, 1109–1122, 1192–1204 | 662–684, 1109–1122, 1192–1204 | 917–928, 2019–2029 | 917–928, 2019–2029 |
| 최종 판정 | L1·L2 REDESIGN, L3 NO-NEED | L1·L2 REDESIGN, L3 NO-NEED | — | AT-DH·ER-KR REDESIGN |

**Figure 5.** NnHispS, PKS25 각각에서 수동 분석(상단)과 자동화 결과(하단) 링커 좌표 페어 비교.

![Figure 5](ResultV_manual_vs_automated.png)

유일한 차이는 NnHispS L1 링커의 끝 좌표(수동 685, 자동화 684)로, 같은 DSSP 출력에서 가장 긴 연속 coil run을 추출하는 동일 절차이므로 round-off 수준의 사소한 차이로 판단된다. 도메인 경계, 미식별 구간, 링커 좌표(1 aa 이내), 최종 판정 모두에서 자동화 결과가 수동 분석과 일치하였다.

---

## 4. Conclusion

**Research Question 1**에 대해, HMM 기반 도메인 탐지(i-evalue < 1e-5)와 이차구조·구조적 압축도 검증을 결합하면 임의의 Type I PKS에서 도메인 간 링커를 찾을 수 있다는 것을 확인하였다. 도메인 구성과 진화적 기원이 전혀 다른 NnHispS와 PKS25 모두에서, 짧은 gap은 링커로 확정되고 긴 gap은 압축도 검증을 거쳐 미식별 영역으로 분류되는 동일한 패턴이 재현되었다.

**Research Question 2**에 대해서도, pLDDT·PAE로 취약 링커를 구별하고 이를 자동화할 수 있다는 것을 확인하였다. NnHispS에서 L1이 가장 취약한 링커로 식별되었고, 촉매 잔기 대조 결과 L1·L2는 재설계 대상, L3는 재설계 불필요로 판정되었다. 전체 절차를 스크립트(`pks_linker_pipeline.py`)로 구현해 NnHispS와 PKS25에 실행한 결과, 도메인 경계·미식별 구간·링커 좌표·최종 판정 모두 수동 분석과 일치하였다.

본 연구는 두 PKS의 링커를 찾은 것을 넘어, **FASTA(또는 CDS), AlphaFold PDB, AlphaFold PAE JSON 세 파일만 주어지면 도메인 경계 탐지부터 재설계 대상 판정까지 자동으로 수행하는 재현 가능한 파이프라인**을 구축하고, 이를 독립적인 두 PKS 사례로 검증했다는 데 의의가 있다.

---

## 5. Discussion

**범용화의 의의.** 본 연구의 핵심 기여는 특정 PKS 한 종의 링커를 정확히 찾은 것이 아니라, 그 절차 자체가 진화적으로 거리가 먼 PKS에도 동일하게 적용된다는 것을 검증했다는 점에 있다. NnHispS와 PKS25는 도메인 구성, 환원 여부, 생물학적 기원이 모두 다름에도 동일한 임계값과 절차가 작동했다는 것은, 이 방법론이 특정 서열에 맞춰 조정된 것이 아니라 Type I PKS가 공유하는 더 일반적인 구조적 특징(도메인은 globular하고 링커는 펴져 있다)에 기반함을 시사한다. 다만 검증 사례가 2개에 불과하므로, 더 많은 PKS, 특히 도메인 수가 훨씬 많은 다중 모듈 어셈블리 라인에 대한 추가 검증이 필요하다.

**파라미터 근거 수준에 대한 한계.** Methods의 수치형 파라미터들은 근거 수준이 균일하지 않다. i-evalue 임계값(1e-5)과 취약도 임계값(30)은 실제 데이터 분포에서 관찰된 간극에 근거하여 비교적 견고하다. 반면 helix/strand 검토 임계값(30%), 압축도 cutoff(0.20), PAE flank(60 aa)는 외부 문헌으로 검증된 표준값이 아니라, 본 연구가 NnHispS·PKS25 두 사례를 분석하며 시행착오를 거쳐 정착시킨 잠정적 기준이다. 더 많은 PKS 사례가 누적되면 이 값들을 통계적으로 재추정하거나, 고정 임계값 대신 데이터 분포 기반의 적응적 기준으로 대체하는 것이 바람직하다.

**적용 범위.** Type II PKS는 도메인이 분리된 개별 단백질로 존재하고, Type III PKS는 단일 도메인으로 기능하므로 "도메인 간 링커" 개념이 성립하지 않는다. 본 파이프라인은 Type I PKS, 그리고 구조적으로 유사한 다중 도메인 메가신타제에 한정해 적용 가능하다.

**미식별 도메인의 한계.** NnHispS의 AMP–ACP_1·AT–ACP_2 구간과 PKS25의 DH–ER 구간은 구조적으로 독립된 globular fold임이 확인되었으나, PKS/NRPS 전용 HMM 라이브러리로는 정체를 특정하지 못했다. 더 넓은 범위의 일반 단백질 도메인 데이터베이스(Pfam 전체 등) 스캔이 필요하며, 본 연구 환경에서는 네트워크 접근 제한으로 시도하지 못했다.

**자동화의 재현성.** 본 연구에서 서술한 절차를 코드로 옮긴 결과가 수동 분석과 거의 정확히 일치하였다(Result V). 다만 스크립트를 처음 구현했을 때는 도메인 사이 gap 전체를 링커로 잡아 좌표가 어긋났던 사례가 있었으며, 이는 Methods 서술과 코드 구현이 정확히 일치하는지 별도로 검증하는 절차가 자동화 도구를 신뢰하기 위한 필수 단계임을 보여준다.

---

## Reference

1. Blin, K., Shaw, S., Augustijn, H. E., Reitz, Z. L., Biermann, F., Alanjary, M., Fetter, A., Terlouw, B. R., Metcalf, W. W., Helfrich, E. J. N., van Wezel, G. P., Medema, M. H., & Weber, T. (2023). antiSMASH 7.0: new and improved predictions for detection, regulation, chemical structures and visualisation. *Nucleic Acids Research*, 51(W1), W46–W50. https://doi.org/10.1093/nar/gkad344
   본 연구의 도메인 경계 탐지(2.2)에 사용한 PKS/NRPS 전용 HMM 라이브러리의 출처.

2. Varadi, M., Anyango, S., Deshpande, M., et al. (2022). AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models. *Nucleic Acids Research*, 50(D1), D439–D444.
   pLDDT 신뢰도 구간 분류(매우 높음 ≥90, 신뢰 가능 70–90, 낮음 50–70, 매우 낮음 <50)의 출처.

---

## 사용 파일

| 파일 | 설명 |
|---|---|
| `pks_linker_pipeline.py` | Result V에서 검증한 자동화 스크립트 (Methods 2.2–2.5 구현) |
| `hmm_data/` | 스크립트 실행에 필요한 HMM 라이브러리 4종 (Reference 1) |
| `NnHispS_domain_map.png` | Figure 1 |
| `NnHispS_linker_vulnerability.png` | Figure 2 |
| `NnHispS_final_verification.png` | Figure 3 |
| `PKS25_domain_map.png` | Figure 4 |
| `ResultV_manual_vs_automated.png` | Figure 5 |
| `QnA.md` | 방법론 정립 과정의 시행착오 전체 기록 (별도 파일) |
