# Seminar
- Seminar: [**Discrete diffusion models for generative protein design**](https://www.youtube.com/watch?v=iV_7mgxe4OI&t=1203s)  
- Paper: [Protein generation with evolutionary diffusion: sequence is all you need](https://www.biorxiv.org/content/10.1101/2023.09.11.556673v1)  
- Presentation: [2026_proteindesignclass_MJ](https://docs.google.com/presentation/d/10Jx54ySwFa0DGtVcM631dQXtkJ4Xj0u4/edit?slide=id.p1#slide=id.p1)  

## 1. Summary

- Question: Can we design novel proteins to expand functional space?  
- Algorithms: **Discrete diffusion models** for protein sequence generation. Leverages evolutionary data (MSA). Corrupts sequences via masking/mutation. Learns reverse denoising process to generate novel sequences. Enables conditional design (evolution-guided, inpainting, scaffolding).  

## 2. Speaker

### **Sarah Alamdari**
- [github](https://github.com/sarahalamdari)  
- [her domain](https://www.sarahalamdari.com/)  

---

### **- 🎓 Career & Education**

- [Microsoft Research](https://www.microsoft.com/en-us/research/) (2021–Present)  
  *Senior Applied Scientist*  
  - Biomedical Machine Learning group  
  - Leads AI models for protein design (e.g., EvoDiff)  

- University of Washington (2016–2021)  
  *PhD, Chemical Engineering*  
  - Molecular dynamics (MD), computational chemistry  

- Arizona State University (2012–2016)  
  *BS, Chemical Engineering*  
  - Undergraduate research in 2D materials  

- [Publications](https://scholar.google.com/scholar?hl=ko&as_sdt=0%2C5&q=sarah+alamdari&btnG=)  
  - [Protein generation with evolutionary diffusion: sequence is all you need](https://www.biorxiv.org/content/10.1101/2023.09.11.556673v2.abstract)  
  - [Orientation and Conformation of Proteins at the Air–Water Interface Determined from Integrative Molecular Dynamics Simulations and Sum Frequency Generation Spectroscopy](https://pubs.acs.org/doi/full/10.1021/acs.langmuir.0c01881)  

---

### **- computational portfolio**

- MIT Rising Star (Chemical Engineering)  

- [EvoDiff](https://github.com/microsoft/evodiff)  
  - Diffusion-based generative model for designing proteins using only sequence data  

- [CleaveNet](https://github.com/microsoft/cleavenet)  
  - Deep learning toolkit for predicting and generating peptide cleavage sites  

## 3. Reference

1. [Structured Denoising Diffusion Models (D3PM)](https://arxiv.org/abs/2107.03006)  
   - Foundation for discrete diffusion models used in protein sequences  

2. [Autoregressive Diffusion Models (ARDM)](https://arxiv.org/abs/2204.04202)  
   - Order-agnostic sequence generation (OADM)  

3. [MSA Transformer](https://arxiv.org/abs/2104.09967)  
   - Learns evolutionary patterns from MSA data  

4. [RFdiffusion](https://www.nature.com/articles/s41586-023-06415-8)  
   - Structure-based diffusion baseline (requires 3D coordinates)  

5. [ESM-1b](https://www.pnas.org/doi/10.1073/pnas.2016239118)  
   - Protein language model capturing evolutionary rules  

## 4. Tool

### EvoDiff (OADM & D3PM)
- [github](https://github.com/microsoft/evodiff)  
- Diffusion-based framework for protein sequence generation without structural templates  
- You can generate protein sequences directly using evolutionary information (MSA optional)  

---

### MSA Transformer
- [github](https://github.com/facebookresearch/esm)  
- Utilizes MSA to capture co-evolutionary signals (EvoDiff-MSA)  
- Can be used for extracting evolutionary constraints and embeddings  

---

### OmegaFold
- [github](https://github.com/HeliXonProtein/OmegaFold)  
- Predicts 3D protein structures from sequences  
- Used to validate foldability of generated sequences  

---

### ESM-IF 
- [ESM-IF](https://github.com/facebookresearch/esm)  
- Inverse folding tools (structure → sequence)  
- Used for self-consistency evaluation with generated proteins  
- You can also find useful examples in RFdiffusion notebooks  

---

### ProtT5 (ProtTrans)
- [github](https://github.com/agemania/ProtTrans)  
- Protein embedding model  
- Used for functional space analysis (e.g., FPD)  

---

### RFdiffusion
- [github](https://github.com/RosettaCommons/RFdiffusion)  
- Structure-based diffusion model for protein design  
- Specific binder design pipelines available in repository  
- [google colab notebook](https://colab.research.google.com/github/RosettaCommons/RFdiffusion/blob/main/notebooks/design_protein.ipynb)  
- Tip: If you download notebooks locally, they may break due to version updates → re-download recommended  

--- 

## 5. Q&As in the seminar

- [Q&A list](https://docs.google.com/document/d/1p-X4sM8lkT6Nnxf6Bqlx3lHlafFc8sItmlM9NJJt27Q/edit?tab=t.0)  

- Key questions  

* Q1: Potts Model(공진화 모델)을 쓰면 더 정확하지 않을까?(5번 질문)  
  - A1: Potts 모델은 특정 MSA 하나에 최적화되지만, EvoDiff는 64개씩 서브샘플링하며 반복 학습하므로 훨씬 방대한 진화적 예시를 학습할 수 있음.  

* Q2: Scaffolding 작업 시 성공 요인은?(12번 질문)  
  - A2: 단순히 구조적 복잡성보다는, 시퀀스 타입이나 데이터셋 내 출현 빈도가 모델의 성공 여부와 더 관련있을 듯.  

* Q3: Inference(추론) 시 디코딩 순서(Decoding Order)가 중요한가?(13번 질문)  
  - A3: 학습 시 다양한 마스크 길이를 경험하므로, 추론 시 모든 스텝을 일일이 조절하거나 순차적으로 할 필요 없이 효율적임.  

* Q4: 서열 생성 시 길이를 미리 정해야 하나?(15번 질문)  
  - A4: 학습 시에는 가변적이지만, 실제 생성(Inference) 단계에서는 원하는 길이가 있다면 설정해야 함.  

## 6. Classmate Questions

`SWKim`:  

`YSOh`:  **First**, regarding the performance comparison of EvoDiff, the paper compares it with other tools such as ESM-2. However, performance of these tools often seems to depend on the specific type of protein. In that case, is it really appropriate to make a performance comparison and conclude that EvoDiff is better? **Second**, since the paper does not provide in vitro validation results, how can we know whether the designed proteins actually perform as predicted computationally?

`KHNam`:  

`DHKim`:  

`MSAn`:  Is it possible to incorporate cofactors into the protein design process itself? Since most enzymes rely on them, I’m wondering if we can design proteins with pre-determined binding sites and interactions for specific coenzymes
