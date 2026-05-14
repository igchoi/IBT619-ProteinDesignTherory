# Seminar
- Seminar: [**Shedding light on functional dark matter with genomic language modeling**](https://youtu.be/G01tGkcw-OA?si=lvekBZHEcXCBApY8)  
- Paper: [Genomic language model predicts protein co-regulation and function](https://www.nature.com/articles/s41467-024-46947-9)
- In class: [presentation](https://docs.google.com/presentation/d/1sF-S-429DUhPfFoTV15OXIbcB2kLGqsV/edit?usp=sharing&ouid=107177185030271497727&rtpof=true&sd=true)


## 1. Summary

- Question: Can we use high throughput method to accelerate sequence-to-function prediction?
- Algorithms: This approach uses a genomic language model trained on metagenomic gene neighborhoods to infer the functions of uncharacterized genes.


## 2. Speaker
### [Yunha Hwang](https://www.yunhahwang.com/)
- research interests
  - Machine learning approaches to discover and design microbial biochemistry.
  - Modeling and interpreting mechanisms of microbial evolution, ecology and function.
  - Microbial applications for human and environmental health.
- career
  - B.S. in Computer Science from Stanford University
  - Ph.D. in Biology from Harvard University
  - Assistant Professor at MIT with a shared appointment between Biology, EECS and the Schwarzman College of Computing
  - [Tatta Bio](https://www.tatta.bio/)의 co-founder (Tatta Bio is a scientific non-profit dedicated to advancing artificial intelligence models and tools to accelerate biology research.)


## 3. Reference
- [Cornman, Andre, et al. "The OMG dataset: An Open MetaGenomic corpus for mixed-modality genomic language modeling." bioRxiv (2024): 2024-08.](https://www.biorxiv.org/content/10.1101/2024.08.14.607850v2.abstract) (genomic language model v2)
- [Devlin, Jacob, et al. "Bert: Pre-training of deep bidirectional transformers for language understanding." Proceedings of the 2019 conference of the North American chapter of the association for computational linguistics: human language technologies, volume 1 (long and short papers). 2019.](https://doi.org/10.18653/v1/N19-1423) (BERT)
- [Lin,Z.et al.Evolutionary-scale prediction of atomic-level protein structure with a language model. Science 379, 1123–1130 (2023).](https://www.science.org/doi/abs/10.1126/science.ade2574) (ESM2 pLM)
- [ Richardson, L. et al. MGnify: the microbiome sequence data analysis resource in 2023. Nucleic Acids Res 51, D753–D759 (2023)](https://academic.oup.com/nar/article/51/D1/D753/6880769?login=false&guestAccessKey=) (MGnify)


## 4. Tool
- [gLM](https://github.com/y-hwang/gLM)
  - training and inference code and analysis scripts
- [ESM Atlas](https://esmatlas.com/)
  - MGYP database using Foldseek
- [EBI](https://www.ebi.ac.uk/)
  - Metagenome sequence data analysis and search platform operated by EBI
- [MGnify server](http://ftp.ebi.ac.uk/pub/databases/metagenomics/peptide_database/2022_05/)
  - Dataset used for training
 

## 5. Q&As in the seminar
### [Q&A list](https://docs.google.com/document/d/1UYl-66FOLdlaX3i3L-27DizRlUGf91UCsnAuk9G5qQY/edit?usp=sharing)

**Key Questions**
- **Q1. contextualization 결과를 보면 훨씬 더 좋은 성능을 보이는데, substrate를 하나에서 다른 하나로 옮기는 big enzyme machine과 같은 것인가요? (14m 10s)**
  - A1. 더 좋은 성능을 보이는 enzyme들은 conserved context를 가지고, 보통 생합성 경로의 일부이거나 specific partner가 있어 해당 partner gene 옆에서 발견되는 경우도 있습니다. 이러한 이유들로 contextualization이 성능 향상에 큰 도움이 되었습니다.

- **Q2. data set이 bacteria에 편향되어 있는 거 같은데, eukaryotic genome으로 transfer가 가능한가요? (20m 58s)**
  - A2. metagenome은 거의 대부분 microbial genomes에 초점을 맞추고 있으며, life는 연결되어 있으니 homolog가 있을 것이고 microbial genome을 잘 이해한다면 transfer가 가능할 것으로 봅니다.

- **Q3. genome 내에서 gene의 위치나 주변 환경이 고정되어있지 않고 다양할텐데 model이 어떻게 해석하나요? (23m 4s)**
  - A3. transposon 같은 gene은 random한 위치에서 발견됩니다. 따라서 동일한 gene이 서로 다른 context에 있을 때, model이 생성하는 contextualized embedding을 비교합니다. gene의 function이 context에 의존적이면 embedding 값이 크게 변할 것입니다.


## 6. Classmate Questions

`SWKim`: gLM2 considered both coding sequences and integenic sequences simultaneously. However, in gLM2, the coding sequences were not encoded at the gene level using ESM, but rather at amino acid level resolution. Why do you think the authors chose this approach? Also, if a multimodel AI such as ESM3, which simultaneously considers sequence-structure-function were used, would it be possible to achieve much better results?

`MJBaek`: When predicting operons, it seems that the model can predict operons relatively well in regions adjacent to known proteins, both upstream and downstream, but not much beyond that. What is the approximate range of operon prediction that can be achieved in a single run? Also, would it be possible to broaden the prediction range by using the newly predicted proteins as known inputs and then predicting neighboring proteins again iteratively?

`KHNam`:  How the model handles an incorrect 'gene context' that can be created when DNA from different species gets mixed during the metagenome assembly process. Can gLM recognize such contexts as outliers and correct for them, or does it instead accept them and potentially predict incorrect functions? Alternatively, is the impact of this type of noise on the model’s final prediction performance generally negligible?

`DHKim`: If sequence have low similarity but appear in similar genomic contexts, how does gLM interpret them? Can it infer similar functional roles or pathway associations based mainly on genomic context? 

`MsAn`:  What is the statistical mechanism by which gLM2 disentangles 'functional coupling' within the genome from mere 'evolutionary hitchhiking'? Specifically, what are the key metrics utilized during the weight allocation process to mitigate false positives



