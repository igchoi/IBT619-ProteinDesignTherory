# 🧬 De Novo Protein Design Plan for a Small Functional Protein

**Protein Design Proposal**

**Course: Protein Design Theory (IBT619)**

**Date: 2026-06-04**

**Speaker: KI HYUN NAM**

## 📌 1. Overview

The goal is to explain how a hypothetical de novo protein design project can be planned, from target selection to computational evaluation.

This summarizes the overall rationale, workflow, expected evaluation criteria, and limitations of a hypothetical de novo protein design project.

---

## 🎯 2. Design Target

The conceptual design target is a **small alpha-helical functional protein**.

This protein type was selected because small alpha-helical proteins are structurally simpler than large multi-domain proteins, making them more suitable as an initial target for a conceptual de novo protein design.

Possible functional directions include:

* **Mini-binder**
* **Small scaffold protein**
* **Antimicrobial peptide-like protein**

**[Examples of Small Functional Protein Targets]**

<img width="875" height="557" alt="image" src="https://github.com/user-attachments/assets/95e36cae-1de8-4a2a-8ec2-02a6929c4608" />



---

## 🧭 3. Design Scope

The proposal includes the following components:

* **Selection of a hypothetical design target**
* **Explanation of the backbone design logic**
* **Explanation of the sequence design logic**
* **Evaluation plan based on structure prediction**
* **Functional plausibility assessment**
* **Discussion of limitations**

---

## 🔁 4. De Novo Protein Design Workflow

**For a small alpha-helical functional protein, the de novo protein design workflow is established as follows:**

**1. Design goal definition**
  
**2. Selection of target function**
          
**3. Protein backbone design or generation**
          
**4. Amino acid sequence design compatible with the backbone**
                 
**5. Structure prediction of the designed sequence**
        
**6. Comparison between the predicted structure and the intended design**
             
**7. Evaluation of stability and functional plausibility**
       
**8. Candidate prioritization**

**The purpose of each step is as follows:**

| Step                     | Purpose                                                                         |
| :------------------------: | :-------------------------------------------------------------------------------: |
| Design goal definition           | Define what type of protein will be designed in terms of its intended function or structural features     |
| Selection of target function       | Establish possible functional directions, such as antimicrobial peptide-like activity, binding, or scaffold formation |
| Backbone design or generation     | Design the overall 3D framework of the protein based on an alpha-helical structure                         |
| Sequence design          | Construct an amino acid sequence that allows the designed backbone to fold stably                      |
| Structure prediction     | Evaluate whether the designed sequence is likely to form the intended structure                                           |
| Design comparison        | Compare the predicted structure with the intended backbone design                                               |
| Evaluation               | Assess the design based on stability, structural plausibility, and functional plausibility          |
| Candidate prioritization | Select relatively suitable candidates based on the evaluation criteria                                          |

---

## 🧩 5. Design Strategy

### 5.1 Target Function

The protein to be designed is defined as a **small functional protein**.

**Possible functional directions include:**

* **Mini-binder**
* **Small scaffold protein**
* **Antimicrobial peptide-like protein**

Among these possibilities, this proposal uses **antimicrobial peptide-like function** as the main functional example.

Therefore, the target function of the designed protein is defined as to design a small alpha-helical protein with functional features that may enable interaction with the bacterial surface or bacterial membrane.

However, the main objective is not to design a protein with actual antimicrobial activity. Rather, the focus is to explain how a function can be defined in a de novo protein design project and how corresponding structural and sequence features can be considered during the design process.

---

### 5.2 Backbone Design

In the backbone design step, the overall three-dimensional structural framework of the protein is defined.

**Key factors to consider in backbone design include:**

* **Overall protein length**
  
* **Number of alpha-helices**

* **Arrangement and orientation of the helices**

* **Overall structural compactness**

* **Potential for internal hydrophobic core formation**

* **Positions of surface-exposed residues**

* **Structural flexibility or space to form a functional surface**

---

### 5.3 Sequence Design

In the sequence design step, an amino acid sequence is designed so that the selected backbone can fold stably.

**Key factors to consider in sequence design in this project include:**

* **Hydrophobic residues positioned in the internal core**

* **Polar residues positioned on the protein surface**

* **Positively charged residues to support potential interaction with bacterial membranes**

* **Residue patterns suitable for alpha-helix formation**

* **Avoidance of overly unstable or unrealistic sequence patterns**

* **Compatibility between the designed backbone structure and the amino acid sequence**

* **Residue arrangement that can form a functional surface**

considering an antimicrobial peptide-like function, the balance between **positive charge** and **hydrophobicity** is important at the sequence level. Positive charge may contribute to electrostatic interactions with the bacterial surface, while hydrophobic residues may be related to membrane interaction.

if hydrophobicity is too high, the possibility of nonspecific interactions or aggregation may increase. Therefore, the balance between functional properties and structural stability should be considered.

---

### 5.4 Structure Prediction

In the structure prediction step, the designed sequence is evaluated to determine whether it can form a structure similar to the intended backbone.

The key question in this step: **Can the designed amino acid sequence fold into the intended alpha-helical structure?**

**Factors that should be considered during structure prediction:**

* **Whether the predicted structure maintains an alpha-helical fold**

* **Whether the predicted structure is similar to the intended backbone**

* **Whether the overall structure forms a compact architecture**

* **Whether excessive unstable or disordered regions are present**

* **Whether functional residues or functional surfaces are exposed to the exterior**

* **Whether the structure prediction confidence is sufficient**

Although this does not demonstrate the actual function of the designed protein, it serves as an important computational checkpoint for assessing whether the designed sequence and structure are consistent with each other.

---

### 5.5 Functional Plausibility

Evaluate whether the designed structure and sequence can be logically connected to the target function.

**When antimicrobial peptide-like function is used as an example, the following factors can be considered:**

* **Distribution of positive charges on the protein surface**

* **Spatial pattern of hydrophobic and hydrophilic residues**

* **Potential formation of an amphipathic alpha-helix**

* **Arrangement of residues that may interact with the bacterial surface or bacterial membrane**

* **Overall structural stability and exposure of the functional surface**

* **Similarity to the general features of known antimicrobial peptides**

**Functional plausibility** is not a criterion for confirming actual biological activity. Rather, it is a conceptual evaluation step used to assess whether the designed protein is logically consistent with the intended target function.

---

## 💻 6. Computational Evaluation Plan

Computational evaluation criteria are established to assess the designed de novo protein candidates.

The key question in the evaluation step: 

**Can the designed sequence form the intended backbone structure, and does it contain structural and sequence-level features related to the target function?**

| Category           | Evaluation Point                        | Description                                                                                                                           |
| :------------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------: |
| Backbone           | Feasibility of the intended structure   | Evaluate whether the designed alpha-helical backbone is not overly complex and can realistically form as a small protein.             |
| Sequence           | Compatibility with the backbone         | Evaluate whether the designed amino acid sequence contains residue patterns that can stabilize the intended backbone.                 |
| Folding            | Structure prediction results            | Determine whether the predicted structure is similar to the intended alpha-helical structure.                                         |
| Stability          | Structural compactness                  | Evaluate whether the overall structure forms a compact architecture and whether an internal hydrophobic core is appropriately formed. |
| Surface property   | Charge distribution                     | Determine whether positive charges or polar residues are appropriately distributed on the protein surface.                            |
| Functional surface | Arrangement of functional residues      | Evaluate whether residues or surfaces related to the target function are exposed to the exterior.                                     |
| Amphipathicity     | Hydrophobic/hydrophilic pattern         | Evaluate whether the alpha-helix is likely to form distinguishable hydrophobic and hydrophilic faces.                                 |
| Disorder           | Presence of disordered regions          | Check whether excessively flexible or disordered regions appear in the predicted structure.                                           |
| Specificity        | Possibility of nonspecific interactions | Evaluate whether excessive hydrophobicity or charge imbalance may increase the likelihood of nonspecific interactions.                |
| Feasibility        | Possibility of future validation        | Evaluate whether the candidate can be further validated through future experimental or additional computational analyses.             |

---

### 6.1 Structure-Based Evaluation

In structure-based evaluation, the designed sequence is assessed to determine whether it is likely to form the intended structure.

**Main evaluation factors:**

* **Whether the alpha-helical fold is maintained**

* **Whether the overall structure is compact**

* **Whether the predicted structure is similar to the intended backbone**

* **Whether structurally unstable regions are not excessive**

* **Whether an internal hydrophobic core can be formed**

* **Whether the functional surface is exposed to the exterior**

If the structure prediction result differs substantially from the intended design, the candidate may need to be revised at the sequence design or backbone design step.

---

### 6.2 Sequence-Based Evaluation

In sequence-based evaluation, the designed amino acid sequence is assessed to determine whether it is suitable for the target structure and function.

**Main evaluation factors:**

* **Whether the sequence length is appropriate**

* **Whether the sequence contains residue patterns suitable for alpha-helix formation**

* **Whether hydrophobic residues are appropriately positioned in the internal core**

* **Whether polar or charged residues are appropriately positioned on the surface**

* **Whether the balance between positive charge and hydrophobicity is appropriate**

* **Whether there are overly repetitive or unrealistic sequence patterns**

When considering an antimicrobial peptide-like function, the combination of positive charge and hydrophobic residues can be an important factor.

If either of these features is excessive, the possibility of nonspecific membrane interaction or aggregation may increase. Therefore, maintaining a proper balance is important.

---

### 6.3 Function-Oriented Evaluation

In function-oriented evaluation, the designed candidate is assessed to determine whether it can be logically connected to the target function.

**Main evaluation factors:**

* **Whether electrostatic interactions with the bacterial surface may be formed**

* **Whether hydrophobic residues are positioned where they could contribute to membrane interaction**

* **Whether an amphipathic alpha-helix is likely to form**

* **Whether the functional surface is structurally exposed**

* **Whether structural stability and potential functional interaction are balanced**

---

### 6.4 Candidate Prioritization

Finally, the candidates can be prioritized based on the evaluation criteria described above.

**High-priority candidates would have the following features:**

* **They maintain the intended alpha-helical structure well.**

* **They show relatively high structure prediction confidence.**

* **Their overall structure appears compact and stable.**

* **They show high compatibility between the sequence and backbone.**

* **The functional surface is well exposed to the exterior.**

* **The balance between positive charge and hydrophobicity is appropriate.**

* **They show limited disorder and a low possibility of nonspecific interactions.**

Based on these criteria, suitable candidates can be selected for further analysis or future validation.

---

## ⚠️ 7. Limitations

This proposal focuses on organizing the overall stages and evaluation criteria of a de novo protein design process, rather than discussing the detailed algorithms in depth.

**First,** the small alpha-helical functional protein defined in this proposal is a conceptual design target. Therefore, the actual performance of the protein candidate cannot be fully determined based only on structure prediction results and sequence-level features.

**Second,** antimicrobial peptide-like function is used as a functional example. However, actual antimicrobial activity is influenced by various factors, including sequence, structure, target cell type, membrane composition, and peptide concentration. Therefore, biological activity cannot be confirmed through computational evaluation alone.

**Third,** de novo protein design requires specialized tools and interpretation at multiple stages, including backbone generation, sequence design, structure prediction, and candidate filtering. This proposal focuses on the core logic and evaluation criteria of each step, while detailed algorithms or advanced modeling procedures are discussed only in a limited manner.

**Fourth,** the stability, specificity, solubility, and aggregation tendency of the designed protein are important factors for assessing its practical applicability. However, in this proposal, these factors are treated only as conceptual evaluation criteria, and quantitative analysis is not included.

---

## ✅ 8. Expected Outcome

**Through this proposal, the following points are summarized:**

* **Definition of the design target and target function**

* **Construction of a de novo protein design workflow**

* **Basic logic of backbone design and sequence design**

* **Evaluation plan based on structure prediction**

* **Criteria for functional plausibility assessment**

* **Criteria for candidate prioritization**

* **Limitations that should be considered during the de novo protein design process**

Ultimately, this proposal focuses on understanding that de novo protein design is not simply a process of generating new sequences. Rather, it is a stepwise design process that connects target function definition, structural design, sequence design, predicted structure evaluation, and functional plausibility assessment.





















