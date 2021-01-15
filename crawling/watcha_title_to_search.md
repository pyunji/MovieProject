### 사용파일
`kobis_movie_filtered.csv`  
`tmdb_movie_filtered.csv`  

### 생성 파일
`test1.csv`


```python
import pandas as pd
```

```python
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

tmdb = pd.read_csv('../movie_project/data/movieinfo/tmdb_movie_filtered.csv')
tmdb_title = tmdb[['original_title','title']]

kobis = pd.read_csv('../movie_project/data/movieinfo/kobis_movie_filtered.csv')
kobis_title = kobis[['movieNm','movieNmEn']]

kobis_title.rename(
    columns = {'movieNm':'title_kor', 'movieNmEn':'title_en'}
    , inplace = True
)
tmdb_title.rename(
    columns = {'title':'title_kor','original_title':'title_en'}
    , inplace = True
)
all_title = pd.concat(
    [tmdb_title,kobis_title]
    , keys = ['tmdb','kobis']
)

all_title.to_csv('./test.csv')

all_title[all_title.duplicated()==True]

all_title1 = all_title.drop_duplicates()

all_title1.to_csv('./test1.csv')

all_title1.head()

```

 

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>title_en</th>
      <th>title_kor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5" valign="top">tmdb</td>
      <td>0</td>
      <td>Inception</td>
      <td>인셉션</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Deadpool</td>
      <td>데드풀</td>
    </tr>
    <tr>
      <td>2</td>
      <td>The Avengers</td>
      <td>어벤져스</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Interstellar</td>
      <td>인터스텔라</td>
    </tr>
    <tr>
      <td>4</td>
      <td>The Dark Knight</td>
      <td>다크 나이트</td>
    </tr>
  </tbody>
</table>
</div>
