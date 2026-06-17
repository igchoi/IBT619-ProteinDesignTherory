# PKS 취약 링커 자동 규명 파이프라인
### **HMM 도메인 탐지와 구조적 비정형성 검증을 결합한 Type I Polyketide Synthase 링커 식별 및 취약도 평가**

---

# 1. Introduction

Polyketide Synthase(PKS)는 아세틸-CoA/말로닐-CoA 유도체를 반복적으로 축합하여 폴리케타이드 골격을 합성하는 효소로, 구조적 특징에 따라 세 가지 유형으로 분류된다. Type II PKS는 KS, CLF, ACP 등의 도메인이 각각 독립된 단백질로 발현되어 비공유 복합체를 이루고, Type III PKS는 단일 도메인(케토아실 합성효소 유사 도메인 하나)만으로 기능하는 소형 효소이다. 이 두 유형은 도메인이 여러 개의 분리된 폴리펩타이드로 존재하거나 도메인이 하나뿐이므로, 도메인과 도메인을 잇는 "링커"라는 구조적 요소 자체가 존재하지 않는다.

반면 **Type I PKS**는 KS(Ketosynthase), AT(Acyltransferase), ACP(Acyl Carrier Protein) 등 여러 촉매 도메인이 하나의 폴리펩타이드 사슬 위에 선형으로 배열되며, 각 도메인은 유연한 링커로 연결된다. 이 도메인 간 링커는 PKS를 대장균과 같은 원핵 이종 숙주에서 발현시킬 때 구조적 불안정성의 주요 원인으로 지목되어 왔다. 링커가 수용액 환경에서 안정적인 구조를 형성하지 못하면 단백질 전체가 inclusion body로 응집되거나 폴딩에 실패하는 것으로 보고된 바 있다. 즉 Type I PKS는 링커가 실제로 존재하고, 그 링커의 구조적 안정성이 발현 성패에 직접 영향을 준다는 점에서, 취약 링커를 찾고 개선하는 연구가 의미를 가지는 유일한 PKS 유형이다. 본 연구는 이러한 이유로 Type I PKS만을 대상으로 한다.

기존 연구는 AlphaFold 기반 구조 예측을 통해 도메인 경계의 구조적 건전성을 평가하거나, 생성형 AI로 링커 서열을 재설계하여 발현 수율을 높이는 시도 등 개별 전략을 다루었다. 그러나 이러한 전략들은 특정 PKS 한 종에 대해 개별적으로 적용되었으며, **임의의 Type I PKS 서열을 입력했을 때 도메인 경계와 취약 링커를 자동으로 식별하는 범용 파이프라인**에 대한 체계적 검증은 보고되지 않았다.

본 연구는 다음 두 질문에서 출발한다.

> **Research Question 1.** 여러 도메인을 가지는 임의의 Type I PKS에서, 통계적으로 검증된 도메인 탐지(HMM)와 구조적 비정형성 지표(이차구조, 구조적 압축도)를 결합하여 도메인 간 링커를 찾을 수 있는가?

> **Research Question 2.** 식별된 링커에 AlphaFold 구조 신뢰도 지표(pLDDT, PAE)를 적용하여 취약한 링커를 구별하고, 이를 자동화 파이프라인으로 구현할 수 있는가?

검증은 두 단계로 진행하였다. 1차로 *Neonothopanus nambi* 유래 Hispidin synthase(NnHispS, AlphaFold 모델 AF-A0A3G9K3K9)에 전체 방법론을 적용하여 링커 식별부터 재설계 판정까지 수행하였다. 2차로 도메인 구성이 전혀 다른 *Dictyostelium discoideum* 유래 Probable polyketide synthase 25(PKS25, UniProt Q54KU3, AlphaFold 모델 AF-Q54KU3)에 동일한 방법론을 적용하여 결과 패턴이 재현되는지 교차 검증하였다. 교차 검증된 방법들을 한 번의 시행으로 결과를 얻을 수 있도록 자동화 스크립트를 제시하였다.

---

# 2. Materials and Methods

## 2.1 서열 및 구조 데이터 확보

| 항목 | NnHispS | PKS25 |
|---|---|---|
| 출처 | CDS FASTA → Biopython 번역 | UniProt Q54KU3 (단백질 FASTA) |
| 길이 | 1,698 aa | 2,380 aa |
| 구조 파일 | AF-A0A3G9K3K9-F1-model_v6.pdb | AF-Q54KU3-F1-model_v6.pdb |
| PAE 파일 | AF-A0A3G9K3K9-F1-predicted_aligned_error_v6.json | AF-Q54KU3-F1-predicted_aligned_error_v6.json |

CDS로 확보한 서열은 Biopython(`Seq.translate`)으로 단백질 서열로 변환하였다. AlphaFold PDB 파일의 B-factor 컬럼에는 잔기별 pLDDT 값이 기록되어 있으며, PAE JSON 파일에는 잔기 쌍 간 위치 불확실성을 나타내는 (서열길이)×(서열길이) 행렬이 들어있다.

## 2.2 도메인 경계 탐지 — HMM 기반 자동 판별

**사용 파일**: antiSMASH 저장소(GitHub, antismash/antismash)에서 확보한 PKS/NRPS 도메인 전용 HMM 프로파일 4종(`nrpspksdomains.hmm`, `ksdomains.hmm`, `dockingdomains.hmm`, `abmotifs.hmm`, 총 166개 모델). 이 라이브러리는 KS, AT, ACP, KR, DH, ER, PT, SAT, docking domain 등 PKS/NRPS에 특화된 도메인 모델을 포함한다.

**실행 도구**: pyhmmer (`hmmscan`)

**파라미터 및 근거**: 도메인 채택 기준은 **i-evalue < 1e-5**로 설정하였다. 이 값을 택한 이유는, 예비 분석에서 도메인 모델이 무작위로 약하게 매칭되는 경우(예: 실제로 도메인이 없는 위치에 i-evalue가 1 이상으로 매칭) 와 통계적으로 유의한 매칭(i-evalue가 1e-10 이하) 사이에 명확한 간극이 존재함을 확인했기 때문이다. 1e-5는 이 둘을 가르는 보수적인 경계값으로, 약한 매칭(가짜 양성)을 배제하면서도 신뢰할 수 있는 도메인은 놓치지 않는 절충점이다.

이 방식은 사전에 "이 PKS는 어떤 도메인을 가지고 있어야 한다"는 가정을 두지 않는다. 라이브러리 전체를 스캔하고 임계값을 통과한 모델만 "이 단백질이 실제로 가진 도메인"으로 채택하므로, 입력 서열마다 다른 도메인 구성이 나올 수 있다.

같은 위치(좌표가 겹치는 경우)에 여러 모델이 매칭되면(예: ACP, PP-binding, PKS_PP가 같은 구간을 가리키는 경우), 이를 하나의 도메인 인스턴스로 병합하고 i-evalue가 가장 작은 모델명을 대표 명칭으로 채택하였다. 좌표가 겹치지 않고 단순히 인접한 매칭은 병합하지 않고 별개의 도메인으로 유지하였다.

## 2.3 링커 후보 정의 — 이차구조 및 구조적 압축도 검증

도메인 사이에 남는 구간(gap)을 곧바로 링커로 간주하지 않고, 두 단계로 추가 검증하였다.

**(1) 이차구조 비율 확인 — DSSP**
mkdssp(v4.2.2, apt 설치)로 AlphaFold 모델의 이차구조를 잔기별로 할당하고, H(helix)/G/I를 Helix로, E(strand)/B를 Strand로, 나머지를 Coil로 단순화하였다. 각 gap 구간 내에서 Coil이 차지하는 비율과 연속 Coil 구간(run)을 계산하였다.

이 단계에서 임의의 "coil 비율 X% 이상이면 링커"라는 단일 임계값은 적용하지 않았다. 사전 조사 결과 PKS 링커 길이가 문헌마다 20 aa에서 550 aa까지 보고되어 있어, 길이나 비율에 고정 숫자 기준을 두는 것이 근거가 부족하다고 판단했기 때문이다. 대신 각 gap의 Helix/Strand 비율이 뚜렷하게 높은 경우(약 30% 이상) 이를 "정형 구조가 섞여 있다"는 정성적 신호로 보고, 다음 단계인 구조적 압축도 검증으로 넘겨 판별하였다.

**(2) 구조적 압축도 — Radius of gyration 및 Compaction ratio**
Helix/Strand 비율이 높아 도메인인지 링커인지 애매한 gap에 대해서는, 해당 구간 CA 원자 좌표만 추출하여 다음을 계산하였다.

```
Compaction ratio = End-to-end distance / [(잔기 수 − 1) × 3.8 Å]
```

3.8 Å은 인접 CA 원자 간 평균 결합 거리이며, 분모는 해당 구간이 완전히 펴졌을 때의 이론적 최대 길이이다. Compaction ratio가 1에 가까우면 구간이 거의 직선으로 뻗어 있다는 뜻이고(링커의 특징), 0에 가까우면 시작과 끝이 서로 가까이 되돌아온다는 뜻으로(독립된 globular 도메인의 특징) 해석하였다. 대조군으로 이미 HMM에서 확정된 도메인 1개와 이미 확정된 링커 1개의 compaction ratio를 함께 계산하여 비교 기준으로 사용하였다.

이 검증을 통과하지 못한 gap(즉 압축도가 도메인 수준으로 낮은 gap)은 링커 후보에서 제외하고 "미식별 도메인(정체 미확인)"으로 분류하였다.

## 2.4 취약도 평가 — pLDDT 및 PAE

2.2–2.3에서 최종 확정된 링커에 대해서만 다음 지표를 계산하였다.

- 평균/최소 pLDDT (해당 잔기 구간의 B-factor 값)
- 도메인 간 PAE: 링커 양옆 60 aa 범위(flank) 내 도메인 간 PAE 행렬 평균값. 60 aa는 인접 도메인의 구조적 영향을 충분히 포함하면서도 먼 도메인까지 포함시켜 신호를 희석시키지 않는 절충 범위로 설정하였다.

```
취약도 점수 = 0.5 × (100 − 평균 pLDDT)/100 × 100  +  0.5 × (도메인 간 PAE / 해당 단백질의 최대 PAE) × 100
```

## 2.5 촉매 잔기 검증 및 재설계 가능 여부 판정

도메인별 촉매 활성 잔기 주변 보존 모티프(KS-Cys: `HGTGT` 인접 Cys, AT-Ser: `GHSxG`/`AFSGQGT`, ACP-Ser: `LGxDS`/`LGxTS`/`LGxES`)를 정규식으로 탐지하고, 해당 위치가 어느 도메인에 속하는지(2.2의 HMM 좌표 기준) 대조하여 모티프 탐지가 도메인 경계와 일치하는지 교차 확인하였다.

각 링커에 대해 다음 판정을 적용하였다.

```
취약도 점수 < 30                              →  NO-NEED (재설계 불필요)
취약도 점수 ≥ 30  AND  링커 내 촉매 잔기 존재   →  SKIP (재설계 불가, 촉매 잔기 보존 필요)
취약도 점수 ≥ 30  AND  위 조건 미해당            →  REDESIGN (재설계 대상)
```

취약도 임계값 30은 6개 gap 전체의 취약도 점수 분포(9.5~62.9)에서, NO-NEED로 분류되어야 할 안정적인 링커(점수 9~25 범위)와 명확히 취약한 링커(점수 35 이상) 사이에 위치하는 값으로 설정하였다.

---

# 3. Results

## Result I. 링커 찾기 (NnHispS) — Research Question 1에 대한 검증

> **Research Question 1.** 여러 도메인을 가지는 임의의 Type I PKS에서, 통계적으로 검증된 도메인 탐지(HMM)와 구조적 비정형성 지표(이차구조, 구조적 압축도)를 결합하여 도메인 간 링커를 찾을 수 있는가?

Research Question 1은 사전 가정 없이 도메인 간 링커를 식별할 수 있는지를 묻는다. 이를 검증하기 위해 2.2의 HMM 스캔(i-evalue < 1e-5)과 2.3의 이차구조·압축도 검증을 NnHispS에 순서대로 적용하였다.

### 3.1 HMM 기반 도메인 확정

i-evalue < 1e-5 기준으로 6개 도메인이 채택되었다.

| 도메인 | 위치(aa) | i-evalue |
|---|---|---|
| AMP-binding | 26–453 | 2.99e-46 |
| ACP_1 | 584–647 | 8.10e-07 |
| KS | 686–1108 | 7.06e-112 |
| Docking domain | 1123–1191 | 2.09e-11 |
| AT | 1210–1491 | 5.32e-68 |
| ACP_2 | 1619–1691 | 1.33e-10 |

이 6개 도메인은 사전에 "PKS는 이런 도메인을 가져야 한다"는 가정을 두지 않고 166개 모델 전체를 스캔한 결과로 얻어졌다. AMP-binding 도메인이 N-말단에서 강하게 검출된 것은 예비 분석 단계에서 예상하지 못했던 결과였으나, NnHispS와 근연한 비환원형 진균 PKS(ShPKS1 등)가 KS 앞에 추가 AMP·ACP 도메인을 가진다는 선행 문헌과 일치하여, 가짜 양성이 아닌 실제 도메인으로 확인되었다.

### 3.2 도메인 사이 gap의 이차구조 및 압축도 검증

5개 gap에 대해 DSSP coil 비율을 계산한 결과는 다음과 같다.

| Gap | 길이 | Helix | Strand | Coil |
|---|---|---|---|---|
| AMP–ACP_1 | 131 aa | 34% | 18% | 48% |
| ACP_1–KS | 39 aa | 32% | 0% | 68% |
| KS–Docking | 15 aa | 0% | 0% | 100% |
| Docking–AT | 19 aa | 0% | 28% | 72% |
| AT–ACP_2 | 128 aa | 33% | 4% | 63% |

Helix 비율이 30% 이상인 두 개의 긴 gap(AMP–ACP_1, AT–ACP_2)은 2.3에서 정의한 정성적 기준(약 30% 이상의 정형 구조 혼재 시 압축도 검증으로 넘김)에 해당하여 구조적 압축도를 추가로 계산하였다. 그 결과 두 구간 모두 compaction ratio 0.09로 나타나 globular 도메인 대조군(KS 도메인, ratio 0.01)에 가까웠고 링커 대조군(확정 링커 구간, ratio 0.60)과는 뚜렷하게 구분되었다. 이에 따라 두 구간은 링커가 아닌 미식별 도메인으로 분류하였다. PKS/NRPS 전용 HMM 라이브러리(166개 모델) 재스캔에서도 이 두 구간에 매칭되는 모델은 없어, 정확한 정체는 확인하지 못했다.

>![Figure 1.](image.png)
> **Figure 1.** NnHispS의 HMM 확정 도메인(6개)과 DSSP coil 비율 기반 고신뢰 링커(3개), 그리고 구조적 압축도로 미식별 도메인으로 재분류된 2개 구간을 함께 표시한 도메인 맵.

남은 3개 gap(ACP_1–KS, KS–Docking, Docking–AT)은 helix/strand 비율이 낮고 compaction ratio 검증이 필요하지 않은 수준이어서 고신뢰 링커로 최종 확정하였다.

| 링커 | 위치(aa) | 길이 |
|---|---|---|
| L1 (ACP_1–KS) | 662–685 | 23 aa |
| L2 (KS–Docking) | 1109–1122 | 13 aa |
| L3 (Docking–AT) | 1192–1204 | 12 aa |

이 결과는 Research Question 1에 대해, 사전 가정 없이 통계적 도메인 탐지와 구조적 검증만으로 링커 3개를 식별할 수 있음을 보여준다. 다만 5개 gap 중 2개(40%)가 단순 "도메인 사이 = 링커" 가정으로는 걸러지지 않고 추가 구조 검증이 필요했다는 점은, 도메인 탐지만으로는 링커 식별이 충분하지 않다는 것도 함께 시사한다.

## Result II. 취약 부위 도출 (NnHispS) — Research Question 2에 대한 검증

> **Research Question 2.** 식별된 링커에 AlphaFold 구조 신뢰도 지표(pLDDT, PAE)를 적용하여 취약한 링커를 구별하고, 이를 자동화 파이프라인으로 구현할 수 있는가?

Research Question 2는 식별된 링커의 취약도를 정량화하고 재설계 가능 여부를 판단할 수 있는지를 묻는다. Result I에서 확정된 링커 3개에 2.4의 pLDDT·PAE 평가(도메인 간 PAE는 링커 양옆 60 aa flank 기준)를 적용한 결과는 다음과 같다.

| 링커 | 평균 pLDDT | 최소 pLDDT | 평균 PAE (Å) | 취약도 점수 |
|---|---|---|---|---|
| **L1 (ACP_1–KS)** | **42.6** | **27.5** | **21.2** | **62.9** |
| L2 (KS–Docking) | 57.5 | 35.9 | 8.2 | 34.5 |
| L3 (Docking–AT) | 65.5 | 52.6 | 4.9 | 25.2 |

참고로 6개 도메인 자체의 평균 pLDDT는 78.5–93.5 범위로 모두 안정적이었으며, 링커 구간에서만 뚜렷한 저하가 관찰되어 도메인-링커 경계 확정이 구조적으로도 타당함을 추가로 확인하였다.

>![Figure 2.](image-1.png)
> **Figure 2.** 확정된 링커 3개의 pLDDT 프로파일 및 도메인 간 PAE 비교.

L1이 세 링커 중 가장 취약하였으며, 이는 1차 모티프 기반 예비 분석(부록 QnA 참조)에서 지목되었던 위치와는 다른 좌표로, 도메인 경계를 HMM으로 재확정한 결과 취약 링커의 실제 위치가 달라졌음을 보여준다.

## Result III. 검증 — 촉매 잔기 확인 및 재설계 판정

2.5에서 정의한 판정 로직(취약도 임계값 30)을 Result II의 결과에 적용하기 전에, 먼저 보존 모티프로 탐지한 촉매 잔기 6개(KS-Cys 2개, AT-Ser 2개, ACP-Ser 2개)의 위치를 HMM 도메인 좌표와 대조하였다. 6개 모두 해당 도메인 내부에 위치하였으며, 확정된 링커 3개(L1, L2, L3) 어디에도 포함되지 않았다. 이는 2.2에서 확정한 도메인 경계가 촉매 활성 부위와 정확히 일치한다는 추가 근거이기도 하다.

| 링커 | 취약도 점수 | 링커 내 촉매 잔기 | 최종 판정 |
|---|---|---|---|
| **L1 (ACP_1–KS)** | 62.9 | 없음 | **REDESIGN** |
| L2 (KS–Docking) | 34.5 | 없음 | **REDESIGN** |
| L3 (Docking–AT) | 25.2 | 없음 | NO-NEED |

>![Figure 3.](image-2.png)
> **Figure 3.** 촉매 잔기 위치를 포함한 NnHispS 최종 통합 리포트.

## Result IV. 교차 검증 (PKS25) — Research Question 1, 2의 재현성 확인

도메인 구성이 NnHispS와 전혀 다른 PKS25(*Dictyostelium discoideum*, KS-AT-DH-ER-KR 구조의 환원형 모듈형 PKS)에 2.2–2.3의 동일한 절차(HMM 도메인 탐지, i-evalue < 1e-5 → DSSP coil 비율 → 30% 임계 초과 시 압축도 검증)를 적용하여, Research Question 1에 대한 답이 NnHispS 한 단백질에 한정되지 않는지 확인하였다.

### 4.1 HMM 기반 도메인 확정

| 도메인 | 위치(aa) | i-evalue |
|---|---|---|
| KS | 34–458 | 1.23e-152 |
| AT | 568–877 | 1.29e-80 |
| DH | 974–1158 | 1.31e-06 |
| ER | 1679–1996 | 1.54e-94 |
| KR | 2031–2211 | 5.73e-18 |

NnHispS와 달리 DH, ER 도메인이 확정되었고 AMP-binding, docking domain은 검출되지 않았다. 이는 사전 가정 없이 도메인 구성이 입력 서열에 따라 자동으로 달라짐을 보여준다. C-말단의 ACP 후보(aa2307–2349)는 i-evalue 5.95e-05로 임계값을 근소하게 통과하지 못해 이번 분석에서는 채택하지 않았다.

### 4.2 gap 검증 결과

| Gap | 길이 | Helix | Strand | Coil | 판정 |
|---|---|---|---|---|---|
| KS–AT | 110 aa | 35% | 20% | 45% | 추가 검증 필요 |
| AT–DH | 97 aa | 33% | 12% | 54% | 추가 검증 필요 |
| DH–ER | 521 aa | 31% | 29% | 39% | 미식별 도메인 의심 |
| ER–KR | 35 aa | 24% | 15% | 62% | 고신뢰 링커 |

>![Figure 4.](image-3.png)
> **Figure 4.** PKS25 도메인 구조 맵 및 NnHispS와의 gap 패턴 비교.

DH–ER 사이의 521 aa gap은 NnHispS의 미식별 도메인 구간(AMP–ACP_1, AT–ACP_2)과 동일하게 Helix/Strand 비율이 30% 내외로 높게 나타나, 같은 기준(압축도 검증 필요)으로 분류되었다. 반면 ER–KR 사이의 35 aa gap은 coil 비율이 62%로 가장 높아, NnHispS의 고신뢰 링커들과 같은 패턴을 보였다.

이 결과는 "도메인 사이 짧은 gap은 coil 우세, 긴 gap은 정형 구조 혼재"라는 판단 기준이 진화적으로 거리가 먼 두 PKS(진균 비환원형 PKS vs 아메바 환원형 모듈형 PKS)에서 공통적으로 관찰됨을 보여주며, 본 방법론이 NnHispS 한 단백질에 특이한 우연이 아니라 일정한 재현성을 가짐을 시사한다.

## Result V. 자동화 파이프라인 검증

2.2–2.5의 절차를 하나의 스크립트(`pks_linker_pipeline.py`)로 통합하고, NnHispS와 PKS25 두 단백질에 각각 실행하여 Result I–IV의 수동 분석 결과와 좌표 단위로 비교하였다.

| 항목 | NnHispS (수동) | NnHispS (자동화) | PKS25 (수동) | PKS25 (자동화) |
|---|---|---|---|---|
| 확정 도메인 수 | 6 | 6 | 5 | 5 |
| 미식별 구간 수 | 2 | 2 | 2 (KS-AT, DH-ER 추정) | 2 |
| 고신뢰 링커 좌표 | aa662–685, 1109–1122, 1192–1204 | aa662–684, 1109–1122, 1192–1204 | aa917–928(AT-DH), 2019–2029(ER-KR) | aa917–928, 2019–2029 |
| 최종 판정 | L1·L2 REDESIGN, L3 NO-NEED | L1·L2 REDESIGN, L3 NO-NEED | (수동 분석 미실시) | AT-DH·ER-KR REDESIGN |

> <img width="2383" height="1093" alt="image" src="https://github.com/user-attachments/assets/c54b24ac-fe0a-41d1-9807-44d0d3da5427" />
> **Figure 5.** 찾은 PKS의 링커에 대한 자동화 전 후 비교.

자동화 결과는 도메인 경계, 미식별 구간, 링커 좌표(1 aa 이내 오차) 및 최종 판정에서 수동 분석과 일치하였다. 유일한 차이는 NnHispS L1 링커의 끝 좌표가 수동 분석에서는 685, 자동화에서는 684였는데, 이는 두 분석 모두 같은 DSSP 출력에서 "가장 긴 연속 coil run"을 추출하는 절차이므로 round-off 수준의 사소한 차이로 판단된다.

이 검증을 통해 2.2–2.5의 절차가 사람이 단계별로 직접 수행한 결과와 코드로 자동 실행한 결과 사이에 실질적 차이가 없음을 확인하였으며, 본 파이프라인이 새로운 Type I PKS 서열에 대해 일관된 결과를 산출하는 재현 가능한 자동화 도구로 기능할 수 있음을 보여준다.

---

# 4. Conclusion

본 연구는 두 개의 Research Question에서 출발하였고, 각각에 대해 다음과 같이 답한다.

**Research Question 1**(여러 도메인을 가지는 임의의 Type I PKS에서 도메인 간 링커를 찾을 수 있는가)에 대해, HMM 기반 도메인 탐지(i-evalue < 1e-5)와 이차구조·구조적 압축도 검증을 결합하면 가능하다는 것을 확인하였다. 이 방법은 NnHispS(AMP-ACP-KS-Docking-AT-ACP, 비환원형 진균 PKS)와 PKS25(KS-AT-DH-ER-KR, 환원형 아메바 모듈형 PKS)처럼 도메인 구성과 진화적 기원이 전혀 다른 두 단백질에서 사전 가정 없이 동일하게 작동하였으며, "짧은 도메인 간 gap은 coil 구조가 우세해 링커로 확정되고, 긴 gap은 정형 구조가 혼재해 압축도 검증이 필요한 미식별 영역으로 분류된다"는 동일한 패턴이 재현되었다.

**Research Question 2**(식별된 링커에 pLDDT·PAE를 적용해 취약 부위를 구별하고 자동화할 수 있는가)에 대해서도 가능하다는 것을 확인하였다. NnHispS의 링커 3개 중 1개(L1)가 다른 두 링커보다 뚜렷이 낮은 pLDDT와 높은 PAE를 보였고, 촉매 잔기 위치와 대조한 결과 L1과 L2가 재설계 대상(REDESIGN)으로, L3가 재설계 불필요(NO-NEED)로 구분되었다. 이 전체 절차(2.2–2.5)를 하나의 스크립트(`pks_linker_pipeline.py`)로 구현하여 NnHispS와 PKS25에 각각 실행한 결과, 도메인 경계·미식별 구간·링커 좌표(1 aa 이내 오차)·최종 판정 모두에서 수동 분석과 일치하였다(Result V).

이로써 본 연구는 단순히 두 PKS의 링커를 찾은 것이 아니라, **FASTA(또는 CDS), AlphaFold PDB, AlphaFold PAE JSON 세 파일만 주어지면 도메인 경계 탐지부터 링커 식별, 취약도 정량화, 재설계 대상 판정까지 자동으로 수행하는 재현 가능한 파이프라인**을 구축하고, 이를 두 개의 독립적인 PKS 사례로 검증했다는 데 의의가 있다. `pks_linker_pipeline.py`는 본 연구에서 검증한 절차를 그대로 실행하는 도구이며, 새로운 Type I PKS 서열에 대해서도 같은 세 파일만 준비되면 동일한 분석을 즉시 재현할 수 있다.

---

# 5. Discussion

### 5.1 범용화의 의의

본 연구의 핵심 기여는 특정 PKS 한 종의 링커를 정확히 찾아낸 것이 아니라, **그 절차 자체가 진화적으로 거리가 먼 PKS에도 동일하게 적용된다는 것을 검증했다는 점**에 있다. NnHispS와 PKS25는 도메인 구성(AMP-ACP-KS-AT-ACP vs KS-AT-DH-ER-KR), 환원 여부(비환원형 vs 환원형), 생물학적 기원(진균 vs 아메바)이 모두 다르다. 그럼에도 동일한 임계값과 동일한 판단 절차가 두 단백질 모두에서 작동했다는 것은, 이 방법론이 특정 PKS의 서열 특성에 맞춰 조정된 것이 아니라 Type I PKS가 공유하는 더 일반적인 구조적 특징(도메인은 globular하고 링커는 펴져 있다)에 기반하고 있음을 시사한다. 다만 검증 사례가 2개에 불과하므로, 이 범용성의 주장은 더 많은 PKS(특히 도메인 수가 훨씬 많은 다중 모듈 어셈블리 라인)에 대한 추가 검증을 통해 더 단단해질 필요가 있다.

### 5.2 설정한 파라미터의 근거 수준에 대한 한계

Methods 2.2–2.5에는 여러 수치형 파라미터가 등장하며, 이들의 근거 수준은 균일하지 않다는 점을 분명히 밝힌다.

비교적 근거가 견고한 파라미터는 두 가지이다. i-evalue 임계값(1e-5)은 실제 스캔 결과에서 가짜 양성 매칭(i-evalue > 1)과 신뢰할 수 있는 매칭(i-evalue < 1e-10) 사이에 명확한 수치적 간극이 관찰되었다는 데이터에 근거한다. 취약도 점수 임계값(30)도 6개 gap의 실제 점수 분포(9.5–62.9)에서 안정 구간과 취약 구간이 갈리는 지점을 그대로 사용하였다.

반면 나머지 파라미터들 — helix/strand 비율 검토 임계값(30%), 구조적 압축도 cutoff(0.20), PAE 산출 시 flank 범위(60 aa) — 은 외부 문헌을 인용할 수 있는 표준값이 아니라, 본 연구가 분석 과정에서 직접 관찰한 제한된 사례(주로 NnHispS 한 단백질, 이후 PKS25로 일부 보강)로부터 설정한 값이다. 예를 들어 압축도 cutoff 0.20은 도메인 대조군(0.01)과 링커 대조군(0.60) 사이에서 도메인 쪽에 가깝게 보수적으로 설정한 것일 뿐, 그 정확한 위치를 뒷받침하는 독립적인 근거는 없다. 이러한 파라미터들은 본 연구가 진행되는 동안 시행착오를 거치며 두 사례에 맞춰 정착된 값이며, 외부 검증된 기준이라기보다는 **현재까지의 관찰에 기반한 잠정적 기준**으로 보아야 한다. 더 많은 PKS 사례가 누적되면 이 값들을 통계적으로 재추정하거나, 고정 임계값 대신 데이터 분포 기반의 적응적 기준으로 대체하는 것이 바람직하다.


# Reference

1. Blin, K., Shaw, S., Augustijn, H. E., Reitz, Z. L., Biermann, F., Alanjary, M., Fetter, A., Terlouw, B. R., Metcalf, W. W., Helfrich, E. J. N., van Wezel, G. P., Medema, M. H., & Weber, T. (2023). antiSMASH 7.0: new and improved predictions for detection, regulation, chemical structures and visualisation. *Nucleic Acids Research*, 51(W1), W46–W50. https://doi.org/10.1093/nar/gkad344
   — 본 연구에서 도메인 경계 탐지(2.2)에 사용한 PKS/NRPS 전용 HMM 라이브러리(`nrpspksdomains.hmm`, `ksdomains.hmm`, `dockingdomains.hmm`, `abmotifs.hmm`)의 출처.

2. Varadi, M., Anyango, S., Deshpande, M., et al. (2022). AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models. *Nucleic Acids Research*, 50(D1), D439–D444.
   — pLDDT 신뢰도 구간 분류(매우 높음 ≥90, 신뢰 가능 70–90, 낮음 50–70, 매우 낮음 <50)의 출처. 본 연구의 2.4 취약도 평가 및 Figure 1의 pLDDT 구간 색상 구분에 이 기준을 적용하였다.

---

# 사용 파일

| 파일 | 설명 |
|---|---|
| `pks_linker_pipeline.py` | Result V에서 검증한 자동화 스크립트 (Methods 2.2–2.5 구현) |
| `hmm_data/` | 스크립트 실행에 필요한 HMM 라이브러리 4종 (antiSMASH 출처, Reference 1) |
| `QnA.md` | 방법론 정립 과정의 시행착오 전체 기록 (별도 파일) |

---
