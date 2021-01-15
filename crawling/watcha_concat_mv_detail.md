```python
import requests
from bs4 import BeautifulSoup
import urllib
import re

import numpy as np
from pandas import DataFrame, Series
import pandas as pd
import glob
from tqdm import tqdm_notebook
```


```python
mv_detail_list=glob.glob('./mv_detail/*')
```


```python
all_df = [pd.read_csv(file, index_col=0) for file in mv_detail_list]
```


```python
concat_df = pd.concat(all_df)
```
```python
concat_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0.5</th>
      <th>1.0</th>
      <th>1.5</th>
      <th>2.0</th>
      <th>2.5</th>
      <th>3.0</th>
      <th>3.5</th>
      <th>4.0</th>
      <th>4.5</th>
      <th>5.0</th>
      <th>...</th>
      <th>원제</th>
      <th>장르</th>
      <th>제작 연도</th>
      <th>조연</th>
      <th>주연</th>
      <th>최고의 인생작을 티빙에서!</th>
      <th>출연</th>
      <th>투표자수</th>
      <th>특별출연</th>
      <th>평점</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mW4L2XW</td>
      <td>0.352</td>
      <td>1.320</td>
      <td>0.440</td>
      <td>2.904</td>
      <td>1.672</td>
      <td>13.904</td>
      <td>9.856</td>
      <td>46.992</td>
      <td>25.608</td>
      <td>88.000</td>
      <td>...</td>
      <td>Inception</td>
      <td>액션/모험/SF/스릴러</td>
      <td>2010.0</td>
      <td>킬리언 머피,톰 베린저</td>
      <td>레오나르도 디카프리오,조셉 고든-레빗,엘렌 페이지,마리옹 꼬띠아르,톰 하디,와타나베 켄</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>97만</td>
      <td>NaN</td>
      <td>4.4</td>
    </tr>
    <tr>
      <td>m53mEDn</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>El crack cero</td>
      <td>스릴러</td>
      <td>2019.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>mWzwxvZ</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>State of exception</td>
      <td>NaN</td>
      <td>2012.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>mWJjpQW</td>
      <td>1.848</td>
      <td>2.640</td>
      <td>2.640</td>
      <td>7.832</td>
      <td>12.760</td>
      <td>41.448</td>
      <td>65.384</td>
      <td>88.000</td>
      <td>39.600</td>
      <td>45.584</td>
      <td>...</td>
      <td>Deadpool</td>
      <td>액션/모험/코미디</td>
      <td>2016.0</td>
      <td>스테판 카피칙,레슬리 우감스</td>
      <td>라이언 레이놀즈,모레나 바카린,에드 스크라인,T.J. 밀러,지나 카라노,브리아나 힐...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35만</td>
      <td>NaN</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td>mWvkxbr</td>
      <td>1.056</td>
      <td>1.232</td>
      <td>2.464</td>
      <td>6.248</td>
      <td>15.048</td>
      <td>47.256</td>
      <td>83.776</td>
      <td>88.000</td>
      <td>36.344</td>
      <td>25.344</td>
      <td>...</td>
      <td>Deadpool 2</td>
      <td>액션/모험/코미디/SF</td>
      <td>2018.0</td>
      <td>브리아나 힐데브란드,T.J. 밀러,빌 스카스가드,스테판 카피칙,테리 크루즈,줄리안 데니슨</td>
      <td>라이언 레이놀즈,조쉬 브롤린</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>14만</td>
      <td>NaN</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>mdR6PQV</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>The All-Out Game</td>
      <td>NaN</td>
      <td>1970.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ミカサスミレ,ナルセアキコ,クダンゴロウ,ホノオサンシロウ,北爪晴茂,ナツカワケイイチ,ヤシ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>mWyaJ91</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>친구누나 일본판 2</td>
      <td>성인</td>
      <td>2018.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>md6oza5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>Letting Go</td>
      <td>로맨스</td>
      <td>1985.0</td>
      <td>피터 드보르스키,마이클 판티니,킷 맥도노프</td>
      <td>존 리터,샤론 글레스,조셉 코르테스,맥스 게일</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>m53VZvy</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>Venere Imperiale</td>
      <td>NaN</td>
      <td>1962.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ジャンニ・サンツッチョ,가브리엘레 페르제티,마시모 지로티,ミシュリーヌ・プレール,レイモ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>mWwA8jl</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>अचानक</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>129653 rows × 30 columns</p>
</div>




```python
concat_df[~concat_df['특별출연'].isnull()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0.5</th>
      <th>1.0</th>
      <th>1.5</th>
      <th>2.0</th>
      <th>2.5</th>
      <th>3.0</th>
      <th>3.5</th>
      <th>4.0</th>
      <th>4.5</th>
      <th>5.0</th>
      <th>...</th>
      <th>원제</th>
      <th>장르</th>
      <th>제작 연도</th>
      <th>조연</th>
      <th>주연</th>
      <th>최고의 인생작을 티빙에서!</th>
      <th>출연</th>
      <th>투표자수</th>
      <th>특별출연</th>
      <th>평점</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>m5DwLBd</td>
      <td>32.032</td>
      <td>54.648</td>
      <td>33.704</td>
      <td>88.000</td>
      <td>41.272</td>
      <td>75.504</td>
      <td>18.480</td>
      <td>15.928</td>
      <td>1.584</td>
      <td>4.576</td>
      <td>...</td>
      <td>Jeni, Juno</td>
      <td>로맨틱코미디/드라마</td>
      <td>2005.0</td>
      <td>이응경,서민정,임동진,김자옥,강남길</td>
      <td>박민지,김혜성</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5만</td>
      <td>안선영</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td>m5YMVR5</td>
      <td>17.160</td>
      <td>37.488</td>
      <td>24.024</td>
      <td>85.360</td>
      <td>50.688</td>
      <td>88.000</td>
      <td>15.752</td>
      <td>13.640</td>
      <td>0.880</td>
      <td>4.840</td>
      <td>...</td>
      <td>The Wife In Romance</td>
      <td>로맨틱코미디</td>
      <td>1999.0</td>
      <td>NaN</td>
      <td>최민수,황신혜,이미연,여균동</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3,048</td>
      <td>신구,김의성,윤현숙,전수경</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td>m5DGo1d</td>
      <td>6.424</td>
      <td>16.632</td>
      <td>10.560</td>
      <td>42.240</td>
      <td>26.400</td>
      <td>88.000</td>
      <td>31.680</td>
      <td>48.928</td>
      <td>4.752</td>
      <td>19.624</td>
      <td>...</td>
      <td>Scary Movie 2</td>
      <td>코미디/공포</td>
      <td>2001.0</td>
      <td>NaN</td>
      <td>캐슬린 로버트슨,데이빗 크로스,숀 웨이언스,말론 웨이언스,안나 페리스,레지나 홀,크...</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>4만</td>
      <td>제임스 우즈</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>mP5m3GO</td>
      <td>1.056</td>
      <td>3.696</td>
      <td>1.408</td>
      <td>9.064</td>
      <td>6.248</td>
      <td>43.208</td>
      <td>40.128</td>
      <td>88.000</td>
      <td>18.040</td>
      <td>24.376</td>
      <td>...</td>
      <td>Misery</td>
      <td>공포/드라마/스릴러</td>
      <td>1990.0</td>
      <td>프란시스 스턴하겐,리처드 판스워드</td>
      <td>제임스 칸,케시 베이츠</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7만</td>
      <td>로렌 바콜</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>mObGARn</td>
      <td>13.200</td>
      <td>23.320</td>
      <td>14.696</td>
      <td>37.136</td>
      <td>53.152</td>
      <td>88.000</td>
      <td>53.416</td>
      <td>35.376</td>
      <td>10.120</td>
      <td>34.056</td>
      <td>...</td>
      <td>RISE OF THE LEGEND</td>
      <td>액션/드라마</td>
      <td>2014.0</td>
      <td>왕조람,바이런 만</td>
      <td>펑위옌,홍금보,왕락단,정백연</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1,895</td>
      <td>양가휘,안젤라 베이비</td>
      <td>2.9</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>mOb41a5</td>
      <td>6.424</td>
      <td>38.808</td>
      <td>15.752</td>
      <td>88.000</td>
      <td>30.976</td>
      <td>70.312</td>
      <td>12.320</td>
      <td>16.720</td>
      <td>0.968</td>
      <td>4.928</td>
      <td>...</td>
      <td>If It Snows On Christmas</td>
      <td>로맨스</td>
      <td>1998.0</td>
      <td>김지영,권오중,김민상</td>
      <td>김현주,박용하</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>580</td>
      <td>조현태</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td>mnOoDmd</td>
      <td>2.024</td>
      <td>12.672</td>
      <td>2.024</td>
      <td>17.600</td>
      <td>10.560</td>
      <td>63.272</td>
      <td>52.360</td>
      <td>88.000</td>
      <td>27.104</td>
      <td>35.992</td>
      <td>...</td>
      <td>Morte a Venezia</td>
      <td>드라마</td>
      <td>1971.0</td>
      <td>로몰로 발리,마크 번즈,노라 리치,마리사 베렌슨,캐롤 앙드레</td>
      <td>더크 보거드,비요른 안드레센</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3,375</td>
      <td>실바나 만가노</td>
      <td>3.5</td>
    </tr>
    <tr>
      <td>m5r3oVJ</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>映画ドラえもん のび太の新恐竜</td>
      <td>애니메이션/모험/판타지</td>
      <td>2020.0</td>
      <td>카카즈 유미,키무라 스바루,세키 토모카즈</td>
      <td>미즈타 와사비,오오하라 메구미</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
      <td>기무라 타쿠야,와타나베 나오미</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>m5nQ2JX</td>
      <td>39.776</td>
      <td>48.224</td>
      <td>67.056</td>
      <td>88.000</td>
      <td>83.776</td>
      <td>81.752</td>
      <td>46.112</td>
      <td>25.168</td>
      <td>6.248</td>
      <td>54.472</td>
      <td>...</td>
      <td>하나식당</td>
      <td>드라마</td>
      <td>2018.0</td>
      <td>유현,최윤희,고유안,니시아키 아이나,히가시온나 루카</td>
      <td>최정원,나혜미</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>263</td>
      <td>오승현</td>
      <td>2.5</td>
    </tr>
    <tr>
      <td>mO8Kz9x</td>
      <td>88.000</td>
      <td>60.368</td>
      <td>52.800</td>
      <td>22.616</td>
      <td>7.568</td>
      <td>17.600</td>
      <td>2.552</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>10.032</td>
      <td>...</td>
      <td>관음증</td>
      <td>성인</td>
      <td>2015.0</td>
      <td>노수람,이기웅</td>
      <td>공대유,이윤선</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>107</td>
      <td>아오이 츠카사</td>
      <td>1.4</td>
    </tr>
  </tbody>
</table>
<p>282 rows × 30 columns</p>
</div>




```python
concat_df[~concat_df['최고의 인생작을 티빙에서!'].isnull()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0.5</th>
      <th>1.0</th>
      <th>1.5</th>
      <th>2.0</th>
      <th>2.5</th>
      <th>3.0</th>
      <th>3.5</th>
      <th>4.0</th>
      <th>4.5</th>
      <th>5.0</th>
      <th>...</th>
      <th>원제</th>
      <th>장르</th>
      <th>제작 연도</th>
      <th>조연</th>
      <th>주연</th>
      <th>최고의 인생작을 티빙에서!</th>
      <th>출연</th>
      <th>투표자수</th>
      <th>특별출연</th>
      <th>평점</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mWvkxbr</td>
      <td>1.056</td>
      <td>1.232</td>
      <td>2.464</td>
      <td>6.248</td>
      <td>15.048</td>
      <td>47.256</td>
      <td>83.776</td>
      <td>88.000</td>
      <td>36.344</td>
      <td>25.344</td>
      <td>...</td>
      <td>Deadpool 2</td>
      <td>액션/모험/코미디/SF</td>
      <td>2018.0</td>
      <td>브리아나 힐데브란드,T.J. 밀러,빌 스카스가드,스테판 카피칙,테리 크루즈,줄리안 데니슨</td>
      <td>라이언 레이놀즈,조쉬 브롤린</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>14만</td>
      <td>NaN</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>mWL6Mrd</td>
      <td>6.688</td>
      <td>20.680</td>
      <td>12.584</td>
      <td>53.768</td>
      <td>35.992</td>
      <td>88.000</td>
      <td>35.464</td>
      <td>35.464</td>
      <td>8.096</td>
      <td>27.456</td>
      <td>...</td>
      <td>Deadfall</td>
      <td>범죄/드라마/스릴러/액션</td>
      <td>2012.0</td>
      <td>찰리 헌냄,케이트 마라,트리트 윌리암스,앨리슨 그레이엄,씨씨 스페이식,알레인 골렘</td>
      <td>에릭 바나,올리비아 와일드</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>4,028</td>
      <td>NaN</td>
      <td>2.9</td>
    </tr>
    <tr>
      <td>mdBzNnP</td>
      <td>0.880</td>
      <td>0.880</td>
      <td>1.144</td>
      <td>2.904</td>
      <td>6.424</td>
      <td>19.360</td>
      <td>43.120</td>
      <td>71.720</td>
      <td>66.616</td>
      <td>88.000</td>
      <td>...</td>
      <td>Avengers: Endgame</td>
      <td>액션/모험/SF</td>
      <td>2019.0</td>
      <td>NaN</td>
      <td>로버트 다우니 주니어,크리스 에반스,크리스 헴스워스,스칼렛 요한슨,마크 러팔로,제레...</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>14만</td>
      <td>NaN</td>
      <td>4.2</td>
    </tr>
    <tr>
      <td>m5DGQDQ</td>
      <td>0.704</td>
      <td>0.616</td>
      <td>1.056</td>
      <td>2.640</td>
      <td>6.072</td>
      <td>20.856</td>
      <td>48.488</td>
      <td>88.000</td>
      <td>59.840</td>
      <td>51.040</td>
      <td>...</td>
      <td>Avengers: Infinity War</td>
      <td>액션/모험/SF</td>
      <td>2018.0</td>
      <td>NaN</td>
      <td>로버트 다우니 주니어,크리스 에반스,크리스 헴스워스,마크 러팔로,스칼렛 요한슨,폴 ...</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>20만</td>
      <td>NaN</td>
      <td>4.1</td>
    </tr>
    <tr>
      <td>m5mY6m3</td>
      <td>88.000</td>
      <td>29.304</td>
      <td>29.304</td>
      <td>29.304</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>29.304</td>
      <td>29.304</td>
      <td>...</td>
      <td>Avengers of Justice: Farce Wars</td>
      <td>액션/코미디/가족</td>
      <td>2018.0</td>
      <td>NaN</td>
      <td>에이미 스마트,토니 차발레로,사이먼 렉스,스티븐 랜나지시,제프 체이스,제이슨 앨런 스미스</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>8</td>
      <td>NaN</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>m53lMen</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>ASSASSIN X</td>
      <td>액션</td>
      <td>2016.0</td>
      <td>NaN</td>
      <td>올리비에 그루너</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>mO0RpPx</td>
      <td>14.168</td>
      <td>11.352</td>
      <td>31.240</td>
      <td>22.704</td>
      <td>31.240</td>
      <td>88.000</td>
      <td>53.944</td>
      <td>14.168</td>
      <td>2.816</td>
      <td>2.816</td>
      <td>...</td>
      <td>素敵なダイナマイトスキャンダル</td>
      <td>코미디/드라마</td>
      <td>2018.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>TVING,TVING</td>
      <td>오노 마치코,미우라 토코,마에다 아츠코,에모토 타스쿠,무라카미 준,마츠시게 유타카,...</td>
      <td>96</td>
      <td>NaN</td>
      <td>2.7</td>
    </tr>
    <tr>
      <td>m85XnNO</td>
      <td>1.320</td>
      <td>4.576</td>
      <td>1.496</td>
      <td>7.040</td>
      <td>5.192</td>
      <td>35.464</td>
      <td>32.736</td>
      <td>88.000</td>
      <td>46.288</td>
      <td>51.832</td>
      <td>...</td>
      <td>Smultronstället</td>
      <td>드라마</td>
      <td>1957.0</td>
      <td>비비 앤더슨,군나르 비욘스트란드,잉그리드 서린,막스 폰 시도우,줄런 킨달</td>
      <td>빅터 소스트롬</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>2,332</td>
      <td>NaN</td>
      <td>3.9</td>
    </tr>
    <tr>
      <td>mOVPvbY</td>
      <td>1.936</td>
      <td>1.936</td>
      <td>1.000</td>
      <td>9.592</td>
      <td>24.904</td>
      <td>49.720</td>
      <td>88.000</td>
      <td>74.624</td>
      <td>34.408</td>
      <td>40.216</td>
      <td>...</td>
      <td>Jeronimo</td>
      <td>다큐멘터리/역사</td>
      <td>2019.0</td>
      <td>NaN</td>
      <td>헤로니모 임,전후석</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>168</td>
      <td>NaN</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>mOAkDLm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>Fronteras</td>
      <td>액션/스릴러</td>
      <td>2018.0</td>
      <td>헤수스 크리스 아코스타,스티브 셔멧</td>
      <td>스티브 오로페자,스티븐 션 가랜드,웨이드 에버렛,코테즈 샤펠</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>2.3</td>
    </tr>
  </tbody>
</table>
<p>3384 rows × 30 columns</p>
</div>




```python
concat_df.reset_index(inplace=True)
```


```python
concat_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>0.5</th>
      <th>1.0</th>
      <th>1.5</th>
      <th>2.0</th>
      <th>2.5</th>
      <th>3.0</th>
      <th>3.5</th>
      <th>4.0</th>
      <th>4.5</th>
      <th>...</th>
      <th>원제</th>
      <th>장르</th>
      <th>제작 연도</th>
      <th>조연</th>
      <th>주연</th>
      <th>최고의 인생작을 티빙에서!</th>
      <th>출연</th>
      <th>투표자수</th>
      <th>특별출연</th>
      <th>평점</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>mW4L2XW</td>
      <td>0.352</td>
      <td>1.320</td>
      <td>0.440</td>
      <td>2.904</td>
      <td>1.672</td>
      <td>13.904</td>
      <td>9.856</td>
      <td>46.992</td>
      <td>25.608</td>
      <td>...</td>
      <td>Inception</td>
      <td>액션/모험/SF/스릴러</td>
      <td>2010.0</td>
      <td>킬리언 머피,톰 베린저</td>
      <td>레오나르도 디카프리오,조셉 고든-레빗,엘렌 페이지,마리옹 꼬띠아르,톰 하디,와타나베 켄</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>97만</td>
      <td>NaN</td>
      <td>4.4</td>
    </tr>
    <tr>
      <td>1</td>
      <td>m53mEDn</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>El crack cero</td>
      <td>스릴러</td>
      <td>2019.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2</td>
      <td>mWzwxvZ</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>State of exception</td>
      <td>NaN</td>
      <td>2012.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>mWJjpQW</td>
      <td>1.848</td>
      <td>2.640</td>
      <td>2.640</td>
      <td>7.832</td>
      <td>12.760</td>
      <td>41.448</td>
      <td>65.384</td>
      <td>88.000</td>
      <td>39.600</td>
      <td>...</td>
      <td>Deadpool</td>
      <td>액션/모험/코미디</td>
      <td>2016.0</td>
      <td>스테판 카피칙,레슬리 우감스</td>
      <td>라이언 레이놀즈,모레나 바카린,에드 스크라인,T.J. 밀러,지나 카라노,브리아나 힐...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35만</td>
      <td>NaN</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td>4</td>
      <td>mWvkxbr</td>
      <td>1.056</td>
      <td>1.232</td>
      <td>2.464</td>
      <td>6.248</td>
      <td>15.048</td>
      <td>47.256</td>
      <td>83.776</td>
      <td>88.000</td>
      <td>36.344</td>
      <td>...</td>
      <td>Deadpool 2</td>
      <td>액션/모험/코미디/SF</td>
      <td>2018.0</td>
      <td>브리아나 힐데브란드,T.J. 밀러,빌 스카스가드,스테판 카피칙,테리 크루즈,줄리안 데니슨</td>
      <td>라이언 레이놀즈,조쉬 브롤린</td>
      <td>TVING,TVING</td>
      <td>NaN</td>
      <td>14만</td>
      <td>NaN</td>
      <td>3.7</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 31 columns</p>
</div>




```python
concat_df.columns
```




    Index(['index', '0.5', '1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '4.5',
           '5.0', 'casual_title', '감독', '국가', '나레이션', '내용', '단역', '상영시간', '성우',
           '영화 드라마 무제한 감상', '우정출연', '원제', '장르', '제작 연도', '조연', '주연',
           '최고의 인생작을 티빙에서!', '출연', '투표자수', '특별출연', '평점'],
          dtype='object')




```python
del concat_df['영화 드라마 무제한 감상']
```


```python
del concat_df['최고의 인생작을 티빙에서!']
```


```python
concat_df.columns
```




    Index(['index', '0.5', '1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '4.5',
           '5.0', 'casual_title', '감독', '국가', '나레이션', '내용', '단역', '상영시간', '성우',
           '우정출연', '원제', '장르', '제작 연도', '조연', '주연', '출연', '투표자수', '특별출연', '평점'],
          dtype='object')





```python
columns_={
      'index':'movie_code'
    , 'casual_title':'casual_title'
    , '원제':'original_title'
    , '국가':'country'
    , '제작 연도':'production_year'
    , '장르':'genre'
    , '상영시간':'running_time'
    , '감독':'director'
    , '주연':'main_actor'
    , '조연':'supporting_actor'
    , '단역':'extra'
    , '출연':'cast'
    , '특별출연':'cameo_special'
    , '우정출연':'cameo_friendship'
    , '성우':'voice_actor'
    , '나레이션':'narration'
    , '평점':'mean_ratings'
    , '투표자수':'voter'
    , '0.5':'ratings_0.5'
    , '1.0':'ratings_1.0'
    , '1.5':'ratings_1.5'
    , '2.0':'ratings_2.0'
    , '2.5':'ratings_2.5'
    , '3.0':'ratings_3.0'
    , '3.5':'ratings_3.5'
    , '4.0':'ratings_4.0'
    , '4.5':'ratings_4.5'
    , '5.0':'ratings_5.0'
    , '내용':'story'
}
```


```python
concat_df.rename(columns=columns_, inplace=True)
```


```python
concat_df.columns
```




    Index(['movie_code', 'ratings_0.5', 'ratings_1.0', 'ratings_1.5',
           'ratings_2.0', 'ratings_2.5', 'ratings_3.0', 'ratings_3.5',
           'ratings_4.0', 'ratings_4.5', 'ratings_5.0', 'casual_title', 'director',
           'country', 'narration', 'story', 'extra', 'running_time', 'voice_actor',
           'cameo_friendship', 'original_title', 'genre', 'production_year',
           'supporting_actor', 'main_actor', 'cast', 'voter', 'cameo_special',
           'mean_ratings'],
          dtype='object')




```python
sorted_df = concat_df[['movie_code', 'casual_title','original_title','country'
           ,'production_year','genre','running_time','director','main_actor'
           ,'supporting_actor','extra','cast','cameo_special'
           ,'cameo_friendship','voice_actor','narration','mean_ratings'
           ,'voter','ratings_0.5','ratings_1.0','ratings_1.5'
           ,'ratings_2.0','ratings_2.5','ratings_3.0','ratings_3.5'
           ,'ratings_4.0','ratings_4.5', 'ratings_5.0','story']]
```


```python
sorted_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movie_code</th>
      <th>casual_title</th>
      <th>original_title</th>
      <th>country</th>
      <th>production_year</th>
      <th>genre</th>
      <th>running_time</th>
      <th>director</th>
      <th>main_actor</th>
      <th>supporting_actor</th>
      <th>...</th>
      <th>ratings_1.0</th>
      <th>ratings_1.5</th>
      <th>ratings_2.0</th>
      <th>ratings_2.5</th>
      <th>ratings_3.0</th>
      <th>ratings_3.5</th>
      <th>ratings_4.0</th>
      <th>ratings_4.5</th>
      <th>ratings_5.0</th>
      <th>story</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>mW4L2XW</td>
      <td>인셉션</td>
      <td>Inception</td>
      <td>미국,영국</td>
      <td>2010.0</td>
      <td>액션/모험/SF/스릴러</td>
      <td>2시간 27분</td>
      <td>크리스토퍼 놀란</td>
      <td>레오나르도 디카프리오,조셉 고든-레빗,엘렌 페이지,마리옹 꼬띠아르,톰 하디,와타나베 켄</td>
      <td>킬리언 머피,톰 베린저</td>
      <td>...</td>
      <td>1.320</td>
      <td>0.440</td>
      <td>2.904</td>
      <td>1.672</td>
      <td>13.904</td>
      <td>9.856</td>
      <td>46.992</td>
      <td>25.608</td>
      <td>88.000</td>
      <td>타인의 꿈에 들어가 생각을 훔치는 특수 보안요원 코브. 그를 이용해 라이벌 기업의 ...</td>
    </tr>
    <tr>
      <td>1</td>
      <td>m53mEDn</td>
      <td>더 크랙: 인셉션</td>
      <td>El crack cero</td>
      <td>스페인</td>
      <td>2019.0</td>
      <td>스릴러</td>
      <td>2시간 2분</td>
      <td>호세 루이스 가르시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-</td>
    </tr>
    <tr>
      <td>2</td>
      <td>mWzwxvZ</td>
      <td>스테이트 오브 익셉션</td>
      <td>State of exception</td>
      <td>브라질</td>
      <td>2012.0</td>
      <td>NaN</td>
      <td>1시간 13분</td>
      <td>후안 포사다</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-</td>
    </tr>
    <tr>
      <td>3</td>
      <td>mWJjpQW</td>
      <td>데드풀</td>
      <td>Deadpool</td>
      <td>미국</td>
      <td>2016.0</td>
      <td>액션/모험/코미디</td>
      <td>1시간 46분</td>
      <td>팀 밀러</td>
      <td>라이언 레이놀즈,모레나 바카린,에드 스크라인,T.J. 밀러,지나 카라노,브리아나 힐...</td>
      <td>스테판 카피칙,레슬리 우감스</td>
      <td>...</td>
      <td>2.640</td>
      <td>2.640</td>
      <td>7.832</td>
      <td>12.760</td>
      <td>41.448</td>
      <td>65.384</td>
      <td>88.000</td>
      <td>39.600</td>
      <td>45.584</td>
      <td>정의감 제로, 책임감 제로, 정신은 인터스텔라급. 마블 역사상 가장 매력 터지는 히...</td>
    </tr>
    <tr>
      <td>4</td>
      <td>mWvkxbr</td>
      <td>데드풀 2</td>
      <td>Deadpool 2</td>
      <td>미국</td>
      <td>2018.0</td>
      <td>액션/모험/코미디/SF</td>
      <td>1시간 58분</td>
      <td>데이빗 리이치</td>
      <td>라이언 레이놀즈,조쉬 브롤린</td>
      <td>브리아나 힐데브란드,T.J. 밀러,빌 스카스가드,스테판 카피칙,테리 크루즈,줄리안 데니슨</td>
      <td>...</td>
      <td>1.232</td>
      <td>2.464</td>
      <td>6.248</td>
      <td>15.048</td>
      <td>47.256</td>
      <td>83.776</td>
      <td>88.000</td>
      <td>36.344</td>
      <td>25.344</td>
      <td>마침내, 그 분이 오신다! 이번엔 혼자가 아니다!\n\n암치료를 위한 비밀 실험에 ...</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>129648</td>
      <td>mdR6PQV</td>
      <td>The All-Out Game</td>
      <td>The All-Out Game</td>
      <td>NaN</td>
      <td>1970.0</td>
      <td>NaN</td>
      <td>1시간 21분</td>
      <td>オカザキアキラ</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-</td>
    </tr>
    <tr>
      <td>129649</td>
      <td>mWyaJ91</td>
      <td>친구누나 일본판 2</td>
      <td>친구누나 일본판 2</td>
      <td>한국</td>
      <td>2018.0</td>
      <td>성인</td>
      <td>1시간 00분</td>
      <td>정완경</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>어릴 적 부모님을 여의고, 남동생 히로키와 힘들게 살아온 나츠미. 졸업후, 직장에서...</td>
    </tr>
    <tr>
      <td>129650</td>
      <td>md6oza5</td>
      <td>애상의 연인</td>
      <td>Letting Go</td>
      <td>미국</td>
      <td>1985.0</td>
      <td>로맨스</td>
      <td>1시간 44분</td>
      <td>잭 벤더</td>
      <td>존 리터,샤론 글레스,조셉 코르테스,맥스 게일</td>
      <td>피터 드보르스키,마이클 판티니,킷 맥도노프</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>다른 여자가 생긴 남자에게서 버림받은 한 여인이 진정한 자기 자신의 모습과 사랑을 ...</td>
    </tr>
    <tr>
      <td>129651</td>
      <td>m53VZvy</td>
      <td>Venere Imperiale</td>
      <td>Venere Imperiale</td>
      <td>NaN</td>
      <td>1962.0</td>
      <td>NaN</td>
      <td>0분</td>
      <td>ジャン・ドラノワ</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-</td>
    </tr>
    <tr>
      <td>129652</td>
      <td>mWwA8jl</td>
      <td>अचानक</td>
      <td>अचानक</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0분</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
<p>129653 rows × 29 columns</p>
</div>




```python
sorted_df.to_csv('./watcha_mv_detail_final.csv', )
```