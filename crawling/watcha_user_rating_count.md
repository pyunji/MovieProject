```python
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
```


```python
from bs4 import BeautifulSoup
import requests
```


```python
from tqdm import tqdm_notebook
```


```python
def create_rating_count_col(file_path):
    # user_id 컬럼만 있는 데이터 프레임
    df = pd.read_csv(file_path, index_col=0)
    df['rating_count'] = np.nan
    return df
```


```python
# # user_id = 'yKZx3nLEWD54d'
# user_id = 'YMKqmjXMkvloD'
# url = f'https://watcha.com/ko-KR/users/{user_id}/contents/movies'
# res = requests.get(url)
# html = res.text
# soup = BeautifulSoup(html, 'html.parser')

# int(soup.find(attrs = 'eupnho10').text)
```


```python
# np.isnan(user_id_df.loc[0, 'rating_count'])
```


```python
# 이런 식으로는 대입 불가능
# user_id_df[user_id_df['id']=='nkPvrb8wrvgar']['rating_count'] = 100

# loc를 써서 행을 선택해야 대입 가능
# user_id_df.loc[user_id_df['id']=='nkPvrb8wrvgar', 'rating_count']
```


```python
def get_user_ratings(df):
    for i in tqdm_notebook(df.index):
        # range(len(df.index)) 하면 스레드 실행시키는 start_num, end_num과
        # 인덱스가 안맞아 버려서 스레드 안돌아감.
        # i는 0부터 초기화되는 숫자가 아니라
        # df의 index값임을 주의!
        user_id = df.loc[i, 'id']
        url = f'https://watcha.com/ko-KR/users/{user_id}/contents/movies'
        res = requests.get(url)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')    
        try:
            df.loc[i, 'rating_count'] = int(soup.find(attrs='eupnho10').text)
        except AttributeError:
            # 비공개 계정인 경우 url에 접근할 수 없다. 몇개의 영화를 평가했는지도 알 수 없음.
            df.loc[i, 'rating_count'] = 0
```




```python
from multiprocessing.pool import ThreadPool
from queue import Queue
```


```python
def run_get_ratings(start_num, end_num, user_id_df):
    split_num = int((end_num-start_num)/5)
    
    q = Queue(maxsize=5)
    for i in range(q.maxsize):
        q.put(user_id_df[start_num + i * split_num :start_num + (i+1)* split_num])
        
    with ThreadPool(5) as tp:
        tp.map(
            get_user_ratings
            , [q.get() for _ in range(5)]
        )

```


```python
user_id_ratings_df = create_rating_count_col('./watcha_user/user_id.csv')
user_id_ratings_df
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
      <th>id</th>
      <th>rating_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>ZBm5R0Mj7qd46</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>1</td>
      <td>WRQxD0apVxdl9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Mr95nJBED5ZPG</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>3</td>
      <td>jae5WNGZ6v1P3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>4</td>
      <td>yKZx3kdBRx4dJ</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>215255</td>
      <td>YMKqmOAXy5loD</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>215256</td>
      <td>ld0q02BmO56Xn</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>215257</td>
      <td>j4PxOdnM7qp0Q</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>215258</td>
      <td>K8nPvyEN9vYo0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>215259</td>
      <td>NP9vL2lQ9x6kl</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>215260 rows × 2 columns</p>
</div>




```python
# np.isnan(user_id_ratings_df.loc[215255, 'rating_count'] )
```


```python
# 과부하를 막기위해 jump 수 만큼 나눠서 실행.
#===================================
# file_path = './mv_review/mv_review_after/user_id_copy.csv'
start_num = 0
end_num = 10
jump = 5
#===================================

# user_id_df = create_rating_count_col(file_path)
for i in tqdm_notebook(range(int((end_num-start_num)/jump))):    
    run_get_ratings(start_num+i*jump, start_num+(i+1)*jump, user_id_ratings_df)
    
```

    


```python
user_id_ratings_df
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
      <th>id</th>
      <th>rating_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>ZBm5R0Mj7qd46</td>
      <td>2070.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>WRQxD0apVxdl9</td>
      <td>415.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Mr95nJBED5ZPG</td>
      <td>1318.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>jae5WNGZ6v1P3</td>
      <td>773.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>yKZx3kdBRx4dJ</td>
      <td>267.0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>DgwxAeQYNxrMj</td>
      <td>5072.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6ADvGQdzgxzZl</td>
      <td>2442.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>DgwxABBQMqrMj</td>
      <td>841.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>87Gv7PoB35E6o</td>
      <td>1295.0</td>
    </tr>
    <tr>
      <td>9</td>
      <td>VRZv4bDPnxr6y</td>
      <td>1124.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
user_id_ratings_df.loc[user_id_ratings_df['rating_count']==0]
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
      <th>id</th>
      <th>rating_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1006</th>
      <td>nb4xkW78yexOA</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2048</th>
      <td>ZBm5RWjkDxd46</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2407</th>
      <td>JgAx88JQVxLbO</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2694</th>
      <td>djaxbZEbwxLw8</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3371</th>
      <td>YMKqmpwNkxloD</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>213988</th>
      <td>nb4xk8J1MqOAz</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>214133</th>
      <td>Qgy51ZBlXxDjk</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>214160</th>
      <td>RE952jBPM5Q72</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>214254</th>
      <td>DgwxA6EekdqrM</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>215214</th>
      <td>YMKqmyWArqloD</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>1163 rows × 2 columns</p>
</div>




```python
user_id_ratings_df.loc[user_id_ratings_df.rating_count.isnull()==True]
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
      <th>id</th>
      <th>rating_count</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
sorted_df = user_id_ratings_df.sort_values(by=['rating_count'], ascending=False)
sorted_df.reset_index(drop=True, inplace=True)
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
      <th>id</th>
      <th>rating_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17ovVgGBL5zyn</td>
      <td>20120.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>YMKqmjXMkvloD</td>
      <td>16657.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Qgy51zEAZxDjk</td>
      <td>11152.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>XZBm5RYOavd46</td>
      <td>10716.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>WRQxDOw1V5dl9</td>
      <td>10675.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>215255</th>
      <td>2mwvgNZNogqMa</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>215256</th>
      <td>36lvXb7eKJxXd</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>215257</th>
      <td>VRZv4e21nZ5r6</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>215258</th>
      <td>yKZx3oBXOx4dJ</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>215259</th>
      <td>24BqE2dAeVvrj</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>215260 rows × 2 columns</p>
</div>




```python
np.sum(sorted_df.rating_count)
```




    89567120.0




```python
sorted_df.to_csv('./watcha_user/temp/user_id_sort_by_rating_count03.csv')
```
