 # Term Project : Genomic language model을 사용해서 Clostridium의 unknown protein의 function 및 alcohol production에 관여하는 enzyme의 chain specific 예측
***
## Seminar (ysoh-0514)
- Seminar: [**Shedding light on functional dark matter with genomic language modeling**](https://youtu.be/G01tGkcw-OA?si=lvekBZHEcXCBApY8)  
- Paper: [Genomic language model predicts protein co-regulation and function](https://www.nature.com/articles/s41467-024-46947-9)
- In class: [presentation](https://docs.google.com/presentation/d/1sF-S-429DUhPfFoTV15OXIbcB2kLGqsV/edit?usp=sharing&ouid=107177185030271497727&rtpof=true&sd=true)
***
## Overview
<pre><code>
<span style="color: #5e91ff">[gLM]</span>
1. 원하는 부분의 gene contig file을 준비한다.   
   (15 - 30개 / seminar에서는 30개로 training 시킴)
2. Colab 또는 Anaconda를 통해 환경 설정을 해준 뒤, data를 input한다.
3. embedding 값을 얻고 이를 inference하여 수치화시킨다.
4. target하는 gene과 주변 gene의 거리를 통해 기능적으로 유사할지 예측한다.


<span style="color: #5e91ff">[Docking simulation]</span>
1. target하는 gene를 Alphafold2를 사용해서 structure를 얻는다.
2. 해당 gene과 아미노산 서열 유사도가 높은 reference gene을 selection하여 보조인자의 위치를 확인할 수 있게 한다.
3. Anaconda에서 receptor와 ligand를 지정하고, vina를 통해 docking affinity를 확인한다.
4. affinity를 PyMOL에서 시각화하여 active site에 붙는지 확인한다. 

</code></pre>

## 1. gLM 구동
### 1-1. Input data 생성
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


### 1-3. Data input
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

## 2. Chain specific 예측
>gLM만으로 chain specific을 예측하기 어려움.   
 따라서 Alphafold2로 structure를 예측한 다음, vina 및 PyMOL를 사용하여 C6 acid를 docking 해보고자 함.

### 2-1. Reference gene 

- target gene은 Protein Data Bank(PDB)에 data가 없기 때문에 Alphafold2로 structure를 예측해야한다. 그러나 Alphafold2를 통해 W 또는 Mo와 같은 보조인자는 알 수 없기 때문에 해당 gene과 amino acid similiarity가 높은 _Clostridium autoethanogenum_ 의 sequence를 reference로 사용한다.
- PDB에서 reference sequence를 다운로드 받는다. (PDBx/mmCIF Format , .cif 형식)


### 2-2. Target gene Structure 준비 (Alphafold2)
- google colab에서 'ColabFold AlphaFold2_mmseqs2'을 검색하여 Alphafold2 실행
- 'query_sequence' 칸에 target하는 amino acid sequence 붙여넣기
- .pdb 파일이 자동 다운로드되면 성공

### 2-3. Docking 환경 구축 
<pre><code>
<span style="color: #008000"># 도킹 전용 환경 만들기</span>
conda create -n docking python=3.9 -y
conda activate docking

<span style="color: #008000"># 핵심 도구</span>
conda install -c conda-forge openbabel -y      <span style="color: #008000"># 리간드 3D 변환</span>
pip install meeko                              <span style="color: #008000"># vina용 파일 준비
</span>
</code></pre>
- AutoDock Vina: https://github.com/ccsb-scripps/AutoDock-Vina/releases 에서 실행파일 받기
- PyMOL :  https://pymol.org 에서 다운로드

### 2-4. Receptor 준비
- PyMOL에서 진행한다.
  - solvent 제거
  - h added
- 해당 파일을 .pdb로 저장 → 00114.pdb
- Vina용 형식(.pdbqt)으로 변환
<Pre><code>prepare_receptor -r aor.pdb -o aor.pdbqt</code></Pre>

### 2-5. Ligand 준비
<pre><code>
<span style="color: #008000"># acetic acid</span>
obabel -:"CC(=O)O" -O acetic_acid.pdbqt --gen3d

<span style="color: #008000"># butyric acid</span>
obabel -:"CCCC(=O)O" -O butanoic_acid.pdbqt --gen3d

<span style="color: #008000"># hexanoic acid</span>
obabel -:"CCCCCC(=O)O" -O hexanoic_acid.pdbqt --gen3d

</code></pre>

- 더 긴 사슬을 넣어서 어디부터 docking이 안되는지 확인할 수 있다.

<pre><code>
<span style="color: #008000"># acetic acid</span>
vina.exe --receptor aor.pdbqt --ligand acetic_acid.pdbqt --center_x 16.772 --center_y 26.895 --center_z 24.908 --size_x 22 --size_y 22 --size_z 22 --exhaustiveness 16 --out acetic_out.pdbqt > acetic_log.txt
type acetic_log.txt

<span style="color: #008000"># butyric acid</span>
vina.exe --receptor aor.pdbqt --ligand butanoic_acid.pdbqt --center_x 16.772 --center_y 26.895 --center_z 24.908 --size_x 22 --size_y 22 --size_z 22 --exhaustiveness 16 --out butanoic_out.pdbqt > butanoic_log.txt
type butanoic_log.txt

<span style="color: #008000"># hexanoic acid</span>
vina.exe --receptor aor.pdbqt --ligand hexanoic_acid.pdbqt --center_x 16.772 --center_y 26.895 --center_z 24.908 --size_x 22 --size_y 22 --size_z 22 --exhaustiveness 16 --out hexanoic_out.pdbqt > hexanoic_log.txt
type hexanoic_log.txt

</code></pre>
- 각 chain 별로 affinity 값을 얻을 수 있고, PyMOL에서 구조를 시각화하여 ligand가 어디에 붙는지 확인한다.
<pre><code>load C:/docking/acetic_out.pdbqt, c2pose
load C:/docking/hexanoic_out.pdbqt, c6pose
show spheres, ref and elem W
color orange, ref and elem W
show sticks, c2pose
show sticks, c6pose
zoom ref and elem W, 15</code></pre>


## 3. Result
### 3-1. gLM 
- strategy 1. Hypothetical protein
> RNA sequencing을 바탕으로 특이적으로 발현량이 높거나 낮은 hypothetical protein을 선별함.    
cluster 안에 여러 개의 hypothetical protein이 존재하는 경우 및 hypothetical protein 수가 많아서 각 경우 별로 1가지의 예시만 올렸음.


- strategy 2) Aldehyde ferredoxin oxidoreductase
> 주변 genomic context 정보를 가지고 해당 gene의 기질 특이성을 확인하고자 했음.

### 3-2. Docking simulation
- acetic acid affinity
![alt text](image-8.png)
![alt text](image-5.png)

- butyric acid affinity
![alt text](image-9.png)
![alt text](image-6.png)
- hexanoic acid affinity
![Fig. 3](image.png)
![alt text](image-7.png)

![alt text](image-4.png)
- C2, C4, C6가 active site에 docking 된다. chain이 증가하면서 affinity도 증가하는 것을 확인하여 simulation이 잘 이루어졌다. 
- hexanoic acid도 docking 되면서 affinity가 증가하는 것으로 보아 C6에도 working 할 것으로 예상한다. 
- octanoic acid도 docking 되는 결과가 있어 어떤 carbon chain 1개의 특이성을 갖는 enzyme은 아닐 수도 있다는 결론이다.


## 4. Conclusion & Discussion




