 # Term Project : Genomic language model을 사용해서 Clostridium의 unknown protein의 function 및 alcohol production에 관여하는 enzyme의 chain specific 예측
***
## Seminar (ysoh-0514)
- Seminar: [**Shedding light on functional dark matter with genomic language modeling**](https://youtu.be/G01tGkcw-OA?si=lvekBZHEcXCBApY8)  
- Paper: [Genomic language model predicts protein co-regulation and function](https://www.nature.com/articles/s41467-024-46947-9)
- In class: [presentation](https://docs.google.com/presentation/d/1sF-S-429DUhPfFoTV15OXIbcB2kLGqsV/edit?usp=sharing&ouid=107177185030271497727&rtpof=true&sd=true)
***

## 1. gLM 구동
### 1-1. Anaconda environment 설정
<pre><code>{code}</code></pre>


### 1-2.
<pre><code>{code}</code></pre>


### 1-3. fasta file 및 sequence direction file 준비
<pre><code>{code}</code></pre>

## 2. chain specific 예측
>gLM만으로 chain specific을 예측하기 어려움. 따라서 Alphafold2로 structure를 예측한 다음, vina를 사용하여 C6 acid를 docking 해보고자 함.

2-1. Structure 준비 (with Alphafold2)
<pre><code>{code}</code></pre>


2-2. 
<pre><code>{code}</code></pre>


## 3. Conclusion & Discussion




