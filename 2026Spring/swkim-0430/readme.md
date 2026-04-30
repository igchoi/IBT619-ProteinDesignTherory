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


## 6. Classmate Questions

`YSOh`: 

`MJBaek`: 

`KHNam`: Are only high-scoring hotspot seeds selected and stitched in the score-then-stitch pipeline? And is the number of hotspots used for stitching dependent on the target protein?

`DHKim`: The Binding Energy predicted by calculation was high, but what do you think caused the failure in the actual experimental results?

`MSAn`: 
