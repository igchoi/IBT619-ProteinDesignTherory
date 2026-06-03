# [Term Project] Predicting Evolutionary Fitness and Sequence Optimization of Carotenoid and Violacein Biosynthetic Genes Using Genomic Language Models (5/14 :Shedding light on functional dark matter with genomic language modeling)

## 1. Background & Objectives
* **Background:** In metabolic engineering and synthetic biology, maximizing the microbial production of natural pigments hinges heavily on the efficiency of their biosynthetic pathways. However, fine-tuning enzyme expression often hits a bottleneck due to unexpected rate-limiting steps or suboptimal sequence fitness.
* **Problem Statement:** We are utilizing a diverse set of genes from the violacein and carotenoid pathways to synthesize target pigments. Screening the relative catalytic efficiencies and stability of these numerous enzyme variants solely through wet-lab trial-and-error is highly resource-intensive.
* **Objectives:** Utilizing the core concepts from genomic language modeling, this project aims to evaluate the evolutionary fitness of these specific pigment-producing genes in silico, rank their predicted efficiencies, and map out beneficial mutational hotspots to guide target sequence optimization.

---

## 2. Target Pathway Genes for Analysis
The project will focus on evaluating and optimizing the following specific gene sets responsible for the core steps in the violacein and carotenoid biosynthetic networks:

### A. Violacein Pathway Variant Genes
* Core sequential enzymes for violacein synthesis:
  * *vioA*
  * *vioB*
  * *vioC*
  * *vioD*
  * *vioE*

### B. Carotenoid Pathway Variant Genes
* Core logic, cyclization, and tailoring enzymes:
  * *crtB* (Phytoene synthase)
  * *crtI* (Phytoene desaturase)
  * *crtY* / *crtY(crtL)* (Lycopene cyclase)
  * *crtZ* (Carotene hydroxylase)
  * *crtW* (Beta-carotene ketolase)
  * *crtG* (Carotenoid 2-hydroxylase)
  * *crtE* (GGPP synthase)
  * *crtD* (Methoxyneurosporene dehydrogenase)
  * *crtO* (Beta-carotene ketolase variants)
  * *cruF* (Gamma-carotene cyclase)
  * *CYP287A1* (Cytochrome P450 carotenoid hydroxylase)
  * *crtT* (Torulene methyltransferase)
  * *crtU* (Beta-carotene desaturase variants)
  * *crtV*
  * *crtEb* (Lyco-di-cyclase)
  * *crtYe* (C50 carotenoid cyclase)
  * *crtYf* (C50 carotenoid cyclase)

---

## 3. Methodology & Pipeline

The project implements a 3-step computational pipeline derived from large-scale genomic transformers.

### Phase 1: Dataset Curation and Preprocessing
* Extract complete nucleotide and amino acid sequences (FASTA format) for all the listed *vio* and *crt* gene variants.
* Gather a reference dataset of high-yielding, naturally occurring homologous enzymes from NCBI/UniProt to serve as a benchmark control group for each gene family.

### Phase 2: Evolutionary Fitness Scoring via Genomic Language Models
* **Model Selection:** Deploy large-scale protein language models such as **ESM-2** or DNA-level autoregressive models like **Evo (Grok-ST)**.
* **Likelihood Scoring:** Input each gene sequence to compute its **Log-Likelihood / Perplexity Score**. This metric determines how well the specific sequence conforms to the "evolutionary grammar" optimized by nature for that pigment step.
* **Relative Ranking:** Plot a comparative distribution profile to identify where each of our provided gene variants ranks against the global natural sequence pool (e.g., Top 5%, Median, or Suboptimal).

### Phase 3: In Silico Deep Mutational Scanning (DMS)
* Leverage the masking and token-prediction capabilities of the language models to run an exhaustive single-point mutation scan across all residues of our target enzymes.
* Generate a comprehensive DMS score heatmap to separate **Deleterious Mutations** (functional collapse) from **Beneficial Mutations** (efficiency/stability boosts).
* Output the **Top 5 optimized mutant sequences** for each pathway gene.
