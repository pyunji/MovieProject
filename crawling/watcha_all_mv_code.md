```python
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import glob
```


```python
en_title_list = glob.glob('./movie_series_en/*')
pd.read_csv(en_title_list[0], header=None)[1]
```




    0       mW4L2XW
    1       m53mEDn
    2       mWJjpQW
    3       mWvkxbr
    4       mOAmVQO
             ...   
    7471    mWzEB45
    7472    mdBqwGO
    7473    mOkmKp5
    7474    m5rmkmd
    7475    mWJ9VM5
    Name: 1, Length: 7476, dtype: object




```python
en_csv_list = [pd.read_csv(file, header=None)[1] for file in en_title_list]

con_en_title = pd.concat(en_csv_list
                        , ignore_index = True
                        )
con_en_title
```




    0         mW4L2XW
    1         m53mEDn
    2         mWJjpQW
    3         mWvkxbr
    4         mOAmVQO
               ...   
    374249    m5r89mO
    374250    mO0ggmx
    374251    m5XM2DL
    374252    m5nPDDO
    374253    mOb4zn5
    Name: 1, Length: 374254, dtype: object




```python
con_en_title.drop_duplicates(inplace=True)
```


```python
kor_title_list = glob.glob('./movie_series_kor/*')

kor_csv_list = [pd.read_csv(file, header=None)[1] for file in kor_title_list]

con_kor_title = pd.concat(kor_csv_list
                        , ignore_index = True
                        )
con_kor_title
```




    0         mW4L2XW
    1         m53mEDn
    2         mWzwxvZ
    3         mWJjpQW
    4         mWvkxbr
               ...   
    314911    mOVkBRd
    314912    mO0ggmx
    314913    mOk8yMd
    314914    m5r89mO
    314915    m5nPDDO
    Name: 1, Length: 314916, dtype: object




```python
con_kor_title.drop_duplicates(inplace = True)
```


```python
concat_kor_en_title = pd.concat([con_kor_title, con_en_title], ignore_index = True).drop_duplicates()
```


```python
concat_kor_en_title
```




    0         mW4L2XW
    1         m53mEDn
    2         mWzwxvZ
    3         mWJjpQW
    4         mWvkxbr
               ...   
    237320    mdRZ0LK
    237321    mOAGV3X
    237328    mdMB67y
    237329    m53vqVy
    237330    mOgKVGM
    Name: 1, Length: 129653, dtype: object




```python
watcha = DataFrame({
    'watcha_code':concat_kor_en_title
})
```


```python
watcha.reset_index(drop=True, inplace = True)
```


```python
watcha
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>watcha_code</th>
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
      <td>129648</td>
      <td>mdRZ0LK</td>
    </tr>
    <tr>
      <td>129649</td>
      <td>mOAGV3X</td>
    </tr>
    <tr>
      <td>129650</td>
      <td>mdMB67y</td>
    </tr>
    <tr>
      <td>129651</td>
      <td>m53vqVy</td>
    </tr>
    <tr>
      <td>129652</td>
      <td>mOgKVGM</td>
    </tr>
  </tbody>
</table>
<p>129653 rows × 1 columns</p>
</div>




```python
watcha.to_csv('./watcha_all_mv_code.csv')
```