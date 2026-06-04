# Research Plan
## AML에서 PIM kinase 활성을 억제하기 위한 ATP-binding pocket block형 De novo protein binder 설계
### 1.Background
#### 1) AML(Acute myeloid leukemia)
   Acute myeloid leukemia, AML은 진행 속도가 빠른 혈액암으로, chemotherapy, hematopoietic stem cell transplantation, targeted therapy 등이 주요 치료 전략으로 사용되고 있다. 환자의 유전자 변이에 따라 FLT3, IDH, BCL-2/venetoclax, menin inhibitor와 같이 환자의 genetic subtype에 따른 targeted therapy가 활발히 연구 및 적용되고 있다. FLT3-ITD AML에서는 constitutive FLT3 signaling이 STAT5 activation을 통해 PIM kinase 발현을 증가된다는 연구 결과가 있다.

#### 2) PiIM kinase
   PIM kinase는 PIM1, PIM2, PIM3 세 가지 isoform으로 구성된 serine/threonine kinase family이다. AML, 특히 FLT3-ITD 양성 AML에서는 FLT3-STAT5 signaling을 통해 PIM kinase 발현이 증가할 수 있으며, PIM kinase는 cancer cell survival, proliferation, anti-apoptosis, drug resistance와 관련된 pathway에 관여한다. 따라서 PIM kinase는 AML에서 중요한 therapeutic target candidate로 여겨진다.
<img src="https://github.com/igchoi/IBT619-ProteinDesignTherory/blob/7fa8cc430e1f8001966726889a1412c12fc5e0d7/2026Spring/dhkim-0604/Pim%20kinase.png" width="100%" height="100%" />

#### 3) ATP inhibitor protein
   PIM kinase에는 ATP binding site가 있어 약물이 개발될 때 흔히 사용된 target site이. 그러나 현재 현재까지 AZD1208, PIM447, INCB053914와 같은 pan-PIM small-molecule inhibitor들이 연구되었지만, AML에서 approved standard therapy로 사용되고 있지는 않으며 monotherapy 효과에도 한계가 보고되었다. 이러한 배경을 바탕으로 본 연구에서는 기존 small-molecule inhibitor와는 다른 방식으로, PIM kinase의 ATP-binding pocket 주변부를 차폐할 수 있는 de novo protein binder candidate를 computational tool을 이용해 in silico로 설계하고자 한다.
<img src="https://github.com/igchoi/IBT619-ProteinDesignTherory/blob/7ee304a7f54283edffac25d3e2368aa35245cf5a/2026Spring/dhkim-0604/protein%20inhibitor.png" width="650" height="400" />


---
### 2. Research objective
연구의 목적은 RFdiffusion, ProteinMPNN, AlphaFold-Multimer, Rosetta InterfaceAnalyzer와 같은 computational protein design tools를 활용하여 PIM kinase ATP-binding pocket을 block할 가능성이 있는 de novo protein binder candidate를 설계하고 평가하고자 한다. PIM kinase의 ATP-binding pocket, hinge region, P-loop, catalytic cleft 주변 residue를 target epitope으로 설정하고, 이 부위를 덮어 ATP 접근을 sterically block할 수 있는 binder 구조를 in silico로 생성한다. 이후 구조 예측 및 interface analysis를 통해 유망한 binder candidate를 선별한다.

---
### 3. Strategy
#### 1) A plan : Competitive-like ATP-pocket-blocking binder design
   PIM kinase의 ATP-binding pocket 주변부에 결합하여 ATP 접근을 물리적으로 차단할 수 있는 binder를 설계하는 전략으로, Protein binder는 small molecule처럼 ATP pocket 내부에 깊게 들어가기 어렵기 때문에, ATP-binding pocket 내부가 아니라 pocket rim, hinge region, P-loop 주변을 덮는 방식의 competitive-like binder design을 목표로 한다.
#### 2) B plan : Potential allosteric binder design
   PIM kinase 표면의 potential allosteric pocket을 탐색하고, 해당 부위에 결합할 수 있는 binder를 설계하는 전략이다. Allosteric binder는 ATP-binding pocket에 직접 결합하지 않더라도 kinase domain의 conformation을 변화시키거나 ATP-binding pocket의 구조적 안정성을 방해할 가능성이 있다. 다만 PIM kinase에서 명확하게 확립된 allosteric site 정보는 제한적이다.

---
### 4. Computational pipeline
   - step1. PDB에서 PIM1/2를 target으로 구조 기반 ATP-binding pocket, hinge, P-loop, pocket hotspot residue 정의
   - step2. Competitive-like epitope와 potential allosteric pocket target epitope 선정  
   - step3. RFdiffusion - 3D 구조에 target epitope주변에 결합 가능한 binder backbone 생성
   - step4. ProteinMPNN - 만들어진 binder backbone의 sequence 생성 및 stability filtering
   - step5. AlphaFold2 Multimer - Complex 예측, ipTM, PAE, clash 및 결합 가능성 평가
   - step6. Rosetta InterfaceAnalyzer - ΔG, buried SASA, shape complementarity 계산(binding energy)
   - step7. 최종 후보 선별

---
### 5. Expected results
   본 연구를 통해 PIM kinase ATP-binding pocket 주변부에 결합할 수 있는 de novo protein binder candidate를 in silico로 확보할 수 있을 것으로 기대된다. 특히 ATP-binding pocket rim, hinge region, P-loop 주변을 덮는 binder candidate를 선별함으로써, ATP 접근을 sterically block할 가능성이 있는 구조적 모델을 제시할 수 있다.

---
### 6. Limitation
   - 1 - in silico design을 중심으로 하기 때문에, computational prediction 결과가 실제 binding affinity나 kinase inhibition을 보장하지 않는다는 한계가 있다. AlphaFold-Multimer와 Rosetta 기반 분석은 candidate filtering에는 유용하지만, 실제 단백질의 folding stability, binding affinity, inhibitory activity는 실험적으로 검증되어야 한다.
   - 2 - PIM kinase의 ATP-binding pocket은 작고 구조적으로 깊은 부위이기 때문에 protein binder가 pocket 내부에 직접 결합하기는 어렵다. 따라서 본 연구는 pocket 내부 결합이 아니라 ATP-binding pocket 주변부를 차폐하는 전략을 사용하지만, 이 구조가 실제로 ATP binding을 충분히 방해할 수 있는지는 추가 검증이 필요하다.
   - 3 - PIM kinase는 intracellular target이므로 실제 치료제로 확장하기 위해서는 cell delivery, intracellular expression, degradation, immunogenicity 등의 문제가 추가적으로 고려되어야 한다.
