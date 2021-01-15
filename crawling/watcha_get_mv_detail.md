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
# 첫화면에서 soup 가져올 경우 get_soup(code)
# overview에서 가져올 경우 get_soup(code, 'overview')
def get_soup(code, option=''):
    url = f'https://watcha.com/ko-KR/contents/{code}/{option}'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    return soup
```


```python
def get_casual_title(soup, code):
    # 영화 코드 형태여도 내용이 아예 없는 경우 존재.
    # 이 경우 영화의 제목을 NaN으로 지정
    try:
        titles = soup.select('#root > div > div > section > div > div > div > section > div > div > div > div > div > h1')
        title = titles[0].text
        dict_ = {'casual_title':title}
    except IndexError:
        dict_ = {'casual_title':np.nan}
    return DataFrame(dict_, index = [code])
```


```python
def get_bar_area(soup, code):
    try:
        p = re.compile(';height:(\d+[.]?\d*)')
        soups = soup.find_all(
            class_=re.compile('BarArea')
        )
        soups
        points = []
        for i, ba in enumerate(soups):
            height = p.findall(str(ba))
            if height:
                height = height[0]
            else:
                height = np.nan
            point = (i+1)*0.5
            points.append({
                  'point': (i+1)*0.5
                , 'class': ba.find('span').get('class')[0].split('-')[1]
                , 'height' : round(float(height), ndigits=3)
            })
        pre_df = DataFrame(points).sort_values(by='class'
                                              ).ffill()[['point','height']].sort_values(by='point')
        return DataFrame(dict(zip(pre_df['point'],pre_df['height'])), index=[code])
    except KeyError:
        e_point=[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]
        e_height=[np.nan]*10
        return DataFrame(dict(zip(e_point, e_height)), index = [code])
```


```python
def get_rating_n_voter(soup, code):
    try:
        ratings = soup.find_all(class_=re.compile("ContentRatings"))
        rating = ratings[0].text

        rating_lst = rating.split()

        rating_mean = rating_lst[1].lstrip('★')

        rating_voter = rating_lst[2].lstrip('(').rstrip('명)')

        a = ['평점', '투표자수']
        b = [rating_mean, rating_voter]
        rating_n_voter = dict(zip(a,b))
    except IndexError:
        a = ['평점', '투표자수']
        b = [np.nan]*2
        rating_n_voter = dict(zip(a,b))
    return DataFrame({code:rating_n_voter}).T
```


```python
def get_casts(soup, code):
    soups = soup.select('#root > div > div > section > div > div > div > div > div > div > div > div > div > section > div > div > div > div > div > ul > li > a > div > div')
    role=[]
    cast=[]
    for sp in soups:
        role_ = sp.find_all(class_=re.compile("Subtitle"))
        cast_= sp.find_all(class_=re.compile("Title"))
        if role_:
            role.append(role_[0].text)
        if cast_:
            cast.append(cast_[0].text)
    role_cast = list(zip(role,cast))
    rc_dict = {}
    for role, cast in role_cast:
        if role in rc_dict.keys():
            rc_dict[role].append(cast)
        else: 
            rc_dict[role] = [cast]
            
    for role in rc_dict:
        rc_dict[role]=','.join(rc_dict[role])
    return DataFrame(Series(rc_dict), columns=[code]).T
```


```python
def get_mv_detail(code):
    soup = get_soup(code, 'overview')
    categories = soup.select('#root > div > div > section > section > div > div > ul > dl > dt')
    contents = soup.select('#root > div > div > section > section > div > div > ul > dl > dd')
    cate=[]
    for category in categories:
        cate.append(category.text)
    
    cont=[]
    for content in contents:
        cont.append(content.text)
    
    detail = dict(zip(cate,cont))
    return DataFrame({code:detail}).T
```


```python
import glob
```


```python
file_list = glob.glob('./test_file/*')
file_list
```




    ['./test_file\\code10.csv']




```python
from tqdm import tqdm_notebook
```


```python
test_file_list = glob.glob('./test_file/*')
for file in tqdm_notebook(test_file_list):
    file_num = file[-6:-4]
    series = pd.read_csv(file)['watcha_code']
    casual_title = []
    bar_area = []
    mv_detail = []
    casts = []
    rating_n_voter=[]
    for code in tqdm_notebook(series):
        soup = get_soup(code)
        # list에 DataFrame 들어있음.
        casual_title.append(get_casual_title(soup, code))
        bar_area.append(get_bar_area(soup, code))
        mv_detail.append(get_mv_detail(code))
        casts.append(get_casts(soup,code))
        rating_n_voter.append(get_rating_n_voter(soup,code))
    con_c_t = pd.concat(casual_title)
    con_b_a = pd.concat(bar_area)
    con_m_d = pd.concat(mv_detail)
    con_casts = pd.concat(casts)
    con_r_n_v = pd.concat(rating_n_voter)
    from_contents = pd.merge(
        con_c_t, con_m_d
        , left_index = True
        , right_index = True
    #     , on=con_c_t.index
    )
    merge_con_ovview = pd.merge(
        from_contents, con_b_a
        , left_index=True
        , right_index=True
    )
    test = pd.merge(
        merge_con_ovview, con_casts
        , left_index=True
        , right_index=True
    )
    test1 = pd.merge(
        test, con_r_n_v
        , left_index=True
        , right_index=True
    )
    test1.to_csv(f'./mv_detail/mv_detail{file_num}.csv')
```



```python
test = pd.read_csv('../watcha_test/watcha_mv_detail_final.csv', index_col=0)
test
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
test.loc[test['casual_title']==np.nan]
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
  </tbody>
</table>
<p>0 rows × 29 columns</p>
</div>
