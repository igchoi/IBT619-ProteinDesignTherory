# Seminar
- Seminar: [**RNA Function, Design, and Modeling**](https://youtu.be/oS_Cb-YMymw?si=DlrBkbfoxmlEGLer)  
- Paper: [**Diverse database and machine learning model to narrow the generalization gap in RNA structure prediction**](https://www.science.org/doi/10.1126/sciadv.adz4967)  
- Presentation: [)  

## 1. Summary
- Question: Can AI modeling be used to predict the complex structure of RNA and design gene expression freely controllable?  
- Algorithms: **eFold** is an architecture for RNA secondary structure prediction. It utilizes DMS-MaPseq to learn complex long-distance interactions within sequences. Integrating single-molecule EM clustering separately separates and captures multiple coexisting alternative structural ensembles, enabling high-resolution analysis and precise design of functional RNAs such as IRES and riboswitches.

## 2. Speaker
### [Silvi rouskin](https://www.rouskinlab.com/)
DMS-seq developer | A Study on the Structure of Viral RNA
- **History**
  - Ph.D : 2009 ~ 2014, University of California, San Francisco
  - Fellow : 2015 ~ 2021, Whitehead Institute for Biomedical Research
- **Affiliation:**
  - Assistant Professor : 2021 ~ Present, Harvard Medical Microbiology

## 3. Related Literatures/Reference
- [Genome-wide probing of RNA structure reveals active unfolding of mRNA structures in vivo (2013)](https://www.nature.com/articles/nature12894#citeas)
- [DMS-MaPseq for genome-wide or targeted RNA structure probing in vivo (2016)](https://www.nature.com/articles/nmeth.4057)
- [Highly accurate protein structure prediction with AlphaFold (2021)](https://www.nature.com/articles/s41586-021-03819-2)
- [UFold: fast and accurate RNA secondary structure prediction with deep learning (2022)](https://academic.oup.com/nar/article/50/3/e14/6430845)
- [Secondary structural ensembles of the SARS-CoV-2 RNA genome in infected cells (2022)](https://www.nature.com/articles/s41467-022-28603-2)

## 4. Tool
**1. EM Clustering - SEISMIC-RNA (Data Isolation)**
   - [Github](https://github.com/rouskinlab/seismic-rna)

**2. eFold (RNA structure prediction)**
   - [Github](https://github.com/rouskinlab/eFold)

## 5. Key Q&As in the seminar
**Q1. 리보스위치 스크리닝이 실제 세포 내에서도 같은 결과가 나오는가?**
**A. 세포 내에서는 대사 물질의 농도를 정밀하게 조절하기 매우 어려워 같은 결과가 나오기 어렵다.**

**Q2. 특정 조직에서만 IRES가 활성화 되는 구체적인 원인이 무엇인가?**
**A. ITAF(IRES Activating Trans Factors)가 핵심 단백질로, 특정 조직에서 많이 발현되어 RNA가 접히도록 돕는것으로 보임.**

**Q3. RNA 구조가 매우 빠르게 변할텐데, DMS 탐 Seminar
- Seminar: [**RNA Function, Design, and Modeling**](https://youtu.be/oS_Cb-YMymw?si=DlrBkbfoxmlEGLer)  
- Paper: [**Diverse database and machine learning model to narrow the generalization gap in RNA structure prediction**](https://www.science.org/doi/10.1126/sciadv.adz4967)  
- Presentation: [)  

## 1. Summary
- Question: Can AI modeling be used to predict the complex structure of RNA and design gene expression freely controllable?  
- Algorithms: **eFold** is an architecture for RNA secondary structure prediction. It utilizes DMS-MaPseq to learn complex long-distance interactions within sequences. Integrating single-molecule EM clustering separately separates and captures multiple coexisting alternative structural ensembles, enabling high-resolution analysis and precise design of functional RNAs such as IRES and riboswitches.

## 2. Speaker
### [Silvi rouskin](https://www.rouskinlab.com/)
DMS-seq developer | A Study on the Structure of Viral RNA
- **History**
  - Ph.D : 2009 ~ 2014, University of California, San Francisco
  - Fellow : 2015 ~ 2021, Whitehead Institute for Biomedical Research
- **Affiliation:**
  - Assistant Professor : 2021 ~ Present, Harvard Medical Microbiology

## 3. Related Literatures/Reference
- [Genome-wide probing of RNA structure reveals active unfolding of mRNA structures in vivo (2013)](https://www.nature.com/articles/nature12894#citeas)
- [DMS-MaPseq for genome-wide or targeted RNA structure probing in vivo (2016)](https://www.nature.com/articles/nmeth.4057)
- [Highly accurate protein structure prediction with AlphaFold (2021)](https://www.nature.com/articles/s41586-021-03819-2)
- [UFold: fast and accurate RNA secondary structure prediction with deep learning (2022)](https://academic.oup.com/nar/article/50/3/e14/6430845)
- [Secondary structural ensembles of the SARS-CoV-2 RNA genome in infected cells (2022)](https://www.nature.com/articles/s41467-022-28603-2)

## 4. Tool
**1. EM Clustering - SEISMIC-RNA (Data Isolation)**
   - [Github](https://github.com/rouskinlab/seismic-rna)

**2. eFold (RNA structure prediction)**
   - [Github](https://github.com/rouskinlab/eFold)

## 5. Key Q&As in the seminar
  **Q1. 리보스위치 스크리닝이 실제 세포 내에서도 같은 결과가 나오는가?**
  -**A. 세포 내에서는 대사 물질의 농도를 정밀하게 조절하기 매우 어려워 같은 결과가 나오기 어렵다.**


  **Q2. RNA 구조가 매우 빠르게 변할텐데, DMS-MaPseq으로 순간 포착이 가능한가?**
  -**A. 2차 구조는 대체적으로 안정적임. 다른 구조로 변하려면 염기쌍을 끊어야해 에너지가 많이 필요하고 그만큼 느림. 때문에 DMS-MaPseq으로 안적적인 상태를 포착 가능.**


  **Q3. RNA 특정 부위를 조금 바꾸면 영향이 국소적인가 전체적인가?**
  -**A. 국소적 변이는 해당 부위에만 영향을 미치나, 드물게 전체 구조 재배열을 일으키기도 함.**


  **Q4. eFold 예측 실패는 어떤 경향으로 나타나는가?(다른 대안 구조를 예측하는지)**
  -**A. 데이터가 부족해 통계적인 데이터로 말하기는 어려움. 완전히 틀린 구조가 나오기도 하는 반면, 실제 존재하는 다른 구조를 찾아내기도 함.**

## 6. Classmate Questions
`SWKim`: 

`YSOh`: 

`MJBaek`: 

`KHNam`: 

`MSAn`: 
