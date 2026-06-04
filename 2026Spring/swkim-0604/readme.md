# Term Project Plan (SWKim)


## 1. Research Question

Does **genomic context-aware masked diffusion models** can generate functional protein sequences better than state-of-the-art protein language models (e.g. ESM3) and genomic language models (e.g. Evo 1, Evo 2)?  


## 2. Background and Motivation

### Gene design with generative genomic language models

Evo 1/Evo 2와 같은 genomic language model은 attention mechanism을 활용해서 자연어의 맥락을 이해할 수 있도록 하는 large language model (LLM)의 한 종류로, 자연어 대신 genomic sequence를 학습한 모델이다 [1-2]. 

| Model | Parameters | Training Data |
| --- | --- | --- |
|Evo 1| 7B | Bacteria, Archaea, and Virus (Phage); **OpenGenome**|
|Evo 2| 1B, 7B, 20B, 40B| All domains of life; **OpenGenome2**| 

![](https://github.com/igchoi/IBT619-ProteinDesignTherory/blob/main/2026Spring/swkim-0604/in-context%20gene%20generation%20with%20Evo1.5.png)

Evo 1의 모델 구조를 동일하게 유지한 채로, 학습을 조금 1.5배 오래하여 만든 Evo 1.5 모델은, 특정한 target gene 주위의 genomic context를 고려해서 highly conserved gene들과 동일한 function을 가지지만 서열이 다른 gene을 생성할 수 있다 [3]. 또한 genetic context가 어느정도 유지되어 있는 system의 경우 (e.g. bacteria toxin-antitoxin system, viral anti-CRISPR system) 본질적으로 다양성이 높은 gene이라도 Evo 1.5 모델이 functional gene을 생성할 수 있다 [3]. 


### Protein design with generative protein language models

ESM3와 같은 protein language model 역시 attention mechanism을 활용하고, 자연어 대신 protein sequence, structure, function을 동시에 학습한 multi-modal language model이다 [4]. 

![](https://github.com/igchoi/IBT619-ProteinDesignTherory/blob/main/2026Spring/swkim-0604/protein%20generation%20with%20ESM3.png)

ESM3 논문에서 보여준 위의 GFP의 에시와 같이, ESM3 모델은 특정한 기능의 active site를 비롯한 핵심적인 부위의 서열과 구조 정보만을 input으로 넣어주면, 나머지 부분을 생성할 수 있다. 논문의 저자들은 약 80,000개의 design를 computational filtering functions 및 experimental testing을 통해 natural GFP와 동등한 fluorescence를 가지지만 서열 유사도가 57% 수준인 de novo GFP를 만들어냈다 [4]. 추가로 ESM3 모델은 scaffolding 등에도 활용될 수 있다. **ESM3는 단백질의 서열-구조-기능을 동시에 학습하여 높은 성능을 보이지만, 단일 단백질 수준에서 학습되어 genomic context를 반영하여 protein design을 하는 것은 어렵다**.  

### Genomic context-aware protein design with generative masked diffusion models  

ESM3 모델의 architecture를 활용하여 처음부터 학습을 수행하거나, open source 모델을 fine-tuning하는 방향도 가능하지만, 전체 모델을 비교적 값싸고 빠르게 테스트해 볼 수 있는 상대적으로 작은 모델인 masked diffusion model을 활용해보기로 하였다. 특별히 단백질의 서열만을 이용해서 만든 masked diffusion model인 EvoDiff 모델의 architecture를 활용하기로 결정하였다 [5]. 

![](https://github.com/igchoi/IBT619-ProteinDesignTherory/blob/main/2026Spring/swkim-0604/EvoDiff%20style%20diffusion%20scheme.png)  

EvoDiff 논문에서 학습시킨 모델의 파라미터는 각각 38M과 640M으로, 38M의 경우 google colab에서도 학습이 가능한 수준으로 생각된다. 

## 3. Design Target

설계계한 masked diffusion model이 작동하는 것을 확인하기 위해서 가장 쉬운 예시를 생각하였고, *E. coli* trp operon을 design target으로 선정하였다. E. coli trp operon은 5개의 gene으로 구성되어 tryptophan biosynthesis에 관여하고 있다. 특히 tryptophan biosynthesis가 가능한 bacteria 등에서는 기능과 구조가 보존되어 있으므로, context를 고려하는 것이 가능하다. 그리고 앞선 Evo 1.5를 활용해서 genomic context를 고려하여 gene design을 한 논문 [3]에서도 trp operon을 활용하였으므로, EvoDiff style masked diffusion model과 genomic language model의 성능을 benchmarking 하기에도 적절한 예시이다. 

![](https://ars.els-cdn.com/content/image/3-s2.0-B9780123749840010962-f01096-02-9780123749840.jpg)

## 4. Computational Strategy

### 4.1 Model architecture

| Model | Parameters | Layers | Hidden Dim | Heads |
|---|---|---|---|---|
| EvoDiff (original, small) | 38M | 6 | 512 | 8 |
| EvoDiff (original, large) | 640M | 33 | 1280 | 20 |
| **Ours (context-aware)** | **~640M–1B (target)** | **40–48 (extended)** | **1280** | **20** |

EvoDiff 논문에서 학습시킨 모델의 파라미터는 각각 38M과 640M으로 최신 모델들에 비하면 작은 편이다. Genomic context를 고려한 protein design을 하기 위해서는 모델이 조금 더 클 필요가 있다고 생각되므로, 모델의 layers를 40-48로 늘려 테스트를 해볼 계획이다. Hidden dimension과 attention heads 역시 조금 더 확장해볼 수 있을 것이다. 

### 4.2 Training data construction

Prokaryotic system은 gene cluster, operon, defense island 등 기능적으로 연관된 유전자들이 물리적으로 연결되거나 가까이에 존재하는 특징이 있으므로 genomic context 학습에 적합하다. 

| Data Source | 용도 |
|---|---|
| NCBI RefSeq (Prokaryote complete genomes) | 전체 genome 서열 및 gene annotation |
| KEGG Pathway / OrthoFinder | Operon 및 기능적 gene cluster 확인 |
| DefenseFinder DB | Defense island annotation |
| DOOR2 / OperonDB | Operon 경계 annotation |
| OpenGenome (optional) | 광범위한 pre-training용 추가 데이터 |

실질적으로 원하는 task인, genomic context를 input으로 넣어주면 context에 맞는 functional protein sequence를 생성하도록 모델을 학습하기 위해서, data augmentation을 진행할 것이다. Data source로부터 수집한 operon 및 gene cluster 정보를 활용해서,

1) Window size를 3 또는 5로 설정하여 여러 개의 gene이 포함된 genomic context 데이터를 만든다.
2) 각 genomic context에서 1개의 gene을 masking하고, 모델이 amino acid residue level diffusion process를 통해서 masked gene의 원래 서열을 예측하도록 학습한다. 

### 4.3 Training strategy 

| 전략 | 장점 | 단점 |
|---|---|---|
| **Operon/gene cluster 증강 데이터만으로 학습** | 빠르고 단순, operon context에 집중 | 일반적인 단백질 서열 지식 부족, 수렴 불안정 가능성 |
| **OpenGenome으로 pre-training → operon fine-tuning** | 풍부한 단백질 서열 사전지식 확보, 안정적 수렴 | 컴퓨팅 비용 증가, pre-training 데이터 처리 복잡성 |

### 4.4 Evaluation

#### Simple in silico evaluation

| 평가 지표 | 방법 | 목적 |
|---|---|---|
| **Sequence recovery** | 생성 서열 vs. 자연 서열 간 identity (%) | 기본 서열 재현 능력 확인 |
| **Amino acid distribution** | KL divergence, per-position AA frequency 비교 | 자연 단백질과의 통계적 유사성 |
| **Structural plausibility** | ESMFold / AlphaFold3로 구조 예측 후 pLDDT, TM-score 분석 | 생성 서열의 3D 구조적 타당성 |
| **Functional site conservation** | PROSITE / functional annotation DB와 비교 | active site, binding site 등 핵심 잔기 보존 여부 |

#### Context-awareness evaluation

설계한 모델이 생성하는 단백질 서열들이 genomic context를 반영하는지 평가하기 위해서 아래의 평가를 진행한다. 

- **E. coli trp operon**: 1개 gene을 masking하고, 나머지 4개 gene을 context로 주어 생성 → 생성 서열의 구조 및 기능적 특성 분석
- **Cross-species context 실험**: *Bacillus subtilis*, *Salmonella typhimurium* 등 다른 종의 trp operon을 context로 입력했을 때 생성되는 서열이 species-specific한 특성을 반영하는지 확인 (서열 identity, phylogenetic placement 분석)
- **Context ablation 실험**: context gene 수를 0 (context 없음) → 1 → 2 → 4개로 늘려가며 생성 서열 품질의 변화를 측정, context 정보가 생성에 실질적으로 기여하는지 검증

#### Benchmarking

| Model | Context-aware | Modality | Evaluation 방법 |
|---|---|---|---|
| **Ours** | ✅ (multi-gene window) | Protein sequence | 위의 4.4 |
| **Evo 1.5** | ✅ (genomic context) | DNA sequence | 동일 trp operon task, 논문 [3] 기준 재현 |

### 4.5 Pipeline summary

```
[Prokaryotic genome DB]

        ↓ operon/gene cluster annotation

[Windowed multi-gene dataset 구성 + 데이터 증강]

        ↓ target gene masking

[Context-aware Masked Diffusion Model 학습]

        ↓ inference (trp operon context 입력)
        
[생성 서열 분석]
   ├─ Structural prediction (ESMFold/AlphaFold3)
   ├─ Functional annotation
   ├─ Cross-species context 실험
   └─ Benchmarking vs. Evo 1.5 / ESM3 / EvoDiff
```

## 5. Reference

**[1]** Eric Nguyen et al. ,Sequence modeling and design from molecular to genome scale with Evo.Science386,eado9336(2024).DOI:10.1126/science.ado9336  
**[2]** Brixi, G., Durrant, M.G., Ku, J. et al. Genome modelling and design across all domains of life with Evo 2. Nature 652, 1349–1361 (2026). https://doi.org/10.1038/s41586-026-10176-5  
**[3]** Merchant, A.T., King, S.H., Nguyen, E. et al. Semantic design of functional de novo genes from a genomic language model. Nature 649, 749–758 (2026). https://doi.org/10.1038/s41586-025-09749-7  
**[4]** Thomas Hayes et al. ,Simulating 500 million years of evolution with a language model.Science387,850-858(2025).DOI:10.1126/science.ads0018  
**[5]** Sarah Alamdari, Nitya Thakkar, Rianne van den Berg, Neil Tenenholtz, Robert Strome, Alan M. Moses, Alex X. Lu, Nicolò Fusi, Ava P. Amini, Kevin K. Yang
bioRxiv 2023.09.11.556673; doi: https://doi.org/10.1101/2023.09.11.556673
