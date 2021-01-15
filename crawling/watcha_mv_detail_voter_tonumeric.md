```python
import pandas as pd
from pandas import DataFrame, Series
```


```python
df = pd.read_csv('../watcha_test/watcha_mv_detail_final.csv', index_col=0)
```


```python
df1 = df[df['voter'].notnull()].truncate()
```


```python
df[df['voter'].notnull()].truncate
```


```python
df1.reset_index(inplace=True)
```


```python
del df1['index']
```


```python
def str_to_number(str_):
    if '만' in str(str_):
        str_ = str(str_).replace('만','0000')
    elif ',' in str(str_):
        str_ = ''.join(str(str_).split(','))
    return str_
```


```python
df1.voter = df1.voter.map(str_to_number)
```


```python
df1.voter = df1.voter.astype('int')
```


```python
df1
```




<div>
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
      <td>2</td>
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
      <td>3</td>
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
      <td>4</td>
      <td>mWL6Mrd</td>
      <td>데드폴</td>
      <td>Deadfall</td>
      <td>미국</td>
      <td>2012.0</td>
      <td>범죄/드라마/스릴러/액션</td>
      <td>1시간 35분</td>
      <td>스테판 루조비츠키</td>
      <td>에릭 바나,올리비아 와일드</td>
      <td>찰리 헌냄,케이트 마라,트리트 윌리암스,앨리슨 그레이엄,씨씨 스페이식,알레인 골렘</td>
      <td>...</td>
      <td>20.680</td>
      <td>12.584</td>
      <td>53.768</td>
      <td>35.992</td>
      <td>88.000</td>
      <td>35.464</td>
      <td>35.464</td>
      <td>8.096</td>
      <td>27.456</td>
      <td>광활한 설원 한 복판. 카지노를 털고 도망 중이던 애디슨(에릭 바나)과 라이자(올리...</td>
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
      <td>74272</td>
      <td>m5QqJVQ</td>
      <td>씨 디스 무비</td>
      <td>See This Movie</td>
      <td>미국</td>
      <td>2014.0</td>
      <td>코미디</td>
      <td>1시간 22분</td>
      <td>데이비드 M. 로젠탈</td>
      <td>존 조,세스 메이어스,레이몬드 오코너</td>
      <td>짐 피독,패튼 오스왈트,제시카 파레,제서린 길직</td>
      <td>...</td>
      <td>88.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>44.000</td>
      <td>1.000</td>
      <td>44.000</td>
      <td>44.000</td>
      <td>1.000</td>
      <td>44.000</td>
      <td>-</td>
    </tr>
    <tr>
      <td>74273</td>
      <td>m5QaEQy</td>
      <td>The Old Bear Hunter</td>
      <td>The Old Bear Hunter</td>
      <td>NaN</td>
      <td>1982.0</td>
      <td>NaN</td>
      <td>1시간 43분</td>
      <td>ゴトウトシオ</td>
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
      <td>74274</td>
      <td>mWwQvqd</td>
      <td>리빙 온 러브 얼론</td>
      <td>Living On Love Alone</td>
      <td>프랑스</td>
      <td>2010.0</td>
      <td>드라마</td>
      <td>1시간 30분</td>
      <td>이자벨 크자이카</td>
      <td>아나이스 드무스티에,피오 마르마이</td>
      <td>로랑 포이트레노스,쟝-루이스 콜로흐,크리스틴 브루체르,줄리앙 하우랑,제니퍼 덱커,귀...</td>
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
      <td>우수한 성적으로 학교 생활에 늘 적극적인 대학생 줄리. 우연히 면접을 보던 중 좀도...</td>
    </tr>
    <tr>
      <td>74275</td>
      <td>mW42DLd</td>
      <td>더 스크린</td>
      <td>The Screen At Kamchanod</td>
      <td>태국</td>
      <td>2007.0</td>
      <td>NaN</td>
      <td>1시간 38분</td>
      <td>송삭 몽콜송</td>
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
      <td>올 여름을 장식할 태국 호러 한 편. 유스는 한 영사기사가 유령 군중들을 위한 영화...</td>
    </tr>
    <tr>
      <td>74276</td>
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
  </tbody>
</table>
<p>74277 rows × 29 columns</p>
</div>




```python
DataFrame(df1['movie_code'], columns = ['movie_code']).to_csv('./watcha_mv_code_filtered.csv')
```


```python
df1.to_csv('./watcha_mv_detail_voter_tonumeric.csv')
```

