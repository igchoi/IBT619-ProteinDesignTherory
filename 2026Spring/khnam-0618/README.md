# Alpha-helical 항균 펩타이드 후보 설계 및 1차 평가

**KI HYUN NAM**

**Date: 2026-06-18**

**Course: IBT619-Protein Design Theory**

---

## 초록

항균 펩타이드와 유사한 방식으로 작용할 가능성이 있는 짧은 alpha-helical peptide 후보를 설계하고, 서열 특성 분석과 ColabFold 기반 구조 예측을 통해 1차 평가를 수행하였다. 총 5개의 후보 서열을 만들고, 각 후보의 순전하, 소수성 비율, helix 형성 가능성, hydrophobic moment 등을 비교하였다. 이후 ColabFold로 예측 구조를 확인하고, pLDDT와 주요 구조 지표를 바탕으로 후보 간 차이를 검토하였다. 최종 후보로 선정한 Design B에 대해서는 helical wheel plot, residue별 pLDDT 분석, 표면 residue 특성 시각화, 추가 ColabFold 재예측을 진행하였다. 종합적으로 Design B는 전하, 소수성, 양친매성, 구조 예측 신뢰도 측면에서 가장 무리가 적은 후보로 확인되었다.

## 1. 배경

항균 펩타이드는 대체로 길이가 짧고, 양전하를 띠는 경우가 많다. 미생물 세포막에는 음전하를 띠는 성분이 많이 포함되어 있기 때문에, 양전하성 펩타이드는 막 표면과 상호작용하기에 유리하다. 또한 여러 항균 펩타이드는 alpha-helix 구조를 형성하며, helix의 한쪽 면에는 소수성 residue가, 다른 면에는 친수성 또는 양전하성 residue가 배치되는 양친매성 구조를 보인다.

최종 목적은 실제 항균 활성을 바로 입증하는 것이 아니라, 항균 펩타이드 후보로 발전시킬 수 있는 서열을 계산적으로 설계 및 평가하여 우선순위를 정하는 것이다. 따라서 설계에서는 짧은 길이, 적절한 양전하, 과도하지 않은 소수성, alpha-helix 형성 가능성을 함께 고려하였다.

## 2. 설계 기준

**후보 서열을 만들 때 적용한 기준**

| 항목 | 기준 |
|:---:|:---:|
| 길이 | 약 35-60 amino acids |
| 구조 | 주로 alpha-helix |
| 기능적 방향 | 항균 펩타이드 유사 막 상호작용 후보 |
| 순전하 | 약 +3에서 +8 |
| 소수성 비율 | 약 35-50% |
| 중요한 특징 | 양친매성 alpha-helix |
| 주로 사용한 잔기 | Ala, Leu, Lys, Glu, Gln, Ser |
| 피하려고 한 특징 | Pro/Gly 과다, 긴 소수성 반복 구간 |

**Lys**는 양전하를 부여하기 위해 사용하였고, **Leu**와 **Ala**는 helix 형성과 소수성 면 형성에 기여하도록 배치하였다. **Glu**, **Gln**, **Ser**는 서열이 지나치게 소수성으로 치우치지 않도록 조절하는 역할로 포함하였다.

## 3. 후보 서열 설계

설계 기준에 따라 다섯 개의 후보 서열을 설계하였다.

| 후보 | 서열 | 설계 의도 |
|:---:|:---:|:---:|
| Design A | `KLAEQLKQSLKELAKQSLKELAKQSLKELAKQKQS` | 기본적인 단일 alpha-helix 후보 |
| Design B | `KLAKQLSEKLKQALSKQLAELKQALSKQLAELKKQS` | 전하와 소수성의 균형을 맞춘 amphipathic helix 후보 |
| Design C | `EALKQLLKAQSKSGKLAEQLLKQALSKQLAEKQSQ` | 짧은 turn을 넣은 helix-turn-helix 유사 후보 |
| Design D | `KRLQALSKQLKELAKQSLKQLAKESLKQLAKKQSQ` | 양전하를 더 강하게 준 후보 |
| Design E | `EALKQLLKQALSKSGEALKQLLKQALSKQLAEKKQS` | 두 개의 helix가 연결된 형태를 의도한 후보 |

Design B는 초기 설계 단계부터 전하와 소수성의 균형을 중점적으로 고려한 후보이다. Design D처럼 양전하가 지나치게 강하지 않으면서도, Design A보다 소수성 비율과 hydrophobic moment가 더 적절하게 나오도록 서열을 조정하였다.

## 4. 서열 기반 평가

먼저 서열 자체에서 계산할 수 있는 기본 지표를 비교하였다. 평가 항목은 길이, 순전하, 소수성 비율, GRAVY score, helix propensity, hydrophobic moment, 가장 긴 소수성 연속 구간, Pro/Gly 비율이었다.

| 후보 | 길이 | 순전하 | 소수성 비율 | GRAVY | Helix propensity | Hydrophobic moment | 최장 소수성 구간 | Pro/Gly 비율 | 점수 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Design A | 35 | +5 | 0.34 | -1.02 | 1.21 | 0.83 | 2 | 0.00 | 5/6 |
| Design B | 36 | +6 | 0.39 | -0.74 | 1.21 | 1.16 | 2 | 0.00 | 6/6 |
| Design C | 35 | +4 | 0.37 | -0.76 | 1.20 | 0.83 | 2 | 0.03 | 6/6 |
| Design D | 35 | +8 | 0.34 | -1.05 | 1.18 | 0.83 | 2 | 0.00 | 5/6 |
| Design E | 36 | +5 | 0.39 | -0.64 | 1.20 | 0.86 | 2 | 0.03 | 6/6 |

서열 지표만 놓고 보면 Design B가 가장 적합한 후보로 보였다. 총점이 6/6이었고, hydrophobic moment도 후보 중 가장 높았다. 이는 Design B가 alpha-helix를 형성할 경우, 소수성 residue가 helix의 한쪽 면에 비교적 잘 모일 가능성이 있음을 의미한다.

<img width="1166" height="642" alt="image" src="https://github.com/user-attachments/assets/fde94ecc-4598-4e74-b318-5a23c47963bb" />




다섯 개 후보의 **전하**, **소수성**, **helix propensity**, **hydrophobic moment** 등을 비교하였다.

## 5. 구조 예측

후보 서열의 구조는 **ColabFold**를 이용해 예측하였다. 이 단계는 정밀한 최종 구조 결정이 아니라, 여러 후보를 빠르게 비교하기 위한 1차 screening으로 진행하였다.

후보들은 자연 단백질에서 가져온 서열이 아니라 직접 설계한 de novo 서열이므로, 충분한 MSA 정보를 기대하기 어렵다고 보아 `single_sequence` mode를 사용하였다.

## 6. 구조 예측 결과

| 후보 | 길이 | 평균 pLDDT | pTM | 해석 |
|:---|:---:|:---:|:---:|:---:|
| Design A | 35 | 95.1 | 0.506 | 매우 높은 신뢰도의 alpha-helix 예측 |
| Design D | 35 | 93.4 | 0.487 | 높은 신뢰도의 양전하성 alpha-helix 예측 |
| Design B | 36 | 94.4 | 0.519 | 높은 신뢰도의 amphipathic alpha-helix 예측 |
| Design E | 36 | 85.1 | 0.400 | 어느 정도 안정적인 예측이지만 A/B/D보다 낮음 |
| Design C | 35 | 74.1 | 0.401 | 상대적으로 낮은 신뢰도의 예측 |

ColabFold 결과에서는 Design A, Design B, Design D가 모두 높은 평균 pLDDT를 보였다. 세 후보 모두 alpha-helix 형태로 예측되었으며, 뚜렷한 구조적 붕괴나 긴 low-confidence 구간은 확인되지 않았다.

<img width="1270" height="661" alt="image" src="https://github.com/user-attachments/assets/bfd48199-2bb9-439d-8869-e4f2e312a188" />



**Design A**, **Design B**, **Design D**가 높은 구조 예측 신뢰도 (**>90**)를 보였다.

## 7. 구조 기반 평가

예측된 PDB 구조를 바탕으로 평균 pLDDT, 최소 pLDDT, low-confidence residue 비율, radius of gyration, helix-like fraction을 계산하였다.

| 순위 | 후보 | 잔기 수 | 평균 pLDDT | 최소 pLDDT | Low-confidence fraction | Radius of gyration | Helix-like fraction | Priority score |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Design A | 35 | 95.1 | 69.4 | 0.03 | 15.17 | 1.00 | 7.46 |
| 2 | Design D | 35 | 93.5 | 70.9 | 0.00 | 15.17 | 1.00 | 7.44 |
| 3 | Design B | 36 | 94.4 | 70.2 | 0.00 | 15.50 | 1.00 | 7.42 |
| 4 | Design E | 36 | 85.1 | 54.8 | 0.06 | 15.29 | 1.00 | 6.89 |
| 5 | Design C | 35 | 74.1 | 56.3 | 0.40 | 11.53 | 0.87 | 5.52 |

구조 점수만 기준으로 하면 **Design A**가 가장 높은 순위를 보였다. 그러나 Design A는 처음 설정한 소수성 비율 기준에는 다소 낮게 걸렸고, hydrophobic moment도 Design B보다 낮았다. 반면 Design B는 구조 기반 순위에서는 3위였지만 Design A와의 점수 차이가 작았고, 서열 기반 기준에서는 더 안정적인 균형을 보였다. 이러한 이유로 최종 후보는 **Design B**로 정하였다.

<img width="1265" height="568" alt="image" src="https://github.com/user-attachments/assets/909d5e3e-8fbd-445c-9415-9a7087e6cd0b" />





## 8. 최종 후보

최종 후보로 선택한 서열은 **Design B**이다.

```text
>Design_B_amp_helix_moderate
KLAKQLSEKLKQALSKQLAELKQALSKQLAELKKQS
```

**Design B를 선택한 근거**

- 순전하가 +6으로 항균 펩타이드 후보로 보기 적절한 범위에 있었다.
- 소수성 비율이 0.39로 설계 기준에 부합하였다.
- Hydrophobic moment가 후보 중 가장 높았다.
- ColabFold 평균 pLDDT가 94.4로 높게 나타났다.
- 전체 구조가 연속적인 alpha-helix로 예측되었다.

<img width="1794" height="631" alt="image" src="https://github.com/user-attachments/assets/a0b81cee-0c4f-44a9-bdba-8c0391347728" />


  
Design B는 ColabFold에서 연속적인 alpha-helix 형태로 예측되었다. 구조는 PyMOL에서 cartoon 형태로 시각화하였고, 색상은 residue별 pLDDT 값을 반영한다. 평균 pLDDT는 94.4였다.

<img width="1267" height="595" alt="image" src="https://github.com/user-attachments/assets/92dca82f-08e1-4733-94f7-ff95cea03b3a" />


 
대부분의 residue에서 높은 pLDDT를 보였고, 말단에서만 상대적으로 낮은 confidence가 확인되었다.

## 9. Design B 추가 분석

최종 후보로 선택한 Design B에 대해서는 구조 예측 결과를 더 자세히 살펴보았다. 먼저 residue별 pLDDT를 정리하였고, alpha-helix에서 각 residue가 어느 방향으로 배치되는지 확인하기 위해 helical wheel plot을 만들었다. 또한 PyMOL을 이용해 표면에서 양전하성, 음전하성, 소수성, 극성 residue가 어떻게 분포하는지 시각화하였다.

**Design B의 residue별 pLDDT 요약**

| 항목 | 값 |
|:---|:---:|
| 서열 길이 | 36 residues |
| 평균 pLDDT | 94.4 |
| 최소 pLDDT | 70.2 |
| pLDDT < 90인 residue 수 | 3 |

pLDDT가 90보다 낮은 residue는 주로 말단에 위치하였다.

| Residue | Amino acid | pLDDT |
|:---:|:---|:---:|
| 1 | LYS | 85.7 |
| 35 | GLN | 82.5 |
| 36 | SER | 70.2 |

Design B의 central helix 구간은 전반적으로 높은 confidence를 보였고, 상대적으로 낮은 confidence는 N-terminus와 C-terminus 부근에 집중되어 있었다. 짧은 peptide-like 구조에서는 말단이 더 유연하게 예측될 수 있으므로, 이 정도의 말단부 confidence 감소는 크게 문제 되는 결과로 보기는 어렵다.

<img width="1024" height="973" alt="image" src="https://github.com/user-attachments/assets/aa1f876f-822d-4118-84ef-24161db81265" />



Design B가 alpha-helix를 형성한다고 가정했을 때, 소수성 residue와 전하성 residue가 helix 둘레에 어떻게 배치되는지 나타낸다. 해당 배치 패턴을 통해 Design B의 양친매성 helix 형성 가능성을 확인할 수 있다.

<img width="3000" height="1140" alt="image" src="https://github.com/user-attachments/assets/84045537-be66-46e5-a9d5-96514964c7bc" />


 
대부분의 residue에서 높은 pLDDT를 보이며, 상대적으로 낮은 confidence는 주로 말단에 위치하였다.

<img width="1024" height="849" alt="image" src="https://github.com/user-attachments/assets/bee899bc-3260-4820-a1e6-0d6656f5b3d8" />


 
PyMOL 표면 시각화에서 Lys와 같은 양전하 residue, Glu와 같은 음전하 residue, Ala/Leu 같은 소수성 residue, Ser/Gln 같은 극성 residue를 서로 다른 색으로 표시하였다. 

## 10. Design B 재예측 결과

초기 구조 예측은 후보 5개를 빠르게 비교하기 위한 비교적 가벼운 조건에서 진행하였다. 이후 최종 후보인 Design B에 대해서는 ColabFold의 model 수와 recycle 수를 늘려 다시 예측하였다. 


| Rank | Model | Mean pLDDT | pTM |
|:---:|:---:|:---:|:---:|
| 1 | alphafold2_ptm_model_5_seed_000 | 97.1 | 0.59 |
| 2 | alphafold2_ptm_model_3_seed_000 | 97.1 | 0.61 |
| 3 | alphafold2_ptm_model_4_seed_000 | 96.8 | 0.57 |
| 4 | alphafold2_ptm_model_1_seed_000 | 94.5 | 0.53 |
| 5 | alphafold2_ptm_model_2_seed_000 | 92.3 | 0.49 |

다섯 개 모델 모두 평균 pLDDT가 92 이상이었고, rank 1 모델의 평균 pLDDT는 97.1이었다. 즉, Design B는 처음의 가벼운 예측 조건뿐 아니라 model 수와 recycle 수를 늘린 조건에서도 높은 confidence의 alpha-helix 구조로 예측되었다. 이는 Design B의 예측 구조가 한 번의 실행 결과에만 의존한 것이 아니라는 점을 뒷받침한다.

<img width="1926" height="646" alt="image" src="https://github.com/user-attachments/assets/d4d094d9-9990-41b6-ac0d-1f8e2e0ea152" />



Design B를 다섯 개 ColabFold model과 세 번의 recycle 조건으로 재예측했을 때 rank 1으로 선택된 구조이다. 평균 pLDDT는 97.1이었다.

## 11. 해석

현재 결과만 기준으로 하면 Design B는 항균 펩타이드 후보로 후속 분석을 진행해볼 만한 서열이다. 서열 수준에서는 전하와 소수성의 균형이 비교적 좋았고, 구조 예측에서도 안정적인 alpha-helix 형태를 보였다. 특히 hydrophobic moment가 높다는 점은 막과 상호작용할 수 있는 양친매성 helix 후보로 해석할 수 있는 근거가 된다.

추가 분석 결과도 Design B 선택을 어느 정도 지지하였다. Helical wheel plot에서는 소수성 residue와 전하성 residue의 배치를 확인할 수 있었고, PyMOL 표면 시각화에서도 residue 특성별 표면 분포가 뚜렷하게 나타났다. 또한 ColabFold 재예측에서 5개 모델 모두 높은 평균 pLDDT를 보여, Design B의 alpha-helical 구조 예측이 비교적 일관적인 것으로 확인되었다.

다만 이러한 결과가 실제 항균 활성을 직접 의미하는 것은 아니다. ColabFold의 pLDDT는 구조 예측의 신뢰도를 나타내는 값이며, 기능을 증명하는 지표는 아니다. 따라서 Design B는 검증이 완료된 항균 펩타이드라기보다는, 실험 검증 단계로 넘길 수 있는 우선 후보로 보는 것이 적절하다.

## 12. 한계


- ColabFold 재예측을 추가로 진행했지만, 전체 결과는 여전히 계산 예측에 기반한다.
- 실제 항균 활성은 실험적으로 확인하지 않았다.
- 막 결합 능력이나 세포 독성은 평가하지 않았다.
- 용해도, aggregation 가능성, protease 안정성은 별도로 분석하지 않았다.
- pTM 값은 높지 않았지만, 짧은 단일 helix 펩타이드라는 점을 고려하면 크게 이상한 결과로 보기는 어렵다.


## 13. 결론

항균 펩타이드 유사 후보 다섯 개를 설계하고, 서열 기반 평가와 ColabFold 구조 예측을 통해 후보를 비교하였다. 그 결과 Design B는 전하, 소수성, 양친매성, 구조 예측 신뢰도 측면에서 가장 균형 있는 후보로 확인되었다. 이후 Design B에 대해 helical wheel plot, residue별 pLDDT 분석, 표면 residue 특성 시각화, ColabFold 재예측을 추가로 수행하였고, 이 결과 역시 Design B를 우선 후보로 선택하는 근거가 되었다. 
