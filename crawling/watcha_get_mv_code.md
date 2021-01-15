```python
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

import requests

from bs4 import BeautifulSoup
```


```python
def mv_cd(title: str) -> list:
    """title을 입력할 때 검색되는 영화의 코드 리스트를 반환하는 함수"""
    url = f'https://watcha.com/ko-KR/searches/movies?query={title}'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    soups = soup.select('#root > div > div > section > section > div > div > div > ul > li > a')
    code_list=[]
    for sp in soups:
        code = sp.get('href').split('/')[-1]
        code_list.append(code)
    return code_list    
```


```python
def one_csv_all_cd(file_path: str) -> list:
    """하나의 csv 파일의 영화제목을 검색하면 하나의 리스트로 영화 코드를 합쳐주는 함수."""
    df = pd.read_csv(file_path)
#     df = pd.read_csv(file_path)[:10]
    titles = df['title_kor']
    all_list = []
    for title in titles:
        all_list += mv_cd(title)
    return all_list
```


```python
def mk_ser(all_list: list, file_num: str) -> Series:
        """모든 영화 코드 리스트를 받아 Series로 변환 후 
        파일과 같은 숫자로 넘버링해 저장하는 함수"""
        Series(all_list).to_csv(f'./mv_code/movie_series{file_num}.csv')
```


```python
file_list = glob.glob('./mv_titles/*')
# file_list = ['./mv_titles\\file00']
for file_path in file_list:
    file_num = file_path[-2:]
    all_list = one_csv_all_cd(file_path)
    mk_ser(all_list, file_num)
```


```python
pd.read_csv('./mv_titles/file00', index_col=0)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0.1</th>
      <th>Unnamed: 1</th>
      <th>title_en</th>
      <th>title_kor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>tmdb</td>
      <td>0</td>
      <td>Inception</td>
      <td>인셉션</td>
    </tr>
    <tr>
      <td>1</td>
      <td>tmdb</td>
      <td>1</td>
      <td>Deadpool</td>
      <td>데드풀</td>
    </tr>
    <tr>
      <td>2</td>
      <td>tmdb</td>
      <td>2</td>
      <td>The Avengers</td>
      <td>어벤져스</td>
    </tr>
    <tr>
      <td>3</td>
      <td>tmdb</td>
      <td>3</td>
      <td>Interstellar</td>
      <td>인터스텔라</td>
    </tr>
    <tr>
      <td>4</td>
      <td>tmdb</td>
      <td>4</td>
      <td>The Dark Knight</td>
      <td>다크 나이트</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>1995</td>
      <td>tmdb</td>
      <td>2009</td>
      <td>Hall Pass</td>
      <td>홀패스 - 일주일의 자유</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>tmdb</td>
      <td>2010</td>
      <td>Elle</td>
      <td>엘르</td>
    </tr>
    <tr>
      <td>1997</td>
      <td>tmdb</td>
      <td>2011</td>
      <td>Two Weeks Notice</td>
      <td>투 윅스 노티스</td>
    </tr>
    <tr>
      <td>1998</td>
      <td>tmdb</td>
      <td>2012</td>
      <td>Polar</td>
      <td>폴라</td>
    </tr>
    <tr>
      <td>1999</td>
      <td>tmdb</td>
      <td>2013</td>
      <td>The Pink Panther</td>
      <td>핑크 팬더</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 4 columns</p>
</div>




```python
pd.read_csv('./movie_series_kor/movie_series00.csv', index_col=0, header=None)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
    </tr>
    <tr>
      <th>0</th>
      <th></th>
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
    <tr>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>7112</td>
      <td>mWJ33xO</td>
    </tr>
    <tr>
      <td>7113</td>
      <td>mWzEB45</td>
    </tr>
    <tr>
      <td>7114</td>
      <td>mOkmKp5</td>
    </tr>
    <tr>
      <td>7115</td>
      <td>m5rmkmd</td>
    </tr>
    <tr>
      <td>7116</td>
      <td>mWJ9VM5</td>
    </tr>
  </tbody>
</table>
<p>7117 rows × 1 columns</p>
</div>
