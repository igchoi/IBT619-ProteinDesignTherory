# Seminar

**Seminar:** [How AF3-Style Structure Prediction Models Can Be Used for Design: BoltzDesign and Protein Hunter](https://www.youtube.com/watch?v=yCOlC_yj4kc)

**Paper 1:** [BOLTZDESIGN1: INVERTING ALL-ATOM STRUCTURE PREDICTION MODEL FOR GENERALIZED BIOMOLECULAR BINDER DESIGN](https://www.biorxiv.org/content/10.1101/2025.04.06.647261v1)

**Paper 2:** [Protein Hunter: exploiting structure hallucination within diffusion for protein design](https://www.biorxiv.org/content/10.1101/2025.10.10.681530v1)

**Presentation:** [2026_proteindesigntheory_mjbaek_0611](https://docs.google.com/presentation/d/1a-y7bXH90u-M8cVhh4Onw2vwY9oLNbz0/edit?usp=sharing&ouid=101911527141458545753&rtpof=true&sd=true)

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
- **Education**
  - Massachusetts Institute of Technology (MIT)
    - Ph. D. in Department of Materials Science and Engineering (DMSE) Sep. 2021 - May.2026
  - Korea Advanced Institute of Science and Technology (KAIST)
    - B.S. in Materials Science and Engineering (MSE) Mar. 2017 – Feb. 2021 
  
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

## 5. [Q&As](https://docs.google.com/document/d/182tMNwqGitB6rTey5Hn6ihYR9ato6_YZOgkIQx_anT8/edit?usp=sharing) in the Seminar

**key questions**

**Q1: 왜 Boltz-2가 다른 모델들 보다 더 confident한 구조를 만드나?**

정확한 이유는 불명확하지만 발표자 가설은 이렇습니다. Boltz-2는 Performer 기반 모듈에서 confidence weight를 직접 계산합니다. 그 과정에서 링커와 복합체 내 상호작용 정보가 더 풍부하게 반영되는 것 같다. 파라미터 수, 레이어 구성 등도 영향을 줄 것으로 봅니다.

**Q2: 실험적 성공률이 낮은 이유는?**

발표자도 고민 중인 문제입니다. 현재는 Rosetta 기반 필터링—delta G, 불포화 수소결합 잔기 등—으로 rough하게 걸러냅니다. 특정 결합이나 상호작용을 극대화하는 방향으로 설계하기도 하고, 여러 모델을 함께 써서 affinity나 KD의 상호 연관성을 보면서 다양한 타입의 바인더를 얻는 방식을 씁니다.

**Q5: 왜 알라닌 편향이 생기나?**

X 토큰으로 시작하면 초반에 알라닌이 많이 나옵니다. Folding 모델이 사이드체인을 알라닌 수준의 단순한 5개 원자(C-alpha 중심)로 표현하기 때문에 구조 예측 시 알라닌으로 수렴하는 경향이 있습니다. 그래서 알라닌 편향 옵션을 넣어서 초반에는 알라닌이 많더라도 사이클이 진행될수록 점진적으로 줄어들게 설계했습니다. 마지막에는 덜 편향된 서열로 수렴합니다.

---

## 6. Classmate Questions

`SWKim`: 

`YSOh`: 

`KHNam`: 

`DHKim`:  

`MSAn`: I have a question regarding BoltzDesign's optimization strategy. As I understand it, the optimization process relies primarily on the Pairformer's distogram as a proxy objective. This approach appears to prioritize high-confidence, high-probability regions of the learned distribution while implicitly filtering out lower-confidence candidates. Under this framework, could potentially viable de novo designs be overlooked simply because they fall outside the model's learned distribution? In particular, highly novel candidates may receive lower confidence scores despite being biophysically feasible. 
 Intuitively, restricting the search space to high-probability regions might reduce structural diversity and could even limit the discovery of successful but unconventional solutions. Given this concern, how does the distogram-based optimization strategy ultimately achieve higher design accuracy and experimental yield without suffering from a significant loss of diversity or innovation?


