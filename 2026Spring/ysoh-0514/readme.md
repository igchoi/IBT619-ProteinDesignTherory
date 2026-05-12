# Seminar
- Seminar: [**Shedding light on functional dark matter with genomic language modeling**](https://youtu.be/G01tGkcw-OA?si=lvekBZHEcXCBApY8)  
- Paper: [Genomic language model predicts protein co-regulation and function](https://www.nature.com/articles/s41467-024-46947-9)
- In class: [presentation]()


## 1. Summary

- Question: Can we use high throughput method to accelerate sequence-to-function prediction?
- Algorithms: 


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


## 3. Reference



## 4. Tool
- [gLM](https://github.com/y-hwang/gLM)
- [Data set](http://ftp.ebi.ac.uk/pub/databases/metagenomics/peptide_database/2022_05/)
- [ESM Atlas](https://esmatlas.com/)

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

`SWKim`: 

`MJBaek`:

`KHNam`:  

`DHKim`:  

`MSAn`:  



