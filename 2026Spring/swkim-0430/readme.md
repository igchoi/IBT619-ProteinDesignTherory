# Seminar

- Seminar: [**Fragment-based backbone sampling & neural net derived potentials to design protein-binding peptides**](https://www.youtube.com/watch?v=CZn8BdvRYJU) 
- Paper: [Computational Methods for the Structure-Based Design of Protein-Binding Peptides](https://www.proquest.com/docview/3031029492?pq-origsite=gscholar&fromopenview=true&sourcetype=Dissertations%20&%20Theses)
- Presentation: [PPT](https://docs.google.com/presentation/d/1_LP0FdfPm8qsgqFh-CeucEZbUhJcFGix/edit?usp=drive_link&ouid=102328751853466048865&rtpof=true&sd=true)

## 1. Summary

- **Question:** Can we design **peptide binders** to target protein, and do better with AI?
- **Algorithms:** **Peptide building block (seed) generation** from naturally occurring tertiary motifs &rarr; **fragment sequence and structure scoring** utilizing neural network (COORDinator) &rarr; **connecting seeds with loops** into full peptide


## 2. Speaker

### [Sebastian Swanson](https://www.linkedin.com/in/sebastian-swanson-727827a7/)
Computational peptide design | Senior Data Scientist [@ Novo Nordisk](https://www.novonordisk.com/science-and-technology/research-technologies.html) (2023-Present)

- **Who:** Senior data scientist at Novo Nordisk with a background of studying the principles of peptide-protein interactions and developing computational methods for the design of peptide binders in Amy Keating's lab at the Massachusetts Institute of Technology (MIT). He is now applying physics-based methods and deep learning models to design peptide therapeutics. 
- **Background:**
  - University of Minnesota, *BS*, *Biochemistry* (2013-2017)
  - Massachusetts Institute of Technology (MIT), *PhD*, *Biology* (2017-2022)
        - in [Amy Keating's lab](https://www.keatinglab.mit.edu/)


## 3. Related Literatures/Reference

- [Tertiary motifs as building blocks for the design of protein-binding peptides (*Protein Science*, 2022)](https://onlinelibrary.wiley.com/doi/full/10.1002/pro.4322)
  - Sebastian Swanson also gave a [seminar on BPDMC](https://www.youtube.com/watch?v=kiKIj4gGY7o) about this topic in 2020
- [One-shot design of functional protein binders with BindCraft (*Nature*, 2025)](https://www.nature.com/articles/s41586-025-09429-6)
- [De novo design of protein structure and function with RFdiffusion. 
(*Nature*, 2023)](https://www.nature.com/articles/s41586-023-06415-8)
- [Neural network-derived Potts models for structure-based protein design using backbone atomic coordinates and tertiary motifs (*Protein Science*, 2022)](https://onlinelibrary.wiley.com/doi/full/10.1002/pro.4554)

## 4. Related distribution/packages

- **Sebstian's github repository**
  - [RelE peptide binder design](https://github.com/KeatingLab/relE_binder_design) Case Study: majority of the codes are written in C++.
  - [Seed generation](https://github.com/swanss/peptide_design): almost all the codes are written in C++.
- **RFdifffusion**
  - [github](https://github.com/RosettaCommons/RFdiffusion?tab=readme-ov-file#binder-design)
  - [google colab notebook](https://colab.research.google.com/github/sokrypton/ColabDesign/blob/v1.1.1/rf/examples/diffusion.ipynb)
  - RFdiffusion is one of the state-of-the-art methods for de novo protein design. And you can run it with google colab's free GPU resource. It is a great choice for the first trial.

## 5. Q&As in the seminar

**Q1: COORDinator의 input으로 multi-chain backbone coordinates를 이용하는가? COORDinator의 사전학습 시에 intramolecular interaction만 있는 single-chain structure만 이용해도 비슷한 결과가 나올까?**   
A: 그렇다. 그리고 interface scoring 등의 목적으로 사용할 때는 multi-chain이 더 나은 것 같다.   
**Q2: Seed의 energy를 계산할 때 전체 complex 구조를 고려하는가 아니면 interface region만 고려하는가?**  
A: Energy를 계산하는 여러 방법이 있을 수 있지만, 본 연구에서는 interface region을 고려하는 것이 효과적으로 보였다.   
**Q3: 생성된 seed들이 실제 native-peptide 구조나 서열로 수렴하지는 않는가?**  
A: 그렇지는 않다.  
**Q4: Native peptide fragment와 seed의 Rosetta energy를 비교할 때 fragment와 seed 서열의 길이는 비슷했나?**  
A: 그렇다. 만약 길이가 다르다면, 일반적으로 길이가 긴 fragment가 더 낮은 energy를 가진다.   
**Q5: Structure-score를 계산할 때, chain 간의 거리를 고려했나?**  
A: 그렇다. Chain 간의 거리에 따라 한 residue에서 최대 8개까지의 interaction이 가능했는데, 거리가 멀어질수록 side chain 간의 interaction이 주를 이루었다.   
**Q6: 생성한 서열들 혹은 peptide들이 self-interaction할 가능성은 고려했나?**  
A: 그렇다. 예전에는 AF2를 이용해서 예측했을 때 complex가 이뤄지지 않는 경우가 있었는데, 지금은 괜찮다.  
**Q7: Seed들을 연결하는 loop의 score는 어떤가?**  
A: loop는 interaction보다는 연결에 초점을 두기 때문에 길어질수록 score에 penalty를 준다. 실제 높은 score를 가진 peptide candidate 들은 loop가 2~3 residue 정도이다.  

## 6. Classmate Questions

`YSOh`: 

`MJBaek`: 

`KHNam`: Are only high-scoring hotspot seeds selected and stitched in the score-then-stitch pipeline? And is the number of hotspots used for stitching dependent on the target protein?

`DHKim`: The Binding Energy predicted by calculation was high, but what do you think caused the failure in the actual experimental results?

`MSAn`: 
