# Reseach Plan
## AML에서 PIM kinase 활성을 억제하기 위한 ATP-binding pocket block형 de novo protein binder 설계
### 1.Background
#### 1) AML(Acute myeloid leukemia)
   Acute myeloid leukemia, AML은 진행 속도가 빠른 혈액암으로, chemotherapy, hematopoietic stem cell transplantation, targeted therapy 등이 주요 치료 전략으로 사용되고 있다. 환자의 유전자 변이에 따라 FLT3, IDH, BCL-2/venetoclax, menin inhibitor와 같이 환자의 genetic subtype에 따른 targeted therapy가 활발히 연구 및 적용되고 있다. FLT3-ITD AML에서는 constitutive FLT3 signaling이 STAT5 activation을 통해 PIM kinase 발현을 증가된다는 연구 결과가 있다.

#### 2) Pim kinase
   PIM kinase는 PIM1, PIM2, PIM3 세 가지 isoform으로 구성된 serine/threonine kinase family이다. AML, 특히 FLT3-ITD 양성 AML에서는 FLT3-STAT5 signaling을 통해 PIM kinase 발현이 증가할 수 있으며, PIM kinase는 cancer cell survival, proliferation, anti-apoptosis, drug resistance와 관련된 pathway에 관여한다. 따라서 PIM kinase는 AML에서 중요한 therapeutic target candidate로 여겨진다.
![Pim kinase](https://github.com/dohoon7482/123/blob/8595f4c972feafce16906bf3c7eaaa0b8a8f5ab5/cancers-14-03565-g001.png)

#### 3) ATP inhibitor protein
   Pim kinase에는 ATP binding site가 있어 약물이 개발될 때 흔히 사용된 target site이. 그러나 현재 현재까지 AZD1208, PIM447, INCB053914와 같은 pan-PIM small-molecule inhibitor들이 연구되었지만, AML에서 approved standard therapy로 사용되고 있지는 않으며 monotherapy 효과에도 한계가 보고되었다. 이러한 배경을 바탕으로 본 연구에서는 기존 small-molecule inhibitor와는 다른 방식으로, PIM kinase의 ATP-binding pocket 주변부를 차폐할 수 있는 de novo protein binder candidate를 computational tool을 이용해 in silico로 설계하고자 한다.

---
### 2. Strategy
본 연구에서 PIM kinase 억제를 위해 두 가지 binder design 전략을 설정했습니다. 첫째, ATP-binding pocket 입구와 hinge/P-loop 주변을 차폐하여 ATP 접근을 sterically block하는 competitive-like binder를 설계합니다. 둘째, PIM kinase 표면의 potential allosteric pocket에 결합하여 ATP-binding pocket의 conformation 또는 kinase activity를 간접적으로 저해하는 allosteric binder를 탐색하고자 합니다.
#### 1) A plan(Main) - Competitive inhibitor
   Protein으로 디자인할때 ATP pocket에 들어가는 구조를 만들기는 어렵기 때문에 ATP pocket rim + hinge/P-loop 주변을 덮어서 ATP의 접근을 막는 binder로 디자인을 하고자 합니다.
#### 2) B plan(Sub) - Allosteric inhibitor
   알려진 Allosterinc site가 있지만 명확히 확립된 site가 아니므로 사용에 어려움은 있겠지만 Allosterinc site에 결합하는 binder portein을 디자인해 ATP pocket 구조를 변형 시켜 ATP 접근을 막고자 합니다.

---
### 3. Computational pipeline
   - step1. PDB에서 PIM1/2를 target으로 구조 기반 ATP-binding pocket, hinge, P-loop, pocket rim residue 정의
   - step2. Competitive-like epitope와 potential allosteric pocket 후보 선정  
   - step3. RFdiffusion - 3D 구조에 hotspot residue를 지정해서 binder backbone 디자인
   - step4. ProteinMPNN - 만들어진 binder backbone의 sequence 디자인 및 monomer stability filtering
   - step5. AlphaFold2 Multimer - Complex 예측, ipTM, PAE, clash filtering
   - step6. Rosetta InterfaceAnalyzer - ΔG, buried SASA, shape complementarity 계산(binding energy)
   - step7. 최종 후보 선별

---
### 4. Expected results
   Checmical을 이용하지 않은 protein으로 pim kinase를 억제함으로써 체내에서 일어날 수 있는 toxicity를 최소화 할 수 있으며 충분한 구조와 binding affinity 최적화를 통해 이전 임상 실험에서 발생한 monotherapy에서의 효과가 낮았던 점을 개선할 수 있을것으로 예상합니다.

---
### 5. Limitation
   ATP pocket을 커버하여 binding하는 residue를 찾기 어렵고 Allosteric site에 대한 알려진 정보가 적어 탐색에 있어 어려움이 존재합니다.
