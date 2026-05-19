# Seminar
- Seminar: [**Jointly Embedding Protein Structures and Sequences through Residue Level Alignment**](https://youtu.be/vGHrLbxyU-Y?si=b6N405PGE-sEX6ij)
- Paper: [**Jointly Embedding Protein Structures and Sequences through Residue Level Alignment**](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490763/)
- Presentation:

---
## 1. Summary
- **Question:** Can residue-level alignment of protein sequence and structure embeddings improve sequence–structure compatibility assessment and binder design screening?
- **Algorithms:** Residue Level Alignment (RLA): a self-supervised contrastive learning framework aligning ESM-2 sequence embeddings and COORDinator structure embeddings at the residue level.

## 2. Speaker
### [**Foster Birnbaum**](https://www.linkedin.com/in/foster-birnbaum-529738180/)

- **Affiliation:** PhD Student (Computational and Systems Biology), [Keating Lab](https://www.keatinglab.mit.edu/), massachusetts institute of technology (MIT), (2021.08 ~ Present)
- **Background:**
1. Stanford University: Stanford, California, US
Bachelor of Science - BS, Biochemistry and Molecular biology (2017.09 ~ 2021.06)

2. Stanford University: Stanford, California, US
Master of Science - MS, Computer Science (2018.09 ~ 2021.06)

## 3. Related Literatures/Reference
- [Evolutionary-scale prediction of atomic-level protein structure with a language model (2023)](https://www.science.org/doi/10.1126/science.ade2574)
- [Improving de novo protein binder design with deep learning (2023)](https://www.nature.com/articles/s41467-023-38328-5)
- [De novo design of protein structure and function with RFdiffusion (2023)](https://www.nature.com/articles/s41586-023-06415-8)
- [Robust deep learning–based protein sequence design using ProteinMPNN (2022)](https://www.science.org/doi/10.1126/science.add2187)



## 4. Related distribution/packages
**1. RLA code package**
- Software for training RLA models and calculating RLA similarity scores.
- **In research:** Used to align sequence and structure embeddings and evaluate sequence–structure compatibility.
- [**Github**](https://github.com/MadryLab/rla)

**2. ESM-2 / ESMFold**
- Protein language model for generating residue-level sequence embeddings.
- **In research:** Used as the pretrained sequence encoder and fine-tuned through RLA.
- [**Github**](https://github.com/facebookresearch/esm)

**3. COORDinator**
- MPNN-based structure encoder for protein backbone structures.
- **In research:** Used as the structure encoder to generate residue-level structure embeddings.

**4. Foldseek**
- Fast protein structure search tool.
- **In research:** Used to assess test–train structural overlap and possible data leakage.
- [**Github**](https://github.com/steineggerlab/foldseek)

**5.AlphaFold2 Initial Guess**
- AlphaFold2-based scoring method for binder design candidates.
- **In research:** Used as the main benchmark method for binder screening.
- [**Github**](https://github.com/google-deepmind/alphafold)

**6. Rosetta InterfaceAnalyzer / DockQ**
- Tools for protein interface scoring and docking quality evaluation.
- **In research:** Used to compare binder discrimination performance and define acceptable docking poses.
- [**Github**](https://github.com/wallnerlab/DockQ)


## 5. Q&As in the seminar


## 6. Classmate Questions
`SWKim`: 

`YSOh`: 

`MJBaek`: 

`DHKim`:

`MSAn`:
