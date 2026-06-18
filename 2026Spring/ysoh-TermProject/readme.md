 # Term Project : Genomic language model을 사용해서 Clostridium의 unknown protein의 function 및 alcohol production에 관여하는 enzyme의 chain specific 예측
***
## Seminar (ysoh-0514)
- Seminar: [**Shedding light on functional dark matter with genomic language modeling**](https://youtu.be/G01tGkcw-OA?si=lvekBZHEcXCBApY8)  
- Paper: [Genomic language model predicts protein co-regulation and function](https://www.nature.com/articles/s41467-024-46947-9)
- In class: [presentation](https://docs.google.com/presentation/d/1sF-S-429DUhPfFoTV15OXIbcB2kLGqsV/edit?usp=sharing&ouid=107177185030271497727&rtpof=true&sd=true)
***

## 1. gLM 구동
### 1-1. input data 생성
<pre><code>2가지의 contig file 생성

1. sequence fasta file (.fa) : target하는 gene 앞 뒤로 7개의 gene (total 15개)

2. sequence direction file (.tsv) : 각 gene의 방향을 +, -로 설정
ex) contig_00114	+RS13210;+RS13215;+RS13220;+RS13225--- 
</code></pre>
- contig_00114 입력 후 'tab'으로 구분해준다.
- direction file 생성할 때, 마지막 gene 뒤에는 ; 을 붙이지 않는다. 
- fasta file과 direction file의 gene name이 동일한지 확인한다.
### 1-2. Environment 설정 (Google colab)
<pre><code>
!nvidia-smi
!git clone https://github.com/y-hwang/gLM 
!pip install fair-esm fairscale -q
print("=== 설치 완료 ===")

-------------------------------------------

<span style="color: #008000"># colab에 맞는 transformation 호환</span>

path = '/content/gLM/gLM/gLM.py'
with open(path) as f:
    code = f.read()
code = code.replace(
    'self.update_keys_to_ignore(config, ["lm_head.decoder.weight"])',
    '# self.update_keys_to_ignore(config, ["lm_head.decoder.weight"])  # 호환성 수정'
)
with open(path, 'w') as f:
    f.write(code)
print("=== gLM.py 수정 완료 ===")

-------------------------------------------

<span style="color: #008000"># download 하는데 30 m 소요</span>

!mkdir -p /content/gLM/model
!wget -q -O /content/gLM/model/glm.bin https://zenodo.org/record/7855545/files/glm.bin
!ls -lh /content/gLM/model/glm.bin

</code></pre>
- linux 또는 Anaconda로 사용하는 방법이 불필요한 errors를 줄일 수 있다.   
 (data download의 소요 시간이 bottleneck이어서 colab으로 사용했음)


### 1-3. data input
<pre><code>
from google.colab import files
print("my_gene_00114.fa 와 my_contig_00114.tsv 두 파일을 선택하세요")
uploaded = files.upload()

</code></pre>

- step 1-1에서 생성한 fa, tsv 파일을 업로드 한다.

### 1-3. Embedding 값 출력
<pre><code>
%cd /content/gLM/data
!mkdir -p my_batched_data
!python batch_data.py my_gene_00114.esm.embs.pkl my_contig_00114.tsv my_batched_data
!ls my_batched_data

</code></pre>
- 3번째 줄을 보면 file name이 있어 코드를 사용할 때 file name이 일치하는지 확인한.

## 2. chain specific 예측
>gLM만으로 chain specific을 예측하기 어려움.   
 따라서 Alphafold2로 structure를 예측한 다음, vina 및 PyMOL를 사용하여 C6 acid를 docking 해보고자 함.

### 2-1. reference gene 

- target gene은 Protein Data Bank(PDB)에 data가 없기 없어 Alphafold2로 structure를 예측해야한다. 그러나  해당 gene과 amino acid similiarity가 높은 _Clostridium autoethanogenum_ 의 sequence를 reference로 사용한다.
- PDB에서 reference sequence를 다운로드 받는다. 
- 

### 2-3. target gene Structure 준비 (Alphafold2)
<pre><code>{code}</code></pre>
- google colab에서 'ColabFold AlphaFold2_mmseqs2'을 검색하여 Alphafold2 실행
- 'query_sequence' 칸에 target하는 amino acid sequence 붙여넣기
- .pdb 파일이 자동 다운로드되면 성공

### 2-2. 
<pre><code>{code}</code></pre>


## 3. Conclusion & Discussion




