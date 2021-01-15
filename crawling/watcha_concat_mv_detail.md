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
concat_df.reset_index(inplace=True)
```


```python
concat_df.head()
```




<div>
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
sorted_df.to_csv('./watcha_mv_detail_final.csv', )
```