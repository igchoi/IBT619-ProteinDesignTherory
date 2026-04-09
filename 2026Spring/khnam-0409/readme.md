# Seminar
- Seminar: [**Computational Design of non-porous, pH-responsive antibody nanoparticles**](https://youtu.be/FX7yBJKQuPg?si=FYIvwJRcjoodvgAF) 
- Paper: [**Computational Design of non-porous, pH-responsive antibody nanoparticles**](https://www.nature.com/articles/s41594-024-01288-5) 
- Presentation: [**Presentation Material**](https://docs.google.com/presentation/d/13WIBRYbhnSoJFg0B_Ice2_nNp8fgKf0T/edit?slide=id.p1#slide=id.p1)

---
## 1. Summary
- **Question:** *Can pH-responsive, non-porous antibody nanoparticles be computationally designed for efficient cargo delivery and release?*
- **Algorithms:** Extended the pH-responsive trimer fusion using **WORMS**, docked it onto nanoparticles with **RPXDock** to evaluate interface feasibility, and optimized trimer and tetramer sequences with **Rosetta** to design variants modulating cargo packaging and pH responsiveness.

## 2. Speaker
### [Erin Yang](https://www.linkedin.com/in/erincyang/)
Protein Designer | ML & Structural Biology for Novel Medicines | Symmetry Enthusiast
- **Who:** Scientist in Computational Protein Design with a PhD from the University of Washington (David Baker & Neil King Labs). Expertise in de novo protein generation, antibody design, and platform innovation at the intersection of computational modeling and experimental validation. Experienced in leading cross-functional teams, developing ML-driven design pipelines, and mentoring researchers to deliver impact in therapeutic discovery and molecular design
- **Affiliation:** Scientist (Computational protein Generation), Generate Biomedicines:Somerville, MA, US (2023.10 ~ present)
- **Background:**
1. Wellesley College: Wellesley, Massachusetts, US
BA, Department of Chemistry (2012.09.01 to 2016.06.01)

2. University of Washington: Seattle, WA, US
PhD, Department of Biochemistry (2018.09.01 to 2023.09)

## 3. Related Literatures/Reference
- [Hierarchical design of pseudosymmetric protein nanocages (2025)](https://www.nature.com/articles/s41586-024-08360-6)
- [Intranasal neomycin evokes broad-spectrum antiviral immunity in the upper respiratory tract (2024)](https://www.pnas.org/doi/abs/10.1073/pnas.2319566121)
- [Blueprinting extendable nanomaterials with standardized protein blocks (2024)](https://www.nature.com/articles/s41586-024-07188-4)
- [Rapid and automated design of two-component protein nanomaterials using ProteinMPNN (2024)](https://www.pnas.org/doi/abs/10.1073/pnas.2314646121)
- [Accurate computational design of three-dimensional protein crystals (2023)](https://www.nature.com/articles/s41563-023-01683-1)
- [De novo design of monomeric helical bundles for pH-controlled membrane lysis (2023)](https://onlinelibrary.wiley.com/doi/full/10.1002/pro.4769)
- [Fast and versatile sequence-independent protein docking for nanomaterials design using RPXDock (2023)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010680)

## 4. Related distribution/packages
**1. WORMS (helical fusion software)**
   - Software used to fuse or link helical protein subunits in desired ways to build larger or more complex protein structures.
   - **In research:** Used to fuse helical repeat proteins to extend pH-responsive trimer building blocks, filling the pores along the C3 axes of an octahedral nanoparticle.
   - [Github](https://github.com/willsheffler/worms)

**2. RDXDock (protein docking software)**
   - A tool used to predict how two or more proteins (or protein domains) interact to form a complex.
   - **In research:** Used to precisely dock the extended trimer plug into the threefold symmetric pores inside antibody nanoparticles.
   - [Github](https://github.com/willsheffler/rpxdock)

**3. Rosetta Macromolecular Modeling**
   - A powerful software used to address a wide range of protein science problems, including structure prediction, design, modeling, and protein–protein docking
   - **In research:** Used to optimize RPXDock-docked sequences for stability and interactions, and to design variants controlling cargo packaging and pH responsiveness.
   - [Web](https://rosettacommons.org/)

## 5. Q&As in the seminar
[**Q&A List**](https://docs.google.com/document/d/1s5P8uvxmlCE2S1HsYh2YY29TFTNhMPIGOT77wAhwzBE/edit?usp=drive_link)

## 6. Classmate Questions
`SWKim`:

`YSOh`:

`MJBaek`: I have two questions. One is 'how did they make 3D particles after cryo-EM?' I just curious about how to convert 2D to 3D and how to make a particles as a real things. And the other one is 'Is it possible to reverse reaction?' I mean after the release between molecules by pH, and can they re-gathering again by pH differences?

`DHKim`:

`MSAn`:Unlike viruses, if a material bursts inside an endosome, can the endosome itself also tear open
