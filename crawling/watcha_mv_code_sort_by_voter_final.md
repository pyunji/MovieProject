```python
import pandas as pd
from pandas import DataFrame, Series
```


```python
df = pd.read_csv('./watcha_mv_detail_voter_tonumeric.csv', index_col  = 0)
```


```python
df1 = df.sort_values(by='voter', ascending=False).reset_index()
```


```python
df1
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
      <th>movie_code</th>
      <th>casual_title</th>
      <th>original_title</th>
      <th>country</th>
      <th>production_year</th>
      <th>genre</th>
      <th>running_time</th>
      <th>director</th>
      <th>main_actor</th>
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
      <td>18607</td>
      <td>mWvDGZd</td>
      <td>써니</td>
      <td>써니</td>
      <td>한국</td>
      <td>2011.0</td>
      <td>드라마/코미디</td>
      <td>2시간 4분</td>
      <td>강형철</td>
      <td>유호정,고수희,홍진희,이연경,심은경,강소라,민효린,남보라</td>
      <td>...</td>
      <td>3.344</td>
      <td>1.848</td>
      <td>8.448</td>
      <td>8.712</td>
      <td>43.384</td>
      <td>34.672</td>
      <td>88.000</td>
      <td>25.256</td>
      <td>87.648</td>
      <td>전라도 벌교 전학생 나미는 긴장하면 터져 나오는 사투리 탓에 첫날부터 날라리들의 놀...</td>
    </tr>
    <tr>
      <td>1</td>
      <td>15762</td>
      <td>mOAgnP5</td>
      <td>도둑들</td>
      <td>도둑들</td>
      <td>한국</td>
      <td>2012.0</td>
      <td>범죄/액션</td>
      <td>2시간 15분</td>
      <td>최동훈</td>
      <td>김윤석,김혜수,이정재,전지현</td>
      <td>...</td>
      <td>4.048</td>
      <td>2.640</td>
      <td>11.528</td>
      <td>12.320</td>
      <td>54.648</td>
      <td>41.096</td>
      <td>88.000</td>
      <td>22.704</td>
      <td>75.240</td>
      <td>한 팀으로 활동 중인 한국의 도둑 뽀빠이와 예니콜, 씹던껌, 잠파노. 미술관을 터는...</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>mOVgp1d</td>
      <td>어벤져스</td>
      <td>The Avengers</td>
      <td>미국</td>
      <td>2012.0</td>
      <td>모험/판타지/액션/SF</td>
      <td>2시간 22분</td>
      <td>조스 웨던</td>
      <td>로버트 다우니 주니어,크리스 헴스워스,스칼렛 요한슨,마크 러팔로,크리스 에반스,제레...</td>
      <td>...</td>
      <td>2.640</td>
      <td>1.144</td>
      <td>5.104</td>
      <td>4.400</td>
      <td>22.176</td>
      <td>18.568</td>
      <td>52.712</td>
      <td>20.240</td>
      <td>88.000</td>
      <td>에너지원 ‘큐브’를 이용한 적의 등장으로 인류가 위험에 처하자 국제평화유지기구인 쉴...</td>
    </tr>
    <tr>
      <td>3</td>
      <td>19868</td>
      <td>m5mQ9z5</td>
      <td>광해, 왕이 된 남자</td>
      <td>광해, 왕이 된 남자</td>
      <td>한국</td>
      <td>2012.0</td>
      <td>시대극/드라마/역사</td>
      <td>2시간 11분</td>
      <td>추창민</td>
      <td>이병헌,류승룡,한효주</td>
      <td>...</td>
      <td>3.608</td>
      <td>2.024</td>
      <td>8.360</td>
      <td>8.712</td>
      <td>40.920</td>
      <td>33.704</td>
      <td>88.000</td>
      <td>26.576</td>
      <td>83.776</td>
      <td>왕위를 둘러싼 권력 다툼과 당쟁으로 혼란이 극에 달한 광해군 8년. 자신의 목숨을 ...</td>
    </tr>
    <tr>
      <td>4</td>
      <td>10234</td>
      <td>m5rND75</td>
      <td>7번방의 선물</td>
      <td>7번방의 선물</td>
      <td>한국</td>
      <td>2012.0</td>
      <td>드라마/코미디</td>
      <td>2시간 7분</td>
      <td>이환경</td>
      <td>류승룡,갈소원</td>
      <td>...</td>
      <td>6.160</td>
      <td>3.608</td>
      <td>11.352</td>
      <td>9.504</td>
      <td>31.328</td>
      <td>21.824</td>
      <td>54.560</td>
      <td>19.888</td>
      <td>88.000</td>
      <td>최악의 흉악범들이 모인 교도소 7번방에 이상한 놈이 들어왔다. 그는 바로 6살 지능...</td>
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
      <td>38678</td>
      <td>md7Bx2O</td>
      <td>스킨너</td>
      <td>Skinner</td>
      <td>미국</td>
      <td>1993.0</td>
      <td>스릴러/공포</td>
      <td>1시간 30분</td>
      <td>이반 나기</td>
      <td>테드 레이미,릭키 레이크,데이빗 워쇼프스키</td>
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
      <td>잔인한 정신병자 스킨너(Dennis Skinner: 테드 라이미 분)에 의해 추한 ...</td>
    </tr>
    <tr>
      <td>74273</td>
      <td>38672</td>
      <td>mdEyZlE</td>
      <td>Bob Dylan Quest Television Special</td>
      <td>Bob Dylan Quest Television Special</td>
      <td>NaN</td>
      <td>1964.0</td>
      <td>NaN</td>
      <td>0분</td>
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
      <td>62186</td>
      <td>mO0gmgX</td>
      <td>옆집 유부녀의 가슴</td>
      <td>Can't Stand! My Neighbor Has Large Breasts!!!</td>
      <td>NaN</td>
      <td>2016.0</td>
      <td>NaN</td>
      <td>0분</td>
      <td>타카하시 카즈히코</td>
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
      <td>초대받아 간 집에서 여성의 속옷을 훔치면서 벌어지는 이야기의 성애 영화</td>
    </tr>
    <tr>
      <td>74275</td>
      <td>38664</td>
      <td>mW42MQg</td>
      <td>더 가디언 엔젤</td>
      <td>The Guardian Angel</td>
      <td>핀란드,덴마크,크로아티아</td>
      <td>2018.0</td>
      <td>스릴러</td>
      <td>1시간 42분</td>
      <td>아르토 할로넨</td>
      <td>요한 필립 애스백,조쉬 루카스,라드 세르베드지야,사라 술리에</td>
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
      <td>74276</td>
      <td>34855</td>
      <td>m5a9NXj</td>
      <td>City Lights</td>
      <td>City Lights</td>
      <td>인도</td>
      <td>2014.0</td>
      <td>스릴러/드라마</td>
      <td>2시간 6분</td>
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
<p>74277 rows × 30 columns</p>
</div>




```python
df1.to_csv('./watcha_mv_detail_voter_tonumeric.csv')
```


```python
DataFrame({'movie_code':df1["movie_code"]}).to_csv('./watcha_mv_code_sort_by_voter_final.csv')
```


```python
pd.read_csv('./watcha_mv_code_sort_by_voter_final.csv', index_col = 0)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>mWvDGZd</td>
    </tr>
    <tr>
      <td>1</td>
      <td>mOAgnP5</td>
    </tr>
    <tr>
      <td>2</td>
      <td>mOVgp1d</td>
    </tr>
    <tr>
      <td>3</td>
      <td>m5mQ9z5</td>
    </tr>
    <tr>
      <td>4</td>
      <td>m5rND75</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>74272</td>
      <td>md7Bx2O</td>
    </tr>
    <tr>
      <td>74273</td>
      <td>mdEyZlE</td>
    </tr>
    <tr>
      <td>74274</td>
      <td>mO0gmgX</td>
    </tr>
    <tr>
      <td>74275</td>
      <td>mW42MQg</td>
    </tr>
    <tr>
      <td>74276</td>
      <td>m5a9NXj</td>
    </tr>
  </tbody>
</table>
<p>74277 rows × 1 columns</p>
</div>

