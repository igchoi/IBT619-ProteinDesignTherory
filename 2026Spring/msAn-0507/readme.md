# Seminar

- Seminar: [**Design of small molecule binding proteins using deep learning**](https://www.youtube.com/watch?v=IgFgAYQrke4)
- Paper: [Zero-shot design of drug-binding proteins via neural selection-expansion](https://www.biorxiv.org/content/10.1101/2025.04.22.649862v1)
- Presentation: [Presentation](https://docs.google.com/presentation/d/1ws4AlQLbKcqhcTR76mKUP2D4t3vjk0UsFeAhCtBkIKE/edit?usp=sharing)

## 1. Summary

- **Question:** Can we use artificial intelligence to design proteins that bind to target small molecules (e.g., drugs) without physical experiments (zero-shot)?
- **Algorithms:** Graph neural network **LASErMPNN** for protein sequence and side-chain design → **RFAA (RoseTTAFold All-Atom)** for 3D structure prediction → **NISE (Neural Iterative Selection-Expansion)** algorithm to iteratively optimize sequence, structure, and ligand placement.

## 2. Speaker

### [Ben Fry](https://github.com/benf549)

Harvard Medical School Biophysics PhD Candidate | Polizzi lab

- **Who:** A PhD candidate in Biophysics at Harvard Medical School (Polizzi lab), focusing on the computational design of small-molecule binding proteins utilizing deep learning algorithms such as LASErMPNN and NISE.
- **Background:**
   - Johns Hopkins University, *BS*, *Biophysics*
   - Harvard Medical School, *PhD Candidate*, *Biophysics*
      - in [Polizzi lab](https://www.polizzilab.org)

## 3. Related Literatures/Reference

- [Zero-shot design of drug-binding proteins via neural selection-expansion (*bioRxiv*, 2025)](https://www.biorxiv.org/content/10.1101/2025.04.22.649862v1)
- [AF2BIND: predicting small-molecule binding sites using the pair representation of AlphaFold2 (*Nature Communications*, 2024)](https://www.nature.com/articles/s41592-026-03011-2)
- [De novo design of drug-binding proteins with predictable binding energy and specificity (*Science*, 2024)](https://www.science.org/doi/10.1126/science.adl5364)
- [Binding and sensing diverse small molecules using shape-complementary pseudocycles (*Nature Chemical Biology*, 2024)](https://www.science.org/doi/10.1126/science.adn3780)
- [Structure-based drug design with equivariant diffusion models (*Nature Computational Science*, 2024)](https://www.nature.com/articles/s43588-024-00737-x)

## 4. Related distribution/packages

- **LASErMPNN**
   - [GitHub](https://github.com/polizzilab/LASErMPNN)
   - A neural network model that designs sequences and side-chain angles using protein and ligand graphs.
- **NISE (Neural Iterative Selection-Expansion)**
   - [GitHub](https://github.com/polizzilab/NISE)
   - An algorithm that combines LASErMPNN and RFAA to cyclically optimize protein sequences, structures, and ligand positions.
- **CARPdock**
   - [GitHub](https://github.com/benf549/CARPdock)
   - A tool for rapidly generating the initial physical placement of small molecules.

## 5. Q&As in the seminar

**Q1: (SPICE 데이터셋 사전 학습 유무에 따른) 3%의 성능 차이는 얼마나 의미가 있습니까?** 
- A: 딥러닝 모델 훈련 시 보통 하이퍼파라미터가 동일하더라도 ±1~2% 오차가 발생합니다. 따라서 3%의 차이는 꽤 유의미(Decently meaningful)하며 양자역학(QM) 데이터 학습이 단순 PDB 데이터보다 물리적 타당성을 부여함이 검증됩니다.

**Q2: 해당 구조에서는 리간드 간(Ligand-Ligand) 상호작용은 모델링되지 않은 것 같네요.** 
- A: 사실이 아닙니다. 사전 훈련(Pre-trained)된 인코더에 내장되어 임베딩이 고정되어 있을 뿐입니다. 경쟁 모델은 원자 간 완전 연결망(Fully connected)을 쓰지만, 저희는 공간 기하학적 특성을 살리기 위해 K-최근접 이웃(KNN) 그래프 구조를 사용합니다.

**Q3: 요약 수치인 Kd 외에 개별 결합/해리 속도(Kaon/Kaoff)도 구하셨습니까?** 
- A: 본인은 컴퓨터 모델링 전담이라 정확히 알 수 없고, 실험실 테크니션이 측정했을 수 있습니다.

**Q4: 35회 루프 중 구조 예측기가 잘못된 카이랄성(Chirality)을 뱉어냈는데 디자인은 무사합니까?** 
- A: 다행히 외부 노출 꼬리 부분 오류였고, 핵심 포켓 입체 중심 에러는 RMSD 필터로 걸러졌습니다. 향후엔 양자역학(DFT) 기반 Conformer로 고정시키는 제약(Constrain) 모듈을 강제화할 계획입니다.

**Q5: 35사이클 동안 뼈대가 바뀌나요, 리간드가 움직나요?** 
- A: 핑퐁 치듯 동시에 아주 미묘하게 변합니다. 나선축이 약간 평평해지고 리간드가 수 옹스트롬 미만으로 정밀하게 이동합니다.

## 6. Classmate Questions

`YSOh`: 

`MJBaek`:

`KHNam`: 

`DHKim`: 

`MSAn`: 
