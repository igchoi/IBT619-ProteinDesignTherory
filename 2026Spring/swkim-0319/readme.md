# Topic

- Seminar: [**BindCraft: one-shot design of functional protein binders**](https://www.youtube.com/watch?v=qQihl6If9vU)  
- Paper: [One-shot design of functional protein binders with BindCraft](https://www.nature.com/articles/s41586-025-09429-6) 

## 1. Seminar Summary

- Question: *Can we design a functional binder for every protein while reducing costs for experimental screening?*  
- Algorithms: **de novo binder design** with AlphaFold2 Multimer &rarr; **sequence optimization** with MPNN_sol &rarr; ***in silico* filtering** with AlphaFold2 monomer


## 2. Who is the speaker?  

### [Martin Pacesa](https://scholar.google.com/citations?user=-pCwE2IAAAAJ&hl=en)
- Affiliation: [Assistant Professor, Institute of Pharmacology, University of Zurich](https://openreview.net/profile?id=~Martin_Pacesa1) (2026-Present)
- Background
  1. Research Interest: structural biology, protein design, nucleic acids, gene editing
  2. MS (Molecular Life Sciences), PhD (Biochemistry) - meaning he was originally experimental scientist.
  3. During his PhD, he started to solve biological problems with deep learning. His first notable work was [AlphaFold-Multimer](https://www.biorxiv.org/content/10.1101/2021.10.04.463034v2) (bioRxiv, 2022), co-authored with [John Jumper](https://deepmind.google/blog/demis-hassabis-john-jumper-awarded-nobel-prize-in-chemistry/) & [Demis Hassabis](https://deepmind.google/blog/demis-hassabis-john-jumper-awarded-nobel-prize-in-chemistry/). 
  4. Since 2022, he published lots of papers targeting open-source and generalized protein binder design platform, and finally he distributed [BindCraft](https://www.nature.com/articles/s41586-025-09429-6) (Nature, 2025).  
  5. He now opened his lab in University of Zurich to understand the interactome between protein and nucleic acid.

## 3. Related literatures/references 

-  [Watson, J. L. et al. De novo design of protein structure and function with RFdiffusion. 
*Nature* **620**, 1089–1100 (2023).](https://www.nature.com/articles/s41586-023-06415-8)
- [Dauparas, J. et al. Robust deep learning–based protein sequence design using ProteinMPNN. 
*Science* **378**, eadd2187 (2022).](https://www.science.org/doi/10.1126/science.add2187)
- [Gainza, P., Wehrle, S., Van Hall-Beauvais, A. et al. De novo design of protein interactions with learned surface fingerprints. *Nature* **617**, 176–184 (2023).](https://www.nature.com/articles/s41586-023-05993-x)

Besides these literatures, there are lots of trials to design protein *de novo*. If you are interested in another approaches, please see the reference of [BindCraft paper](https://www.nature.com/articles/s41586-025-09429-6). 

## 4. Related distribution/packages

- **BindCraft**
    - [github](https://github.com/martinpacesa/BindCraft?tab=readme-ov-file)
    - [google colab notebook](https://colab.research.google.com/github/martinpacesa/BindCraft/blob/main/notebooks/BindCraft.ipynb) 
    - *Note*: BindCraft is an open-source model, but user needs GPU at least A100. 
- **RFdiffusion**
    - [github](https://github.com/RosettaCommons/RFdiffusion)
    - [specific part on github for binder design](https://github.com/RosettaCommons/RFdiffusion?tab=readme-ov-file#binder-design)
    - [google colab notebook](https://colab.research.google.com/github/sokrypton/ColabDesign/blob/v1.1.1/rf/examples/diffusion.ipynb)
    - *Tip*: If you download these notebooks on your local environment, they may not work few days later. One of the common issue is version up. You need to re-download notebooks. 
- **ProteinMPNN**
    - [github](https://github.com/dauparas/ProteinMPNN)
    - You can find useful example in RFdiffusion notebook!
- **AlphaFold Server**
  - [webpage](https://alphafoldserver.com/)
  - On the webpage, you can freely predict the structure of protein monomer, and diverse interaction such as Protein-Protein Interaction, Protein-DNA interaction, or with ions & ligands **30 times per day**. 
- **Neurosnap**
    - If you don't like colab notebook, you can easily use diverse AI-based bioinformatics tools on [Neurosnap](https://neurosnap.ai/).

## 5. Audience Question

`YSOh`:  
`MJBaek`:  
`KHNam`:  
`DHKim`:  
`MSAn`:  
