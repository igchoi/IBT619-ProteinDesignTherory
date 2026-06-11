# 연구계획서

## *Polyketide Synthase(PKS)* 의 대장균 내 안정적인 발현을 높이기 위한 취약 링커 규명 및 재설계 In silico 파이프라인

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

### 타겟 재설계 단백질: Neonothopanus nambi 유래의 Hispidin synthase(HispS)
*N. nambi*의 HispS(NnHispS)는 **Type I  PKS**로서, 단일 모듈이 카페산(Caffeic acid)에 두 분자의 말로닐-CoA를 순차적으로 축합하여 히스피딘(Hispidin)을 합성한다. 히스피딘은 이후 H3H → Luz → CPH 효소와 연계하여 생물발광 루시페린 3-hydroxyhispidin으로 전환되는 진균 생물발광 경로의 핵심 전구체이다 [2].

NnHispS는 Caffeoyl-CoA와 2분자의 Malonyl-CoA를 기질로 사용하여 강력한 항산화 물질인 히스피딘을 합성하는 약 1,600~1,700개 아미노산 크기(약 180kDa)의 거대한 메가효소이다. npgA는 Hispidin synthase 내부의 핵심 배달원인 ACP 도메인에 꼬리(Phosphopantetheine 암)를 달아주어 효소를 활성화하는 역할을 한다.

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

세 전략을 검토한 결과, **구조 예측과 생성형 AI 기반 링커 재설계**가 이종 발현 문제 해결에 가장 직접적으로 접근하는 전략임을 확인하였다. 그러나 기존 연구들은 각 전략을 개별적으로 적용하는 데 그쳤으며, AlphaFold 기반 취약 링커 규명과 RFdiffusion 기반 링커 재설계를 순차적으로 연결한 사례는 Type I 메가효소에서 드물다.

특히 링커 재설계 시 **촉매 핵심 잔기(KS Cys, AT Ser, ACP Ser)의 보존**이 명시적 설계 제약 조건으로 다루어지지 않는 경우, 효소 활성을 희생하면서 안정성만 향상되는 결과를 낳을 수 있다.

> **Can we identify structurally unstable linkers in NnHispS using AlphaFold predictions and redesign them via RFdiffusion while preserving catalytic residues, to enable functional soluble expression in *E. coli*?**

---

## 4. 단계별 In Silico 파이프라인

```
[입력] NnHispS FASTA 서열
        │
   Phase 1  ColabFold (AlphaFold2 기반)
        │   → 3D 구조 (PDB)
        │   → pLDDT 프로파일 (잔기별 구조 신뢰도)
        │   → PAE 행렬 (도메인 간 상대 위치 오차)
        │   → 취약 링커 후보 구간 특정
        │
   Phase 2  RFdiffusion
        │   → 취약 링커 백본 앙상블 생성
        │   ※ Fixed residues: KS 활성 Cys, AT 활성 Ser, ACP Ppant화 Ser
        │
   Phase 3  ProteinMPNN
        │   → 링커 백본에 대한 서열 역설계
        │   → 촉매 잔기 고정 유지
        │
   Phase 4  ColabFold 재예측 + Aggrescan3D
        │   → 재설계 서열의 구조 신뢰도 재평가
        │   → 응집 경향 잔기 변화 확인
        │
[출력] Δ pLDDT / Δ PAE / Aggrescan3D 핫스팟 변화량
```

---

### Phase 1 — 구조 모델링 및 취약 링커 도출

ColabFold를 이용하여 NnHispS FASTA 서열로부터 3D 구조를 예측한다. 출력된 pLDDT 프로파일과 PAE 행렬을 기반으로 취약 링커 후보를 아래 기준으로 특정한다.

| 지표 | 기준 | 의미 |
|------|------|------|
| pLDDT | < 50 잔기 클러스터 | 구조 신뢰도 낮은 구간 = 취약 링커 1차 후보 |
| PAE | ≥ 15 Å 도메인 간 경계 | 도메인 간 상대 위치 불확실 = 취약 링커 2차 후보 |

두 기준의 교집합 구간을 **최우선 재설계 대상 링커**로 확정하고, 잔기 번호 및 서열 정보를 Phase 2에 전달한다.

---

### Phase 2 — 링커 백본 재설계 (RFdiffusion)

Phase 1에서 특정된 취약 링커 좌표를 RFdiffusion의 마스크 영역(`contigs`)으로 지정하여 새로운 링커 백본 앙상블을 생성한다.

**핵심 설계 제약:**
- **Fixed residues (서열 고정 대상):** KS 활성 Cys, AT 활성 Ser, ACP 인산판테테인화 Ser
- **링커 길이:** 야생형 ± 3잔기 범위 내에서 탐색
- **생성 앙상블 수:** 50~100개 후보 백본

---

### Phase 3 — 서열 역설계 (ProteinMPNN)

RFdiffusion이 생성한 링커 백본에 대해 ProteinMPNN으로 아미노산 서열을 역설계한다. Phase 2의 fixed residues를 동일하게 고정하여 촉매 잔기가 변경되지 않도록 한다.

상위 후보 서열은 아래 기준으로 1차 필터링한다.

- ProteinMPNN confidence score 상위 20%
- 링커 구간 소수성 잔기 비율 감소 여부 (수용성 향상 기대)

---

### Phase 4 — In Silico 검증

최종 후보 서열을 ColabFold에 재입력하여 야생형과 구조 지표를 대비하고, Aggrescan3D(웹 기반)로 응집 경향 잔기 변화를 확인한다.

| 지표 | 의미 | 성공 기준 |
|------|------|------|
| **Δ pLDDT** (링커 잔기) | 구조 신뢰도 향상 | 링커 구간 pLDDT ≥ 70 도달 |
| **Δ PAE** (도메인 간) | 도메인 간 위치 오차 감소 | PAE 감소 및 경계 블록 명확화 |
| **Aggrescan3D 핫스팟 수** | 응집 경향 잔기 감소 | 야생형 대비 핫스팟 감소 |

---

## 5. 연구 수행 타임라인

본 연구는 총 7일간 매일 약 2시간씩 수행하는 일정으로 설계되었다. 각 단계는 배경 학습과 실습을 병행하여 진행한다.

| 일차 | 주요 활동 | 세부 내용 | 산출물 |
|-------|----------|----------|--------|
| **Day 1** | 문헌 학습 및 환경 준비 | PKS 구조·AlphaFold pLDDT/PAE 개념 학습; ColabFold 노트북 접속 및 FASTA 서열 준비 | 배경지식 정리 노트 |
| **Day 2** | Phase 1 실행 | ColabFold로 NnHispS 구조 예측 실행 (대기 중 서론 작성) | PDB 파일, pLDDT/PAE 그래프 |
| **Day 3** | Phase 1 분석 | pLDDT < 50 잔기 클러스터 특정; PAE 행렬 시각화; 취약 링커 후보 구간 확정 | 취약 링커 목록 (잔기 번호) |
| **Day 4** | 환경 구축 및 Phase 2 준비 | 실험실 서버에 RFdiffusion 설치; contigs 파라미터 설정; 촉매 잔기 fixed residues 지정 | RFdiffusion 실행 환경 |
| **Day 5** | Phase 2–3 실행 | RFdiffusion으로 링커 백본 앙상블 생성; ProteinMPNN으로 서열 역설계; 상위 후보 필터링 | 재설계 서열 목록 |
| **Day 6** | Phase 4 검증 | ColabFold 재예측으로 Δ pLDDT / Δ PAE 비교; Aggrescan3D(웹) 응집 핫스팟 분석 | 검증 지표 비교표, 구조 그림 |
| **Day 7** | 보고서 작성 및 마무리 | 결과 정리, 그림 삽입, 결론 및 향후 연구 방향 작성 | 최종 보고서 |

> **비고:** Day 4에서 서버 환경 구축 중 예상치 못한 오류 발생 시, Phase 2–3은 방법론 제안으로 대체하고 ColabFold 분석 결과를 중심으로 보고서를 완성하는 대안 경로를 병행한다.

---

## 6. 출력값 분석 및 후속 연구

Phase 4의 최종 *in silico* 검증 지표를 바탕으로 두 가지 경로로 나누어 후속 연구를 진행한다.

### Case 1: In Silico 검증 통과 (성공적인 설계)

**판단 기준**
- pLDDT: 링커 구간 70점 이상으로 상승
- PAE: 도메인 간 경계면 PAE 감소 및 녹색 블록 형성
- Aggrescan3D: 표면 응집 핫스팟 잔기 수 유의미하게 감소

**후속 액션 플랜 (Wet-lab 진입)**
1. 검증을 통과한 최상위 변이체(Variant)의 아미노산 서열 확정
2. 국내외 유전자 합성 기업에 *E. coli* 맞춤형 CDS 서열 합성(Gene Synthesis) 의뢰
3. 발현 벡터 구축 후 *E. coli* 내 수용성 발현 수율 확인 및 히스피딘(Hispidin) 생산 농도 분석

---

### Case 2: In Silico 검증 실패 (재설계 필요)

**실패 유형 및 원인 분석**

| 유형 | 증상 | 원인 |
|------|------|------|
| **유형 A** | 구조 신뢰도 상승했으나 Aggrescan3D 핫스팟 증가 | 표면 소수성 잔기 노출 |
| **유형 B** | pLDDT 개선 미미, PAE 변화 없음 | 링커 재설계 범위 부족 |

**후속 액션 플랜 (In Silico 피드백 루프)**
1. **유형 A:** ProteinMPNN의 아미노산 편향 파라미터(`--soluble_designs`) 조정 후 서열만 재설계
2. **유형 B:** RFdiffusion `contigs` 길이 확장 또는 마스크 범위 재조정 후 백본부터 재설계
3. 수정된 서열을 Phase 3, 4에 재투입하여 지표 개선 여부 재확인

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
