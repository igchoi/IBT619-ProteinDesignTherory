# Agentic in-silico directed evolution: an LLM-orchestrated, stability-guided mutational diffusion of protein sequences


## 1. Research Question

Does **property-guided, protein sequence context-aware diffusion models** can propose plausible mutations for higher stability for ESM3 generated de novo protein?


## 2. Background and Motivation

### Gene design with generative genomic language models

Evo 1/Evo 2와 같은 genomic language model은 attention mechanism을 활용해서 자연어의 맥락을 이해할 수 있도록 하는 large language model (LLM)의 한 종류로, 자연어 대신 genomic sequence를 학습한 모델이다 [1-2]. 

| Model | Parameters | Training Data |
| --- | --- | --- |
|Evo 1| 7B | Bacteria, Archaea, and Virus (Phage); **OpenGenome**|
|Evo 2| 1B, 7B, 20B, 40B| All domains of life; **OpenGenome2**| 

![](https://github.com/igchoi/IBT619-ProteinDesignTherory/blob/main/2026Spring/swkim-0604/in-context%20gene%20generation%20with%20Evo2.png)

Evo 1의 모델 구조를 동일하게 유지한 채로, 학습을 조금 1.5배 오래하여 만든 Evo 1.5 모델은, 특정한 target gene 주위의 genomic context를 고려해서 highly conserved gene들과 동일한 function을 가지지만 서열이 다른 gene을 생성할 수 있다 [3]. 또한 genetic context가 어느정도 유지되어 있는 system의 경우 (e.g. bacteria toxin-antitoxin system, viral anti-CRISPR system) 본질적으로 다양성이 높은 gene이라도 Evo 1.5 모델이 functional gene을 생성할 수 있다 [3]. 


### Protein design with generative protein language models

ESM3와 같은 protein language model 역시 attention mechanism을 활용하고, 자연어 대신 protein sequence, structure, function을 동시에 학습한 multi-modal language model이다 [4]. 

![](https://github.com/igchoi/IBT619-ProteinDesignTherory/blob/main/2026Spring/swkim-0604/protein%20generation%20with%20ESM3.png)

ESM3 논문에서 보여준 위의 GFP의 에시와 같이, ESM3 모델은 특정한 기능의 active site를 비롯한 핵심적인 부위의 서열과 구조 정보만을 input으로 넣어주면, 나머지 부분을 생성할 수 있다. 논문의 저자들은 약 80,000개의 design를 computational filtering functions 및 experimental testing을 통해 natural GFP와 동등한 fluorescence를 가지지만 서열 유사도가 57% 수준인 de novo GFP를 만들어냈다 [4]. 추가로 ESM3 모델은 scaffolding 등에도 활용될 수 있다. **ESM3는 단백질의 서열-구조-기능을 동시에 학습하여 높은 성능을 보이지만, functional하고 안정화된 하나의 de novo protein을 얻는 데에는 많은 computational resources와 exprimental validation을 동반한 검증 루프가 여러 번 필요하다**.  

### Property-guided, protein sequence context-aware design with generative diffusion models  

최근의 AI 분야의 동향이 foundation AI 모델의 추론 시간을 늘리는 것만으로 (즉, sampling을 많이 하는 것) 성능을 계속해서 높일 수 있다는 것인데, 이러한 접근은 일반적이고 넓은 문제에는 적합하지만, 특정한 목적과 제한된 문제에 해당하는 protein target의 개별 디자인에는 비효율적일 수 있다. 따라서 본 프로젝트에서는 activate site로부터 나머지 protein sequence를 생성해주는 ESM3의 결과 서열을 활용하여, 샘플링된 sequence의 biophysical or biochemical property를 높여줄 수 있는 mutation을 제안하는 diffusion model을 개발하고자 한다. 

ESM3 모델의 architecture를 활용하여 처음부터 학습을 수행하거나, open source 모델을 fine-tuning하는 방향도 가능하지만, 전체 모델을 비교적 값싸고 빠르게 테스트해 볼 수 있는 상대적으로 작은 모델인 diffusion model을 활용해보기로 하였다. 특별히 단백질의 서열만을 이용해서 만든 diffusion model인 EvoDiff 모델의 architecture를 활용하기로 결정하였다 [5]. 

![](https://github.com/igchoi/IBT619-ProteinDesignTherory/blob/main/2026Spring/swkim-0604/EvoDiff%20style%20diffusion%20scheme.png)  

EvoDiff 논문에서 학습시킨 모델의 파라미터는 각각 38M과 640M으로, 38M의 경우 google colab에서도 학습이 가능한 수준으로 생각된다. 

## 3. Computational Strategy

### 3.1 Pipeline overview

Target 선정에 앞서, 최종적으로 설계한 pipeline은 다음과 같다. 

1) ESM3로 active site를 input으로 주어 protein sequence을 생성한다.
2) 생성한 서열들을 기본적인 biophysical property score로 filtering 한다.
3) Filtering한 서열들과 원하는 property (e.g. thermostability) 를 EvoDiff style diffusion model에 input으로 넣어주고, 모델이 제안하는 property-guided mutation을 output으로 받는다. 
4) Agentic AI를 활용하여 제안된 mutation을 protein sequence에 분석 후 선별하여 적용하고, 결과를 평가한다. 다시 3)으로 돌아가 반복한다. 

```
# Agentic Loop

Input: ESM3 generated protein sequence + desired property (e.g. thermostability)

   ↓

1. Diffusion Model: Desired property를 만들 수 있는 mutations 제안

   ↓

2. Scoring: dG, pLDDT, etc. 계산

   ↓

3. LLM Agent: UniProt/Papers (PubMed search plugin)를 활용하여 design에 대한 제약, 효용 분석 (with documentation of reasoning)

   ↓

4. Re-design: LLM Agent가 최종 선택한 mutation들을 protein sequence에 적용하고, 다시 1.로 돌아가 반복
```

### 3.2 Diffusion model architecture

| Model | Parameters | Layers | Hidden Dim | Heads |
|---|---|---|---|---|
| EvoDiff (original, small) | 38M | 6 | 512 | 8 |
| EvoDiff (original, large) | 640M | 33 | 1280 | 20 |
| **Ours** | **~640M–1B (target)** | **40–48 (extended)** | **1280** | **20** |

EvoDiff 논문에서 학습시킨 모델의 파라미터는 각각 38M과 640M으로 최신 모델들에 비하면 작은 편이다. State-of-the-art 모델들에 견줄 수 있는 protein design을 하기 위해서는 모델이 조금 더 클 필요가 있다고 생각되므로, 모델의 layers를 40-48로 늘려 테스트를 해볼 계획이다. Hidden dimension과 attention heads 역시 조금 더 확장해볼 수 있을 것이다. 


### 3.3 Training dataset

| Dataset | Content | Objective | Link |
|---|---|---|---|
|Tsuboyama 2023 mega-scale | every single mutation and selected double mutation data of 331 natural + 148 de novo domain (~776,000 folding stability data) | main training set (folding stability) | [Mega-scale experimental analysis of protein folding stability in biology and design (Nature, 2023)](https://www.nature.com/articles/s41586-023-06328-6#Sec10) |
|FireProtDB (2.0) | Manually curated stability data of single mutation and insertion/deletion/multi-mutation | complementary training set (stability) | [FireProtDB 2.0: large-scale manually curated database of the protein stability data (Nucleic Acids Research, 2026)](https://academic.oup.com/nar/article/54/D1/D409/8329105) |
|ProteinGym | 217 deep mutational scanning dataset, ~2.7M single mutation data | complementary training set | [ProteinGym](https://proteingym.org/) |


## 4. Design target

설계한 diffusion model과 agentic loop가 작동하는 것을 확인하기 위해서 가장 쉬운 예시를 생각하였고, 화학 반응을 통해 노란색을 띄는 **photoactive yellow protein (PYP)** 라는 단백질을 design target으로 선정하였다. 추후 모델과 pipeline이 생성한 서열을 spectrophotometry 등으로 쉽게 검증할 수 있으므로, 실험적으로 검증할 계획이다. 

#### Benchmarking

| Model | Modality | Evaluation 방법 |
|---|---|---|
| **Ours** | ESM3 + Diffusion + Agentic AI | 실험적 검증 |
| **ESM3-only** | ESM3 | ESM3에서 esmGFP를 생성한 파이프라인 참고 후 실험적 검증 |

## 5. Expected timeline

| Week | Task |
|:---:|---|
| 1-2 | Dataset collection and preprocessing |
| 3-4 | Diffusion model architecture design and implementation, PYP design with ESM3 |
| 5-6 | Training diffusion model, generating mutations for ESM3-generated PYP |
| 7-8 | Agentic loop implementation and testing |
| 9-10 | Experimental validation of designed PYP variants |

## 6. Novelty & Limitations

**Novelty**: 
- 단백질 optimization 또는 redisign 문제에서 masking을 사용하지 않고, 전체 서열을 고려한 채로 mutation을 제안하는 D3PM을 활용하는 diffusion model을 설계한다는 점에서 novelty가 있다. 이는 단백질 서열 수준에서 context를 고려해서 특정한 property 방향으로의 mutation을 제안하는 모델이라는 점에서 특이하다. 
- 본 프로젝트에서는 시간이 많이 소요되고, 병목이 되는 mutation selection 과정에 Agentic AI를 접목하여, 자동화된 pipeline에서 계속해서 mutation을 통한 protein evolution이 in silico에서 일어날 수 있도록 설계하였다. 

**Limitations**:
- 학습 데이터셋에서 가장 큰 부분을 차지하는 Tsuboyama 2023 mega-scale dataset은 40-72 a.a. 수준의 짧은 도메인 위주이므로 큰 단백질이나 multi-domain이 필요한 epistasis를 고려한 design에는 한계가 존재한다. 
- 현재의 적용은 stability 또는 thermostability에 초점을 두고 있으므로, 추후 다른 property나 function에 대한 확장이 필요하다. 

## 7. Reference

**[1]** Eric Nguyen et al. ,Sequence modeling and design from molecular to genome scale with Evo.Science386,eado9336(2024).DOI:10.1126/science.ado9336  
**[2]** Brixi, G., Durrant, M.G., Ku, J. et al. Genome modelling and design across all domains of life with Evo 2. Nature 652, 1349–1361 (2026). https://doi.org/10.1038/s41586-026-10176-5  
**[3]** Merchant, A.T., King, S.H., Nguyen, E. et al. Semantic design of functional de novo genes from a genomic language model. Nature 649, 749–758 (2026). https://doi.org/10.1038/s41586-025-09749-7  
**[4]** Thomas Hayes et al. ,Simulating 500 million years of evolution with a language model.Science387,850-858(2025).DOI:10.1126/science.ads0018  
**[5]** Sarah Alamdari, Nitya Thakkar, Rianne van den Berg, Neil Tenenholtz, Robert Strome, Alan M. Moses, Alex X. Lu, Nicolò Fusi, Ava P. Amini, Kevin K. Yang
bioRxiv 2023.09.11.556673; doi: https://doi.org/10.1101/2023.09.11.556673
