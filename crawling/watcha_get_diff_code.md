```python
import requests
from bs4 import BeautifulSoup
import urllib
import re

import numpy as np
from pandas import DataFrame, Series
import pandas as pd
```


```python
import glob
```


```python
file_list = glob.glob('./mv_detail/*')
detail_df = [pd.read_csv(file, index_col=0) for file in file_list]
```

```python
con_mv_detail=pd.concat(detail_df)
len(con_mv_detail)
```
    125641

```python
con_mv_detail
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
      <td>mdRZ0LK</td>
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
      <td>Последняя ночь</td>
      <td>드라마</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>mOAGV3X</td>
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
      <td>Status Quo - The Last Night of the Electrics</td>
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
    <tr>
      <td>mdMB67y</td>
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
      <td>We Have Not Come Here to Die</td>
      <td>NaN</td>
      <td>2018.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>m53vqVy</td>
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
      <td>Vashti Bunyan: From Here to Before</td>
      <td>다큐멘터리</td>
      <td>2008.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>mOgKVGM</td>
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
      <td>I Used to Be Normal: A Boyband Fangirl Story</td>
      <td>다큐멘터리</td>
      <td>2018.0</td>
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
<p>125641 rows × 30 columns</p>
</div>




```python
all_mv_code = pd.read_csv('./all_mv_code.csv', header=None)
all_mv_code.head()
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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>mW4L2XW</td>
    </tr>
    <tr>
      <td>1</td>
      <td>m53mEDn</td>
    </tr>
    <tr>
      <td>2</td>
      <td>mWzwxvZ</td>
    </tr>
    <tr>
      <td>3</td>
      <td>mWJjpQW</td>
    </tr>
    <tr>
      <td>4</td>
      <td>mWvkxbr</td>
    </tr>
  </tbody>
</table>
</div>




```python
a = set(all_mv_code[0].tolist())
len(a)
```




    129653




```python
b = set(con_mv_detail.index.tolist())
len(b)
```




    125641




```python
diff = a - b
diff_list = list(diff)
```


```python
len(a-b)
```




    4012




```python
Series(diff_list)
```




    0       m5ewXGg
    1       mOkl9zE
    2       m5DpbR5
    3       mdEwALV
    4       m5aYE4M
             ...   
    4007    mdR6PQV
    4008    mWyaJ91
    4009    md6oza5
    4010    m53VZvy
    4011    mWwA8jl
    Length: 4012, dtype: object




```python
diff_ser = Series(diff_list)
```


```python
DataFrame(diff_ser, columns=['diff_code']).to_csv('./diff.csv')
```


```python
pd.read_csv('./diff.csv', index_col=0)
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
      <th>diff_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>m5ewXGg</td>
    </tr>
    <tr>
      <td>1</td>
      <td>mOkl9zE</td>
    </tr>
    <tr>
      <td>2</td>
      <td>m5DpbR5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>mdEwALV</td>
    </tr>
    <tr>
      <td>4</td>
      <td>m5aYE4M</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>4007</td>
      <td>mdR6PQV</td>
    </tr>
    <tr>
      <td>4008</td>
      <td>mWyaJ91</td>
    </tr>
    <tr>
      <td>4009</td>
      <td>md6oza5</td>
    </tr>
    <tr>
      <td>4010</td>
      <td>m53VZvy</td>
    </tr>
    <tr>
      <td>4011</td>
      <td>mWwA8jl</td>
    </tr>
  </tbody>
</table>
<p>4012 rows × 1 columns</p>
</div>




```python
for file in file_list:
    df = pd.read_csv(file, index_col=0)
    if 'm5aYE4M' in df.index:
        print(file)
#     for code in df.index:
#         if code == 'm2dj7w5':
#             print(file)
```


```python
df1 = pd.read_csv('./mv_detail/mv_detail30.csv', index_col=0)
```


```python
pd.read_csv(file_list[6], index_col=0)
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
      <th>casual_title</th>
      <th>국가</th>
      <th>내용</th>
      <th>상영시간</th>
      <th>원제</th>
      <th>장르</th>
      <th>제작 연도</th>
      <th>0.5</th>
      <th>1.0</th>
      <th>1.5</th>
      <th>...</th>
      <th>성우</th>
      <th>영화 드라마 무제한 감상</th>
      <th>우정출연</th>
      <th>조연</th>
      <th>주연</th>
      <th>최고의 인생작을 티빙에서!</th>
      <th>출연</th>
      <th>특별출연</th>
      <th>투표자수</th>
      <th>평점</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mOop4Gz</td>
      <td>굿-바이</td>
      <td>일본</td>
      <td>-</td>
      <td>1시간 6분</td>
      <td>グッドバイ</td>
      <td>NaN</td>
      <td>2020.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>코바야시 아사코,이케우에 코헤이,이게타 히로에,요시이에 아키히토</td>
      <td>후쿠다 마유코</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>mOb3NRd</td>
      <td>플레이어</td>
      <td>미국</td>
      <td>흥행물만 취급하는 헐리우드 메이저 영화사의 그리핀(팀 로빈스)은 어느날 시나리오 작...</td>
      <td>2시간 3분</td>
      <td>The Player</td>
      <td>드라마/스릴러/범죄/코미디</td>
      <td>1992.0</td>
      <td>0.440</td>
      <td>6.952</td>
      <td>1.408</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>프레드 워드,우피 골드버그,피터 갤러거</td>
      <td>팀 로빈스,그레타 스카치</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2,186</td>
      <td>3.6</td>
    </tr>
    <tr>
      <td>mOVvGNR</td>
      <td>체스 플레이어</td>
      <td>스페인</td>
      <td>1940년 제2차 세계대전 시기,\n '천재'라 불리며 승승장구하던 체스 플레이어 ...</td>
      <td>1시간 38분</td>
      <td>El jugador de ajedrez</td>
      <td>드라마</td>
      <td>2017.0</td>
      <td>37.488</td>
      <td>71.896</td>
      <td>15.312</td>
      <td>...</td>
      <td>NaN</td>
      <td>왓챠플레이,왓챠플레이</td>
      <td>NaN</td>
      <td>안드레스 게르트루디스,후안 델 산토</td>
      <td>마크 클로테트,멜리나 메튜스,스테판 웨이너트,알레조 사우라스</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>620</td>
      <td>2.9</td>
    </tr>
    <tr>
      <td>m5mQZA5</td>
      <td>플레이어</td>
      <td>인도</td>
      <td>대량의 금이 비밀리에 루마니아로 수송되자 A급 절도범 찰리와 리야는 금을 탈취하기 ...</td>
      <td>2시간 47분</td>
      <td>Players</td>
      <td>액션/드라마/스릴러/범죄</td>
      <td>2012.0</td>
      <td>9.768</td>
      <td>4.928</td>
      <td>4.928</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>슈웨타 바르드와즈,바비 데올,소남 카푸르</td>
      <td>소남 카푸르,아비쉑 밧찬,비파샤 바수</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40</td>
      <td>2.8</td>
    </tr>
    <tr>
      <td>m5NNKL5</td>
      <td>바이올린 플레이어</td>
      <td>프랑스,벨기에</td>
      <td>71년에 데뷔한 사진 작가 찰리 반 담의 첫 영화 데뷔작으로 깐느 영화제에 출품되었...</td>
      <td>0분</td>
      <td>The Violin Player</td>
      <td>드라마</td>
      <td>1994.0</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>5.720</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>존 도브리닌,제노 레히너,이네스 드 메디어로스</td>
      <td>프랑수아 베를레앙,리샤드 베리</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>94</td>
      <td>3.9</td>
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
      <td>mOk6Zqk</td>
      <td>프라이버시</td>
      <td>미국</td>
      <td>마크는 어플 개발대회에 참가하기 위해 친구 토비와 어플을 개발 중이다. 마크는 휴대...</td>
      <td>1시간 33분</td>
      <td>Privacy</td>
      <td>스릴러</td>
      <td>2012.0</td>
      <td>16.016</td>
      <td>19.976</td>
      <td>16.016</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>존 쉐퍼드,지나 부쉬,클레이턴 마이어스,브랜튼 듀플레시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>76</td>
      <td>2.5</td>
    </tr>
    <tr>
      <td>mdRlAgW</td>
      <td>프라이버시</td>
      <td>미국</td>
      <td>어느날 오후, 테레사(Theresa Barnes: 밀리 아비틀 분)는 공원에서 누군...</td>
      <td>1시간 34분</td>
      <td>Invasion Of Privacy</td>
      <td>스릴러/드라마</td>
      <td>1996.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>스콧 윌킨슨</td>
      <td>밀리 아비탈,조나슨 스캐치,나오미 캠벨</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5</td>
      <td>3.5</td>
    </tr>
    <tr>
      <td>mObGAbR</td>
      <td>프라이버시</td>
      <td>한국</td>
      <td>스피드에 중독된 톱스타에게 납치된 '사생팬'과 딸을 구하려는 전직 스턴트맨 아버지의...</td>
      <td>0분</td>
      <td>프라이버시</td>
      <td>NaN</td>
      <td>2014.0</td>
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
      <td>NaN</td>
    </tr>
    <tr>
      <td>md768Ne</td>
      <td>오필리아 - 러브&amp;프라이버시_셋팅</td>
      <td>독일</td>
      <td>부끄러운 상황이 되기 전에 너의 생각을 어떻게 드러낼 것인가? 나쁜 생각들은 당신을...</td>
      <td>4분</td>
      <td>Ophelia - Love &amp; Privacy_Settings</td>
      <td>애니메이션/코미디</td>
      <td>2013.0</td>
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
      <td>NaN</td>
    </tr>
    <tr>
      <td>m5YgvXO</td>
      <td>프라이벗 넘버</td>
      <td>미국</td>
      <td>-</td>
      <td>1시간 20분</td>
      <td>Private Number</td>
      <td>로맨스/드라마</td>
      <td>1936.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>마저리 게이트슨,폴 하비,제인 다웰,폴 스탠턴,존 밀란,먼로 오슬리</td>
      <td>로버트 테일러,로레타 영</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>2.9</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 30 columns</p>
</div>




```python
df.index.values
```


```python
diff_cd = pd.read_csv('./mv_detail_diff.csv', index_col=0)
```


```python
len(diff_cd)
```




    4012




```python
final = pd.concat([con_mv_detail,diff_cd])
```

    C:\Users\vusgu\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
    of pandas will change to not sort by default.
    
    To accept the future behavior, pass 'sort=False'.
    
    To retain the current behavior and silence the warning, pass 'sort=True'.
    
      """Entry point for launching an IPython kernel.
    


```python
len(final)
```




    129653




```python
final
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
