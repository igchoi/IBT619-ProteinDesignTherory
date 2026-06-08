# Seminar

**Seminar:** [How AF3-Style Structure Prediction Models Can Be Used for Design: BoltzDesign and Protein Hunter](https://www.youtube.com/watch?v=yCOlC_yj4kc)

**Paper 1:** [BOLTZDESIGN1: INVERTING ALL-ATOM STRUCTURE PREDICTION MODEL FOR GENERALIZED BIOMOLECULAR BINDER DESIGN](https://www.biorxiv.org/content/10.1101/2025.04.06.647261v1)

**Paper 2:** [Protein Hunter: exploiting structure hallucination within diffusion for protein design](https://www.biorxiv.org/content/10.1101/2025.10.10.681530v1)

**Presentation:** 

---

## 1. Summary

**Question:** Can we repurpose AF3-style structure prediction models — without fine-tuning or retraining — to *design* novel proteins and binders across diverse biomolecular targets?

**Algorithms:**
- **BoltzDesign1:** Inverts the Boltz-1 all-atom structure prediction model for binder design. Optimizes the probability distribution of pair features (predicted distogram) via the Pairformer and Confidence modules. Enables design of binders to proteins, small molecules, DNA, and RNA without fine-tuning.
- **Protein Hunter:** Exploits the hallucination behavior of AF3-style diffusion models. Starting from an all-X (unknown token) sequence, the model hallucinates a plausible fold, which is iteratively refined through cycles of sequence redesign (ProteinMPNN/LigandMPNN) and structure re-prediction (Boltz1/2 or Chai1). Fast, fine-tuning-free, and general.

---

## 2. Speaker

**Yehlin Cho**

- [GitHub](https://github.com/yehlincho) · [Personal Site](https://sites.google.com/view/yehlincho/home)

### Domain
- 🎓 **Career & Education**
  - **MIT** — PhD student, Department of Materials Science and Engineering (DMSE) & Biology
    - Advisor: Prof. Sergey Ovchinnikov
    - Research: ML for protein structure prediction and engineering
  - Awards: MOGAM-KASBP Scholarship (2022), SBS Foundation Scholarship (2021), BEST PDB Poster Award at ISMB 2024

- **Publications**
  - *BoltzDesign1: Inverting All-Atom Structure Prediction Model for Generalized Biomolecular Binder Design* (bioRxiv, 2025)
  - *Protein Hunter: Exploiting Structure Hallucination within Diffusion for Protein Design* (Nature Communications, 2025)
  - *Stable de novo protein design via joint conformational landscape and sequence optimization*
  - *Hit or Miss: Understanding Emergence and Absence of Homo-oligomeric Contacts in Protein Language Models*

- **Computational Portfolio**
  - **BoltzDesign1** — All-atom biomolecular binder design via Boltz-1 inversion
  - **Protein Hunter** — Fast, fine-tuning-free de novo protein design via structure hallucination

---

## 3. Reference

| Model | Description |
|---|---|
| **Boltz-1/2** | All-atom structure prediction model (AF3-style); backbone of BoltzDesign1 |
| **AlphaFold3** | All-atom diffusion-based structure prediction; used for cross-validation |
| **Chai-1** | AF3-style model integrated into Protein Hunter pipeline |
| **RFdiffusion / RFdiffusion-AA** | Structure-based generative diffusion model; benchmark baseline |
| **ProteinMPNN** | Sequence design from backbone structure; used in iterative cycling in Protein Hunter |
| **LigandMPNN** | Extends ProteinMPNN to handle small molecules, nucleic acids |
| **BindCraft** | Optimization-based binder design; gradient-descent baseline |

---

## 4. Tool

### BoltzDesign1
- [GitHub](https://github.com/yehlincho/BoltzDesign1) · [Google Colab](https://colab.research.google.com/github/yehlincho/BoltzDesign1/blob/main/Boltzdesign1.ipynb)
- Inverts Boltz-1 to design binders for proteins, small molecules, DNA, and RNA
- Optimizes via predicted distogram without backpropagating through all 200 diffusion steps
- Outputs designs with iPTM and pLDDT scores; includes AlphaFold3 cross-validation pipeline

```bash
# Example: protein binder design
python boltzdesign.py --target_name 7v11 --target_type protein --gpu_id 0 --design_samples 5

# Example: small molecule binder
python boltzdesign.py --target_name 7v11 --target_type small_molecule --target_mols OQO --gpu_id 0 --design_samples 2
```

---

### Protein Hunter
- [GitHub](https://github.com/yehlincho/Protein-Hunter)
- Fine-tuning-free de novo design via iterative structure hallucination + sequence redesign
- Supports: unconditional design, binder design (protein / peptide / small molecule / DNA / RNA), motif scaffolding, partial redesign
- Speed: ~10 sec for 100-residue protein, ~130 sec for 900-residue design

```bash
git clone https://github.com/yehlincho/Protein-Hunter.git
cd Protein-Hunter
chmod +x setup.sh && ./setup.sh   # auto-installs Boltz, Chai, LigandMPNN, ProteinMPNN
# AF3 must be installed separately
python run_protein_hunter.py
```

> ⚠️ AlphaFold3 setup is not included — install separately following official instructions.

---

### Boltz-1/2
- [GitHub (Boltz)](https://github.com/jwohlwend/boltz)
- AF3-style all-atom structure prediction model; used as the core engine for both BoltzDesign1 and Protein Hunter

---

### Chai-1
- [GitHub](https://github.com/chaidiscovery/chai-lab)
- Alternative AF3-style model supported in the Protein Hunter pipeline

---

### ProteinMPNN
- [GitHub](https://github.com/dauparas/ProteinMPNN)
- Designs amino acid sequences given a fixed backbone structure
- Core sequence redesign step in Protein Hunter's iterative cycling

---

### LigandMPNN
- [GitHub](https://github.com/dauparas/LigandMPNN)
- Extension of ProteinMPNN for contexts involving small molecules, DNA, RNA
- Used for all-atom binder design in Protein Hunter

---

### AlphaFold3
- [Official Inference Code](https://github.com/google-deepmind/alphafold3)
- Used for cross-validation of BoltzDesign1 and Protein Hunter outputs
- Self-consistency evaluation: re-fold designed sequences and check structural agreement (RMSD, ipTM, PAE)

---

## 5. Q&As in the Seminar

**key questions**

**Q1: Why is Boltz-2 so confident in its predictions compared to AlphaFold3?**
AlphaFold3 essentially memorizes correct structures and stretches them during inference, whereas Boltz-2 derives module weights directly from the Pairformer's confidence output. This means Boltz-2 has access to richer interface and complex-level information encoded in the pair representations, which likely explains its higher confidence scores. *(Personal hypothesis by the speaker.)*

**Q2: How do you experimentally measure and evaluate binding affinity (KD)?**
BLI (Bio-Layer Interferometry) is used. The target protein is immobilized on the BLI tip, and binders at varying concentrations are flowed over it. The resulting binding curves (kon/koff) are used to calculate KD. Notably, KD measurement is not strictly necessary for initial screening — the equilibrium curve itself provides sufficient information. The KD values reported in the papers are experimental, not computationally predicted; current models may estimate protein–protein KD during fine-tuning, but reliable prediction across diverse and difficult targets remains challenging.

**Q3: What filtering strategies are used to enrich for experimentally successful designs?**
Rough energy-based filters analogous to Rosetta are applied (e.g., ΔG, unsatisfied hydrogen bond residues). For specific cases, particular interaction types (e.g., specific bonds) are maximized during design. Using multiple models and examining correlations between metrics like affinity and KD across models helps obtain diverse, target-specific binder candidates.

**Q7: Does training data bias affect where binders dock on the target?**
Yes, bias is inevitable. When using all-X token sequences, the model sometimes docks at the binding pocket and sometimes elsewhere — there is genuine uncertainty about the binding site. This arises partly from overfitting to training data distributions and partly from target-specific variation. For example, a 10-X token sequence designed for one binding site may also score well at unintended sites. The exact nature of the binding pocket interference is not fully understood.

**Q9: Which of the three methods (BoltzDesign1, Protein Hunter, single diffusion) would you recommend?**
Each method has its strengths. **BoltzDesign1** fixes the interface first and redesigns around it, making it well-suited when you have a defined interface and want to leverage rich learned structural information. **Protein Hunter** (multi-step diffusion) is recommended when you want to maximize confidence scores quickly — it jointly optimizes sequence and structure iteratively and is the fastest option. For initial exploration, using multiple methods in parallel (as BindCraft does with ~5 models) is strongly advised, as performance varies considerably across targets.

---

## 6. Classmate Questions

`SWKim`: 

`YSOh`: 

`KHNam`: 

`DHKim`:  

`MSAn`: 
