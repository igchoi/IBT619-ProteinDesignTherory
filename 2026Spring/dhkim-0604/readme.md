# Reseach Plan
## Acute myeloid leukemia(AML)에서 과발현되는 Pim kinase를 억제하기 위한 ATP binding site block 단백질 디자인
### 1.Background
#### 1) AML(Acute myeloid leukemia)
   AML은 급성 골수성 백혈병으로 진행이 매우 빠릅니다. 현재 사용되고 있는 치료법으로는 항암화학요법과 조혈모세포 이식이 기본적입니다. 환자의 유전자 변이에 따라 FLT3(FMS-like tyrosine kinase 3), IDH, venetoclax, menin 등과 같은 표적 치료를 메인으로 연구되고 있습니다. NCI에서 AML 치료 옵션으로 chemotherapy, stem cell transplant, targeted therapy 등을 제시하고 있습니다. AML에서는 FLT3-ITD 양성에서 FLT3 → STAT5 신호가 활성화되면 Pim kinase 발현이 증가 된다는 연구 결과가 있습니다.
#### 2) Pim kinase
   Pim kinase는 PIM1, PIM2, PIM3 세 종류가 있으며 serine/threonine kinase입니다. 기능으로는 암세포의 생존·증식·약제저항성을 도와주는 보조 신호로 활용됩니다. 즉, FLT3-ITD AML에서는 FLT3가 가속화 시킨다면 PIM kinase는 그 신호를 받아 암세포가 더 잘 버티게 해주는 보조역할을 하고 있다 볼 수 있습니다.
![Pim kinase](https://github.com/dohoon7482/123/blob/8595f4c972feafce16906bf3c7eaaa0b8a8f5ab5/cancers-14-03565-g001.png)
#### 3) ATP inhibitor protein
   Pim kinase에는 ATP binding site가 있어 약물이 개발될 때 흔히 사용된 target site입니다. 그러나 현재 Pim kinase inhibitor는 AML의 승인된 표준치료제가 없습니다. AZD1208, PIM447, INCB053914 등 같은 pan-PIM inhibitor들이 AML 또는 혈액암에서 임상시험까지 갔지만, monotherapy에서 효과가 제한적이거나 개발이 중단된 사례가 있습니다. 때문에 De nove ATP binding inhibitor protein을 디자인 하고자 합니다.

---
### 2. Strategy
ATP inhibitor는 크게 ATP binding site에 직접적으로 결합하여 ATP가 결합하지 못하게해 활성을 낮추는 Competitive inhibitor와 target으로 하는 kinase의 다른 부분에 결합하여 ATP pocket의 구조를 변형 시켜 ATP를 결합하지 못하게 하는 Allosteric inhibitor 두 가지 있습니다. 
#### 1) A plan - Competitive inhibitor
   Protein으로 디자인할때 ATP pocket에 들어가는 구조를 만들기는 어렵기 때문에 ATP pocket rim + hinge/P-loop 주변을 덮어서 ATP의 접근을 막는 binder로 디자인을 하고자 합니다.
#### 2) B plan - Allosteric inhibitor
   알려진 Allosterinc site가 있지만 명확히 확립된 site가 아니므로 사용에 어려움은 있겠지만 Allosterinc site에 결합하는 binder portein을 디자인해 ATP pocket 구조를 변형 시켜 ATP 접근을 막고자 합니다.

---
### 3. Computational pipeline
   - step1. PDB에서 구조를 찾아 ATP binding stie residue 및 Allosteric site residue 탐색  
   - step2. RFdiffusion - 3D 구조에 hotspot residue를 지정해서 binder backbone을 생성  
   - step3. ProteinMPNN - 만들어진 binder backbone의 서열을 설계  
   - step4. AlphaFold2 Multimer - 서열의 구조 예측과 ipTM 필터링  
   - step5. Rosetta InterfaceAnalyzer - ΔG, shape complementarity 계산(binding energy)  

### 4. Expected results
   Checmical을 이용하지 않은 protein으로 pim kinase를 억제함으로써 체내에서 일어날 수 있는 toxicity를 최소화 할 수 있으며 충분한 구조와 binding affinity 최적화를 통해 이전 임상 실험에서 발생한 monotherapy에서의 효과가 낮았던 점을 개선할 수 있을것으로 예상합니다.

### 5. Limitation
   ATP pocket을 커버하여 binding하는 residue를 찾기 어렵고 Allosteric site에 대한 알려진 정보가 적어 탐색에 있어 어려움이 존재합니다.
