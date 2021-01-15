```python
"""
mv_review/mv_review_before 디렉토리에 
"""
```


```python
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
```


```python
import glob
```


```python
file_list = glob.glob('./mv_review/mv_review_before/*')

df_list = [pd.read_csv(file, index_col=0) for file in file_list]
```


```python
def check_len(df_list):
    i = 0
    for df in df_list:
        i += len(df)
    print('전처리 전 모든 데이터의 length : ', i)
```


```python
def processing_df(df_list):
    # 폴더 내의 모든 DataFrame을 concat한다.
    df1 = pd.concat(df_list, ignore_index=True)
    print("전처리 전 모든 데이터의 length : ", len(df1))
    
    print("중복 된 row의 수: ", np.sum(df1.duplicated()))
    # 중복된 row를 삭제했다.
    df2 = df1.drop_duplicates().reset_index(drop=True)
    
    # 리뷰가 없는 영화는 따로 저장하였다.
    df3 = df2[df2.id.isnull()]
    print("리뷰가 없는 영화의 개수 : ", len(df3))
    df3.to_csv('./mv_review/mv_review_after/리뷰가없는영화들.csv')
    
    # 리뷰가 있는 영화를 따로 저장하였다.
    reviewed = df2.dropna(subset=['id']).reset_index(drop=True)
    reviewed.to_csv('./mv_review/mv_review_after/reviewed_mv.csv')
    
    # reviewed의 id만 뽑아오자
    user_id = DataFrame({
        'id':reviewed.id.drop_duplicates().reset_index().id
    })
    user_id.to_csv('./watcha_user/user_id.csv')
    return user_id
```


```python
check_len(df_list)
```

    전처리 전 모든 데이터의 length :  6243134
    


```python
processing_df(df_list)
```

    전처리 전 모든 데이터의 length :  6243134
    중복 된 row의 수:  9736
    리뷰가 없는 영화의 개수 :  30317
    




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>ZBm5R0Mj7qd46</td>
    </tr>
    <tr>
      <td>1</td>
      <td>WRQxD0apVxdl9</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Mr95nJBED5ZPG</td>
    </tr>
    <tr>
      <td>3</td>
      <td>jae5WNGZ6v1P3</td>
    </tr>
    <tr>
      <td>4</td>
      <td>yKZx3kdBRx4dJ</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>215443</td>
      <td>YMKqmOAXy5loD</td>
    </tr>
    <tr>
      <td>215444</td>
      <td>ld0q02BmO56Xn</td>
    </tr>
    <tr>
      <td>215445</td>
      <td>j4PxOdnM7qp0Q</td>
    </tr>
    <tr>
      <td>215446</td>
      <td>K8nPvyEN9vYo0</td>
    </tr>
    <tr>
      <td>215447</td>
      <td>NP9vL2lQ9x6kl</td>
    </tr>
  </tbody>
</table>
<p>215448 rows × 1 columns</p>
</div>




```python
pd.read_csv('./mv_review/mv_review_after/reviewed_mv.csv', index_col=0)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movie_code</th>
      <th>id</th>
      <th>nick_name</th>
      <th>ratings</th>
      <th>comment</th>
      <th>like</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>mWvDGZd</td>
      <td>ZBm5R0Mj7qd46</td>
      <td>김성호의 씨네만세</td>
      <td>3.0</td>
      <td>춘화의 경제력을 통해 나머지 멤버들이 처한 문제를 한 순간에 해결하는 억지스러운 결...</td>
      <td>593.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>mWvDGZd</td>
      <td>WRQxD0apVxdl9</td>
      <td>SJ</td>
      <td>4.0</td>
      <td>가 본 적도 없는 시대에서 풍기는 향수. 추억만큼 아름답지 않은 현재도 너무 잘 보...</td>
      <td>388.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>mWvDGZd</td>
      <td>Mr95nJBED5ZPG</td>
      <td>탈지구 기원자</td>
      <td>3.0</td>
      <td>누구나 있었으면, 하고 바라는 찬란한 추억. \n그러나 결코 머무르지 않는 추억.</td>
      <td>236.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>mWvDGZd</td>
      <td>jae5WNGZ6v1P3</td>
      <td>다한</td>
      <td>3.5</td>
      <td>그 많던 여학생들은 어디로 갔는가 / 문정희</td>
      <td>213.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>mWvDGZd</td>
      <td>yKZx3kdBRx4dJ</td>
      <td>이하연</td>
      <td>5.0</td>
      <td>알지도 못하는 시대를 공감하고있었다</td>
      <td>179.0</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>6203076</td>
      <td>m5m6GzW</td>
      <td>g64qzYYy1xER0</td>
      <td>underdog</td>
      <td>3.0</td>
      <td>너무 사차원 유머라 괴리가 크다.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>6203077</td>
      <td>m5m6GzW</td>
      <td>7YaR5Yejo5gX1</td>
      <td>채영</td>
      <td>4.0</td>
      <td>재밌다</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>6203078</td>
      <td>m5m6GzW</td>
      <td>PdjaxbNwExLw8</td>
      <td>소주안주</td>
      <td>1.0</td>
      <td>내가 본 영화 중 최악.....무슨 내용을 담으려고 했는지,,</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>6203079</td>
      <td>m5m6GzW</td>
      <td>ADgwxAPB45rMj</td>
      <td>정혜린</td>
      <td>2.0</td>
      <td>난 아직도 이 영화가 무슨 내용인지 이해가 안된다</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>6203080</td>
      <td>m5m6GzW</td>
      <td>RJgkqlGkxX0b6</td>
      <td>쿡쿠다스</td>
      <td>4.0</td>
      <td>공효진의 연기는 정말 좋은 연기인데 시나리오가 너무 가벼운게 아쉽다.</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>6203081 rows × 6 columns</p>
</div>
