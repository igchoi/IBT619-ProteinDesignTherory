# Seminar
- Seminar: [**Discrete diffusion models for generative protein design**](https://www.youtube.com/watch?v=iV_7mgxe4OI&t=1203s)  
- Paper: [Protein generation with evolutionary diffusion: sequence is all you need](https://www.biorxiv.org/content/10.1101/2023.09.11.556673v1)
- [Presentation](https://docs.google.com/presentation/d/1qkhc8TLJXyW_kuOD6BntSoyWBaDfw9GC/edit?slide=id.p15#slide=id.p15)

## 1. Summary

- Question: Can we design novel proteins to expand functional space?
- Algorithms: **Discrete diffusion models** for protein sequence generation. Leverages evolutionary data (MSA). Corrupts sequences via masking/mutation. Learns reverse denoising process to generate novel sequences. Enables conditional design (evolution-guided, inpainting, scaffolding).


## 2. Speaker
### **[Sarah Alamdari](https://github.com/sarah-alamdari)**
**Senior Applied Scientist at Microsoft Research**  
*Biology × Deep Learning × Molecular Simulation*

---

**- Repositories & Tools**

- [EvoDiff](https://github.com/microsoft/evodiff)  
  Diffusion-based generative model for designing proteins using only sequence data 

- [ProtNote](https://github.com/microsoft/protnote)
  Multimodal deep learning tool for protein function prediction and annotation  

- [CleaveNet](https://github.com/microsoft/cleavenet)
  Deep learning toolkit for predicting and generating peptide cleavage sites  
  
---

**- 🎓 Career & Education**

- Microsoft Research (2021–Present)  
  *Senior Applied Scientist*  
  - Biomedical Machine Learning group  
  - Leads AI models for protein design (e.g., EvoDiff)

- University of Washington (2016–2021)  
  *PhD, Chemical Engineering*  
  - Molecular dynamics (MD), computational chemistry  
  - NSF GRFP Fellow  

- Arizona State University (2012–2016)
  *BS, Chemical Engineering*  
  - Magna Cum Laude  
  - Undergraduate research in 2D materials  

---

**- 🏆 Awards & Honors**

- MIT Rising Star (Chemical Engineering)  


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
1. [EvoDiff (OADM & D3PM)](https://github.com/microsoft/evodiff) 
   - Diffusion-based framework for protein sequence generation without structural templates  

2. [MSA Transformer](https://github.com/facebookresearch/esm)  
   - Utilizes MSA to capture co-evolutionary signals (EvoDiff-MSA)  

3. [OmegaFold](https://github.com/HeliXonProtein/OmegaFold) 
   - Predicts 3D structures to assess foldability of generated sequences  

4. [ProteinMPNN](https://github.com/dauparas/ProteinMPNN ) & [ESM-IF](https://github.com/facebookresearch/esm) 
   - Inverse folding tools for self-consistency evaluation  

5. [ProtT5 (ProtTrans)](https://github.com/agemania/ProtTrans)
   - Embedding model for functional space analysis (FPD)  


## 5. Q&As in the seminar

* Q1
  - A1

* Q2
  - A2


## 6. Classmate Questions

`SWKim`: 

`MJBaek`: 

`KHNam`:  

`DHKim`:  

`MSAn`:  











