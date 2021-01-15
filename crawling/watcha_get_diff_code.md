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
all_mv_code = pd.read_csv('./all_mv_code.csv', header=None)
all_mv_code.head()
```




<div>
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
diff_cd = pd.read_csv('./mv_detail_diff.csv', index_col=0)
```


```python
len(diff_cd)
```




    4012




```python
final = pd.concat([con_mv_detail,diff_cd])
```

```python
len(final)
```




    129653