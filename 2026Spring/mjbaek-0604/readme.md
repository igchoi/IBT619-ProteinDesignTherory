# 연구계획서

## *Neonothopanus nambi* 유래 Hispidin Synthase(NnHispS)의 대장균 내 이종 발현을 위한 최적화 In silico 파이프라인

---

## 1. 연구 배경 및 발현 병목

### PKS란 무엇인가

Polyketide Synthase(PKS)는 아세틸-CoA 및 말로닐-CoA 유도체를 반복적으로 축합하여 다양한 폴리케타이드 골격을 합성하는 거대 효소 복합체(mega-enzyme)이다. 지방산 합성효소(FAS)와 진화적으로 유사하지만, 각 연장 주기마다 케토 환원(KR), 탈수(DH), 에노일 환원(ER) 등의 선택적 수식 반응이 가능하여 항생제(에리스로마이신), 항암제(에포틸론), 면역억제제(라파마이신) 등 의약학적으로 중요한 천연물을 생산한다 [1].

PKS는 구조에 따라 세 가지 유형으로 분류된다.

| 유형 | 구조적 특징 | 대표 산물 |
|------|------------|----------|
| **Type I** | KS·AT·ACP 등 도메인이 하나의 거대 폴리펩타이드에 선형 배열 | 에리스로마이신, 히스피딘 |
| **Type II** | 개별 단일 기능 단백질이 복합체를 이룸 | 테트라사이클린, 독소루비신 |
| **Type III** | 독립적 소형 효소, 주로 식물·세균 | 플라보노이드, 스틸벤 |

### Neonothopanus nambi 유래의 Hispidin synthase(HispS)
*N. nambi*의 HispS(NnHispS)는 **Type I 이터레이티브 PKS**로서, 단일 모듈이 카페산(Caffeic acid)에 두 분자의 말로닐-CoA를 순차적으로 축합하여 히스피딘(Hispidin)을 합성한다. 히스피딘은 이후 H3H → Luz → CPH 효소와 연계하여 생물발광 루시페린 3-hydroxyhispidin으로 전환되는 진균 생물발광 경로의 핵심 전구체이다 [2].

NnHispS는 Caffeoyl-CoA와 2분자의 Malonyl-CoA를 기질로 사용하여 강력한 항산화 물질인 히스피딘을 합성하는 약 1,600~1,700개 아미노산 크기(약 180kda)의 거대한 메가효소이다. npgA는 Hispidin synthase 내부의 핵심 배달원인 ACP 도메인에 꼬리(Phosphopantetheine 암)를 달아주어 효소를 활성화하는 역할을 한다.

<img width="1966" height="982" alt="image" src="https://github.com/user-attachments/assets/8bb08fc8-749b-415c-a041-dfc701edeea6" />
그림 1. AlphaFold Protein Structure Database에서 확인한 NnHispS의 구조

---

### 대장균 이종 발현의 병목

이처럼 복잡한 구조를 가진 NnHispS를 원핵 숙주인 대장균에서 이종 발현하고자 할 때, 아래 네 가지 병목이 복합적으로 작용한다[3].

| 병목 | 원인 | 결과 |
|------|------|------|
| **구조적 불안정성** | 도메인 간 유연한 링커가 수용액 환경에서 고정되지 못함 | Inclusion body / 불용성 침전 |
| **번역 역학 불호환** | 진균–대장균 코돈 사용 빈도(Codon bias) 불일치로 mRNA 번역 속도 불균일 | 공번역 폴딩 실패 / 응집 |
| **PPTase 결핍** | 대장균은 ACP 도메인의 Ppant 부착을 촉매할 적합한 PPTase 미보유 | apo-PKS 유지 / 효소 비활성 |
| **Malonyl-CoA 부족** | 지방산 합성계가 Malonyl-CoA 풀을 경쟁적으로 소모 | 기질 결핍 / 폴리케타이드 미생산 |

이 중 두 가지 병목 사항은 컴퓨테이션을 통한 단백질의 구조의 재설계로 해결할 수 있다고 생각한다.

---

## 2. 기존 컴퓨테이션 전략 검토

### 전략 A — 구조 예측 기반 도메인 경계 및 취약 링커 규명

PKS 엔지니어링의 핵심 난제는 모듈 간 도메인 교환 시 단백질 안정성이 무너진다는 점이다. Englund et al.은 AlphaFold를 도메인 경계 예측에 활용하고, 형광 기반 용해도 바이오센서를 개발하여 무작위 경계 배정 PKS 라이브러리를 *E. coli*에서 고처리량 스크리닝함으로써 야생형 생산 수준을 유지하는 안정 변이체를 동정하였다 [4]. 이 연구는 AlphaFold의 pLDDT / PAE 지표가 PKS 도메인 경계의 구조적 건전성을 사전에 평가하는 데 유효함을 실증하였으며, 실험적 스크리닝 이전에 *in silico*로 취약 링커 구간을 좁혀내는 방법론적 기반을 제공한다.

<img width="900" height="400" alt="image" src="https://github.com/user-attachments/assets/6047200e-a0fc-461c-a6bc-b25cff65bfb2" />
<img width="900" height="600" alt="image" src="https://github.com/user-attachments/assets/93d346cc-bd09-4373-8c9b-4ed255d30b80" />

### 전략 B — 생성형 AI 기반 서열 재설계를 통한 수용성·발현 향상

자연 단백질은 기능에는 최적화되어 있으나 이종 숙주에서 수용성 발현 수율이 낮은 경우가 많다. Sumida et al.은 ProteinMPNN을 진화 정보 및 구조 정보와 결합하여, 활성 부위 잔기를 고정(fixed residues)한 채 비활성 표면 잔기만을 재설계하는 전략으로 향상된 발현량·열안정성·촉매 활성을 갖는 서열을 도출하였다 [5]. 이를 확장한 GRACE 워크플로우는 RFdiffusion으로 링커 백본을 생성하고 ProteinMPNN으로 서열을 역설계한 뒤, 수용성 분석 및 분자동역학 시뮬레이션으로 설계를 검증하는 완결형 자동화 파이프라인을 구현하였다 [6].

### 전략 C — Type I PKS에 직접 적용한 코돈 최적화

단순 고빈도 코돈 치환 방식은 도메인이 순차적으로 접혀야 하는 메가 엔자임에서 역효과를 낼 수 있다. Schmidt et al.은 Type I PKS(LipPKS)를 대상으로 DNA Chisel의 11종 코돈 변이체를 *E. coli*, *C. glutamicum*, *P. putida*에서 체계적으로 비교하였고 [7], 원천 유기체의 코돈 사용 빈도 프로파일을 숙주 tRNA 풀에 조화시키는 **'Harmonize RCA'** 전략이 야생형 대비 최소 50배의 PKS 단백질 수준 증가를 달성함을 보고하였다. 이는 코돈 최적화 전략의 선택이 단순 번역 속도 조절을 넘어 공번역 폴딩 결과를 직접 결정함을 정량적으로 입증한 최초의 Type I PKS 특화 연구이다.

---

## 3. Research Question

세 전략을 검토한 결과, PKS 이종 발현 문제를 해결하기 위한 컴퓨테이션 접근은 구조 예측, 서열 재설계, 코돈 최적화의 세 축으로 발전해왔다. 그러나 기존 연구들은 각 전략을 개별적으로 적용하는 데 그쳤으며, **세 전략을 하나의 통합 파이프라인으로 연결한 사례는 없다.** 나아가 기존 연구들은 대부분 구조적 안정성과 번역 최적화에만 집중하였고, **PPTase 인식 인터페이스 보존**이라는 기능적 활성화 조건을 설계 제약 조건으로 명시적으로 다룬 사례는 전무하다.

대장균은 PKS ACP 도메인을 holo 형태로 전환하는 PPTase를 천연 보유하지 않으므로, 이종 PPTase를 공동 발현하더라도 ACP 표면의 PPTase 인식 잔기가 링커 재설계 과정에서 손상되면 효소는 apo 상태로 남아 촉매 불활성이 된다 [8]. 따라서 본 연구는 **링커 경직화 + 코돈 최적화 + PPTase 인식 인터페이스 보존**을 동시에 만족하는 통합 *in silico* 설계 전략을 제안한다.

> **Can we computationally redesign NnHispS — its unstable linkers, surface residues, and PPTase-recognition interface — to enable functional soluble expression in *E. coli*?**

---

## 4. 단계별 In Silico 파이프라인

```
[입력] NnHispS FASTA
        │
   Phase 1  AlphaFold 3 / ESMFold
        │   → 3D 구조(PDB)
        │   → 취약 링커 위치 (pLDDT < 50, PAE ≥ 15 Å)
        │   → ACP–PPTase 인터페이스 예측 (AlphaFold-Multimer)
        │
   Phase 2  RFdiffusion + ProteinMPNN
        │   → 링커 백본 재설계
        │   → 경직화 아미노산 서열
        │   ※ Fixed residues: 촉매 핵심 잔기 + PPTase 인식 잔기
        │
   Phase 3  DNA Chisel (Harmonize RCA) + Salis RBS Calculator
        │   → 코돈 페이싱 최적화
        │   → E. coli 맞춤 CDS (mRNA 헤어핀 배제)
        │
   Phase 4  AlphaFold 3 재예측 + AlphaFold-Multimer (ACP–PPTase 재검증)
        │
[출력] Δ pLDDT / Δ PAE / Rosetta 에너지 / ACP–PPTase 인터페이스 보존 확인
```

### Phase 1 — 구조 모델링, 취약 링커 도출 및 PPTase 인터페이스 예측

AlphaFold 3 / ESMFold로 NnHispS 3D 구조를 도출하고, 잔기별 pLDDT 및 PAE 행렬로 **취약 링커 구간**을 특정한다. 동시에 AlphaFold-Multimer를 이용하여 ACP 도메인과 PPTase의 복합체 구조를 예측하고, PPTase 인식에 결정적인 **ACP 표면 잔기 목록**을 도출한다 [9].

- pLDDT < 50 잔기 클러스터 → 취약 링커 1차 후보
- PAE ≥ 15 Å 도메인 간 경계 → 취약 링커 2차 후보
- ACP–PPTase 인터페이스 접촉 잔기 → Phase 2 fixed residues 목록 확정

### Phase 2 — 링커 재설계 (PPTase 인터페이스 보존)

Phase 1 취약 링커 좌표를 RFdiffusion에 마스크 영역으로 지정하여 새로운 링커 백본 앙상블을 생성한다. ProteinMPNN 역설계 시 아래 잔기를 fixed residues로 고정한다.

**Fixed residues (서열 고정 대상):**
- 촉매 핵심 잔기: KS 활성 Cys, AT 활성 Ser, ACP 인산판테테인화 Ser
- PPTase 인식 결정 잔기: Phase 1 AlphaFold-Multimer 예측 기반 [8, 9]

이후 CamSol / Aggrescan3D 수용성 스코어로 상위 후보를 필터링한다.

### Phase 3 — 코돈 페이싱 최적화

DNA Chisel 'Harmonize RCA'로 진균 코돈 빈도 프로파일을 대장균 tRNA 풀에 조화시키되, 링커 구간에 희귀 코돈을 집중 배치하여 리보솜의 일시 정지를 유도한다. Salis RBS Calculator로 mRNA 헤어핀 구조를 배제한 최종 CDS를 출력한다.

- 링커 구간 번역 속도: 도메인 내부 대비 30–50% 감속 목표
- CAI > 0.85 (E. coli K12 기준)
- 5'UTR MFE < −5 kcal/mol

### Phase 4 — In Silico 구조 및 기능 검증

최종 최적화 서열을 AlphaFold 3에 재입력하여 야생형 구조와 지표를 대비하고, AlphaFold-Multimer로 최적화된 ACP–PPTase 복합체를 재예측하여 인터페이스 잔기 보존 여부를 확인한다.

| 지표 | 의미 |
|------|------|
| **Δ pLDDT** (링커·계면 잔기) | 구조 신뢰도 향상 |
| **Δ PAE** (도메인 간 경계) | 도메인 간 상호작용 신뢰도 향상 |
| **Rosetta REF2015 에너지** | 전체 에너지 준위 감소 |
| **Aggrescan3D hotspot 수** | 응집 경향 잔기 감소 |
| **ACP–Sfp 인터페이스 PAE** | PPTase 인식 잔기 보존 확인 |

---

## 5. 출력값 분석 및 후속 연구

Phase 4의 최종 인실리코(In silico) 검증 지표를 바탕으로 다음과 같이 두 가지 경로로 나누어 후속 연구를 진행한다.

###  Case 1: 인실리코 검증 통과 (성공적인 설계)
**[판단 기준]**
* **pLDDT / PAE:** 링커 구간 점수 70점 이상으로의 상승 및 도메인 간 경계면 녹색 블록 형성.
* **Rosetta 에너지:** 야생형(WT) 대비 전체 구조 에너지 준위 감소.
* **Aggrescan3D:** 표면 응집 핫스팟 잔기 수가 유의미하게 감소.
* **npgA 인터페이스:** npgA-ACP 복합체 재예측 시 계면 PAE가 낮고 안정적임 (인식 잔기 보존).

**[후속 액션 플랜 (Wet-lab 진입)]**
1. **최적화 서열 확정:** 검증을 통과한 최상위 변이체(Variant)의 아미노산 및 Phase 3 최적화 CDS 염기서열 고정.
2. **유전자 합성 발주:** 국내외 유전자 합성 전문 기업에 대장균(*E. coli*) 맞춤형 CDS 서열 합성(Gene Synthesis) 의뢰.
3. **발현 및 활성 검증:** 발현 벡터 생성 후 *E. coli* 내에서 수용성(Soluble) 발현 수율을 확인하고, npgA 동시 발현을 통해 최종 히스피딘(Hispidin) 생산 농도 분석.

---

###  Case 2: 인실리코 검증 실패 (재설계 필요)
**[판단 기준 및 원인 분석]**
* **유형 A (npgA 인식 불가):** 구조 안정성은 올랐으나, ACP-npgA 인터페이스 PAE가 치솟거나 결합 각도가 뒤틀린 경우 (링커의 과도한 경직화로 인한 구조적 왜곡).
* **유형 B (불용성 응집 위험):** 구조 신뢰도는 올라갔으나, Aggrescan3D 핫스팟이 늘어나고 Rosetta 에너지가 오히려 악화된 경우 (표면 소수성 잔기 노출).

**[후속 액션 플랜 (In silico 피드백 루프)]**
1. **유형 A 해결을 위한 Phase 2 피드백 (RFdiffusion 조건 수정):**
   * RFdiffusion의 `contigs` 서열 길이를 살짝 늘려 유연성을 확보하거나, ACP 표면 잔기 고정(Fixed residues) 영역을 더 넓게 지정하여 npgA 결합 포켓 공간을 강제로 보호한 뒤 뼈대 재설계.
2. **유형 B 해결을 위한 Phase 2 피드백 (ProteinMPNN 조건 수정):**
   * RFdiffusion 백본(뼈대)은 유지하되, ProteinMPNN 구동 스크립트에 아미노산 편향 매개변수(`--soluble_designs`)를 조정하여 표면에 친수성 잔기가 배치되도록 서열만 다시 입히기.
3. **재검증:** 수정된 서열들을 다시 Phase 3, 4 라인에 투입하여 지표의 개선 여부를 재확인.

---

## 참고문헌

[1] Hertweck, C. (2009). The biosynthetic logic of polyketide diversity. *Angewandte Chemie International Edition*, 48(26), 4688–4716.

[2] Kotlobay, A.A., et al. (2018). Genetically encodable bioluminescent system from fungi. *PNAS*, 115(50), 12728–12732.

[3] Walsh, C.T., et al. (1997). Posttranslational modification of polyketide and nonribosomal peptide synthases. *Current Opinion in Chemical Biology*, 1(3), 309–315.

[4] Englund, E., et al. (2023). Biosensor guided polyketide synthases engineering for optimization of domain exchange boundaries. *Nature Communications*, 14, 4871.

[5] Sumida, K.H., et al. (2024). Improving protein expression, stability, and function with ProteinMPNN. *Journal of the American Chemical Society*, 146(3), 1952–1962.

[6] Khowsathit, J., et al. (2024). GRACE: Generative redesign in artificial computational enzymology. *ACS Synthetic Biology*.

[7] Schmidt, M., et al. (2023). Maximizing heterologous expression of engineered type I polyketide synthases: Investigating codon optimization strategies. *ACS Synthetic Biology*, 12(11), 3211–3223.

[8] Kalkreuter, E., et al. (2024). Strategic acyl carrier protein engineering enables functional type II polyketide synthase reconstitution in vitro. *ACS Chemical Biology*, 19(12), 2580–2589.

[9] Hirsch, M., et al. (2024). Mutagenesis supports AlphaFold prediction of how modular polyketide synthase acyl carrier proteins dock with downstream ketosynthases. *Proteins*, 92(12), 1375–1384.
