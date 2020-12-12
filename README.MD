# Hocor2020 - Graph DB Sample

---

## Description

本專案為針對Hocor2020的分享-裁判書的深度解析-從裁判書到知識圖譜

運用到Knowledge Graph的技術，針對裁判書進行解析並且期望建構一個法律上的專家圖譜。

建構Knowledge Grpah必須要有一個儲存的基礎，因此本sample透過neo4j，簡單demo如何針對一個基本語料，進行知識萃取，存到GraphDB後，透過query去達成後續用途


## Environment

* python3.6
* neo4j
* docker(optional)

## Packages

* py2neo
* jieba


## Process

1. 首先必須先準備neo4j的環境，這邊可以選擇兩種做法：
    1. 直接本機安裝neo4j相關環境
    2. 透過docker建立container啟動neo4j環境
    
2. 準備好想要抽取的語料對象，這邊可以泛指各種文本

3. 針對文本進行不同的處理(POS CUT、NER、Denpendency Parser......)，這些處理的最終目的，是要解析出你所需要的資訊，並且根據這些資訊建構你的Knowledge Graph

4. 將解析過的Knowledge，建構在neo4j上

5. 加值應用(問答、Chatbot、搜尋引擎......)


## Demo

1. 下載專案

<pre>git clone https://github.com/aron3312/GraphDB_sample</pre>

2. CMD操作，安裝必要的套件；打開jupyternotebook

<pre>cd GraphDB_sample
pip install -r requirements.txt
cd judgement_sample
jupyter notebook
</pre>

3. 點開 extract_knowledge.ipynb

4. 跟著上面的cell去執行



