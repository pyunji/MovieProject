### 사용파일
`kobis_movie_filtered.csv`  
`tmdb_movie_filtered.csv`  

### 생성 파일
`test1.csv`


```python
import pandas as pd
```


```python
pd.read_csv('../movie_project/data/movieinfo/tmdb_movie_filtered.csv')
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
      <th>imdb_id</th>
      <th>title</th>
      <th>original_title</th>
      <th>original_language</th>
      <th>runtime</th>
      <th>release_date</th>
      <th>budget</th>
      <th>revenue</th>
      <th>genres</th>
      <th>overview</th>
      <th>popularity</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>tagline</th>
      <th>production_companies</th>
      <th>production_countries</th>
      <th>spoken_languages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>27205.0</td>
      <td>tt1375666</td>
      <td>인셉션</td>
      <td>Inception</td>
      <td>en</td>
      <td>148.0</td>
      <td>2010-07-15</td>
      <td>160000000.0</td>
      <td>8.255328e+08</td>
      <td>[{'id': 28, 'name': '액션'}, {'id': 878, 'name':...</td>
      <td>타인의 꿈과 접속해 생각을 빼낼 수 있는 근미래, 돔 코브(레오나르도 디카프리오)는...</td>
      <td>55.528</td>
      <td>24996.0</td>
      <td>8.3</td>
      <td>생각을 훔치는 거대한 전쟁</td>
      <td>[{'id': 923, 'logo_path': '/5UQsZrfbfG2dYJbx8D...</td>
      <td>[{'iso_3166_1': 'GB', 'name': 'United Kingdom'...</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}, {'iso...</td>
    </tr>
    <tr>
      <td>1</td>
      <td>293660.0</td>
      <td>tt1431045</td>
      <td>데드풀</td>
      <td>Deadpool</td>
      <td>en</td>
      <td>108.0</td>
      <td>2016-02-09</td>
      <td>58000000.0</td>
      <td>7.831000e+08</td>
      <td>[{'id': 28, 'name': '액션'}, {'id': 12, 'name': ...</td>
      <td>특수부대 요원 출신의 용병 웨이드 윌슨(라이언 레이놀즈)은 취향과 장난기마저 똑 닮...</td>
      <td>36.615</td>
      <td>22122.0</td>
      <td>7.6</td>
      <td>마블 역사상 가장 매력 터지는 히어로</td>
      <td>[{'id': 7505, 'logo_path': '/837VMM4wOkODc1idN...</td>
      <td>[{'iso_3166_1': 'US', 'name': 'United States o...</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}]</td>
    </tr>
    <tr>
      <td>2</td>
      <td>24428.0</td>
      <td>tt0848228</td>
      <td>어벤져스</td>
      <td>The Avengers</td>
      <td>en</td>
      <td>142.0</td>
      <td>2012-04-25</td>
      <td>220000000.0</td>
      <td>1.519558e+09</td>
      <td>[{'id': 878, 'name': 'SF'}, {'id': 28, 'name':...</td>
      <td>에너지원 큐브를 이용한 적의 등장으로 인류가 위험에 처하자 국제평화유지기구인 쉴드의...</td>
      <td>53.733</td>
      <td>21813.0</td>
      <td>7.7</td>
      <td>최강의 슈퍼히어로들이 모였다.</td>
      <td>[{'id': 420, 'logo_path': '/hUzeosd33nzE5MCNsZ...</td>
      <td>[{'iso_3166_1': 'US', 'name': 'United States o...</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}, {'iso...</td>
    </tr>
    <tr>
      <td>3</td>
      <td>157336.0</td>
      <td>tt0816692</td>
      <td>인터스텔라</td>
      <td>Interstellar</td>
      <td>en</td>
      <td>169.0</td>
      <td>2014-11-05</td>
      <td>165000000.0</td>
      <td>6.751200e+08</td>
      <td>[{'id': 12, 'name': '모험'}, {'id': 18, 'name': ...</td>
      <td>세계 각국의 정부와 경제가 완전히 붕괴된 미래가 다가온다. 지난 20세기에 범한 잘...</td>
      <td>65.551</td>
      <td>21426.0</td>
      <td>8.3</td>
      <td>우린 답을 찾을 거야, 늘 그랬듯이</td>
      <td>[{'id': 923, 'logo_path': '/5UQsZrfbfG2dYJbx8D...</td>
      <td>[{'iso_3166_1': 'GB', 'name': 'United Kingdom'...</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}]</td>
    </tr>
    <tr>
      <td>4</td>
      <td>155.0</td>
      <td>tt0468569</td>
      <td>다크 나이트</td>
      <td>The Dark Knight</td>
      <td>en</td>
      <td>152.0</td>
      <td>2008-07-16</td>
      <td>185000000.0</td>
      <td>1.004558e+09</td>
      <td>[{'id': 18, 'name': '드라마'}, {'id': 28, 'name':...</td>
      <td>범죄와 부정부패를 제거하여 고담시를 지키려는 배트맨(크리스찬 베일). 그는 짐 고든...</td>
      <td>49.676</td>
      <td>21389.0</td>
      <td>8.4</td>
      <td>이 도시에 정의는 죽었다</td>
      <td>[{'id': 429, 'logo_path': '/2Tc1P3Ac8M479naPp1...</td>
      <td>[{'iso_3166_1': 'GB', 'name': 'United Kingdom'...</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}, {'iso...</td>
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
    </tr>
    <tr>
      <td>129607</td>
      <td>536883.0</td>
      <td>tt8480208</td>
      <td>Flash in the Pain</td>
      <td>Flash in the Pain</td>
      <td>en</td>
      <td>4.0</td>
      <td>2014-06-10</td>
      <td>0.0</td>
      <td>0.000000e+00</td>
      <td>[]</td>
      <td>NaN</td>
      <td>0.600</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>[]</td>
      <td>[]</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}]</td>
    </tr>
    <tr>
      <td>129608</td>
      <td>354605.0</td>
      <td>tt2823218</td>
      <td>Too Smart for Strangers</td>
      <td>Too Smart for Strangers</td>
      <td>en</td>
      <td>41.0</td>
      <td>1985-06-19</td>
      <td>0.0</td>
      <td>0.000000e+00</td>
      <td>[{'id': 18, 'name': '드라마'}, {'id': 10751, 'nam...</td>
      <td>NaN</td>
      <td>0.673</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>[]</td>
      <td>[{'iso_3166_1': 'US', 'name': 'United States o...</td>
      <td>[{'iso_639_1': 'en', 'name': 'English'}]</td>
    </tr>
    <tr>
      <td>129609</td>
      <td>406086.0</td>
      <td>tt3790350</td>
      <td>Ánimo valiente</td>
      <td>Ánimo valiente</td>
      <td>en</td>
      <td>6.0</td>
      <td>2014-06-10</td>
      <td>0.0</td>
      <td>0.000000e+00</td>
      <td>[{'id': 18, 'name': '드라마'}]</td>
      <td>NaN</td>
      <td>0.627</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>[{'id': 79207, 'logo_path': None, 'name': 'Rel...</td>
      <td>[{'iso_3166_1': 'ES', 'name': 'Spain'}]</td>
      <td>[{'iso_639_1': 'es', 'name': 'Español'}]</td>
    </tr>
    <tr>
      <td>129610</td>
      <td>67649.0</td>
      <td>tt0084019</td>
      <td>Le grand frère</td>
      <td>Le grand frère</td>
      <td>fr</td>
      <td>0.0</td>
      <td>1982-09-08</td>
      <td>0.0</td>
      <td>0.000000e+00</td>
      <td>[{'id': 80, 'name': '범죄'}]</td>
      <td>NaN</td>
      <td>0.620</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>[]</td>
      <td>[{'iso_3166_1': 'FR', 'name': 'France'}]</td>
      <td>[{'iso_639_1': 'fr', 'name': 'Français'}]</td>
    </tr>
    <tr>
      <td>129611</td>
      <td>498126.0</td>
      <td>tt0454553</td>
      <td>Summer of No Return</td>
      <td>Summer of No Return</td>
      <td>en</td>
      <td>30.0</td>
      <td>1988-01-01</td>
      <td>0.0</td>
      <td>0.000000e+00</td>
      <td>[{'id': 35, 'name': '코미디'}]</td>
      <td>NaN</td>
      <td>0.600</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
<p>129612 rows × 18 columns</p>
</div>




```python
pd.read_csv('../movie_project/data/movieinfo/kobis_movie_filtered.csv')
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
      <th>movieCd</th>
      <th>movieNm</th>
      <th>movieNmEn</th>
      <th>prdtYear</th>
      <th>openDt</th>
      <th>typeNm</th>
      <th>prdtStatNm</th>
      <th>nationAlt</th>
      <th>genreAlt</th>
      <th>repNationNm</th>
      <th>...</th>
      <th>info_prdtStatNm</th>
      <th>info_typeNm</th>
      <th>info_nations</th>
      <th>info_genres</th>
      <th>info_directors</th>
      <th>info_actors</th>
      <th>info_showTypes</th>
      <th>info_companys</th>
      <th>info_audits</th>
      <th>info_staffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>20206967</td>
      <td>피델리티</td>
      <td>Fidelity</td>
      <td>2019.0</td>
      <td>NaN</td>
      <td>장편</td>
      <td>개봉예정</td>
      <td>러시아</td>
      <td>드라마</td>
      <td>러시아</td>
      <td>...</td>
      <td>개봉예정</td>
      <td>장편</td>
      <td>[{'nationNm': '러시아'}]</td>
      <td>[{'genreNm': '드라마'}]</td>
      <td>[{'peopleNm': '니기나 사이풀라에바', 'peopleNmEn': 'Nig...</td>
      <td>[{'peopleNm': '에브게니야 그로모바', 'peopleNmEn': 'Evg...</td>
      <td>[{'showTypeGroupNm': '2D', 'showTypeNm': '디지털'}]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>1</td>
      <td>20207185</td>
      <td>해안가의 처녀들: 인어</td>
      <td>Virgins</td>
      <td>2018.0</td>
      <td>NaN</td>
      <td>장편</td>
      <td>기타</td>
      <td>이스라엘</td>
      <td>드라마</td>
      <td>이스라엘</td>
      <td>...</td>
      <td>기타</td>
      <td>장편</td>
      <td>[{'nationNm': '이스라엘'}]</td>
      <td>[{'genreNm': '드라마'}]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>2</td>
      <td>20207141</td>
      <td>스와핑 : 아내의 동의 무삭제</td>
      <td>NaN</td>
      <td>2019.0</td>
      <td>NaN</td>
      <td>장편</td>
      <td>개봉예정</td>
      <td>한국</td>
      <td>멜로/로맨스</td>
      <td>한국</td>
      <td>...</td>
      <td>개봉예정</td>
      <td>장편</td>
      <td>[{'nationNm': '한국'}]</td>
      <td>[{'genreNm': '멜로/로맨스'}]</td>
      <td>[{'peopleNm': '최민현', 'peopleNmEn': ''}]</td>
      <td>[]</td>
      <td>[{'showTypeGroupNm': '2D', 'showTypeNm': '디지털'}]</td>
      <td>[{'companyCd': '20161021', 'companyNm': '(주)영화...</td>
      <td>[{'auditNo': '2020-MF00608 ', 'watchGradeNm': ...</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>3</td>
      <td>20207101</td>
      <td>헌트</td>
      <td>The Hunt</td>
      <td>2020.0</td>
      <td>NaN</td>
      <td>장편</td>
      <td>개봉예정</td>
      <td>미국</td>
      <td>액션,공포(호러),스릴러</td>
      <td>미국</td>
      <td>...</td>
      <td>개봉예정</td>
      <td>장편</td>
      <td>[{'nationNm': '미국'}]</td>
      <td>[{'genreNm': '액션'}, {'genreNm': '공포(호러)'}, {'g...</td>
      <td>[{'peopleNm': '크레이그 조벨', 'peopleNmEn': 'Craig ...</td>
      <td>[{'peopleNm': '베티 길핀', 'peopleNmEn': 'Betty Gi...</td>
      <td>[{'showTypeGroupNm': '2D', 'showTypeNm': '디지털'}]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>4</td>
      <td>20196841</td>
      <td>걸즈 앤 판처 최종장 제2화</td>
      <td>GIRLS und PANZER das FINALE : Part II</td>
      <td>2019.0</td>
      <td>NaN</td>
      <td>장편</td>
      <td>개봉예정</td>
      <td>일본</td>
      <td>애니메이션</td>
      <td>일본</td>
      <td>...</td>
      <td>개봉예정</td>
      <td>장편</td>
      <td>[{'nationNm': '일본'}]</td>
      <td>[{'genreNm': '애니메이션'}]</td>
      <td>[{'peopleNm': '미즈시마 츠토무', 'peopleNmEn': 'Mizus...</td>
      <td>[{'peopleNm': '후치가미 마이', 'peopleNmEn': 'Mai Fu...</td>
      <td>[{'showTypeGroupNm': '2D', 'showTypeNm': '디지털'}]</td>
      <td>[{'companyCd': '20158370', 'companyNm': '(주)디스...</td>
      <td>[]</td>
      <td>[]</td>
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
      <td>60392</td>
      <td>20060475</td>
      <td>죽느냐 사느냐</td>
      <td>To Be or Not To Be</td>
      <td>2006.0</td>
      <td>NaN</td>
      <td>단편</td>
      <td>기타</td>
      <td>한국</td>
      <td>NaN</td>
      <td>한국</td>
      <td>...</td>
      <td>기타</td>
      <td>단편</td>
      <td>[{'nationNm': '한국'}]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[{'showTypeGroupNm': '필름', 'showTypeNm': '필름'}]</td>
      <td>[]</td>
      <td>[{'auditNo': '', 'watchGradeNm': ''}]</td>
      <td>[{'peopleNm': '김윤정', 'peopleNmEn': 'KIM Yoon-j...</td>
    </tr>
    <tr>
      <td>60393</td>
      <td>20060468</td>
      <td>샌프란시스코 블루스</td>
      <td>San Francisco Blues</td>
      <td>2005.0</td>
      <td>NaN</td>
      <td>단편</td>
      <td>기타</td>
      <td>한국</td>
      <td>NaN</td>
      <td>한국</td>
      <td>...</td>
      <td>기타</td>
      <td>단편</td>
      <td>[{'nationNm': '한국'}]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[{'showTypeGroupNm': '필름', 'showTypeNm': '필름'}]</td>
      <td>[]</td>
      <td>[{'auditNo': '', 'watchGradeNm': ''}]</td>
      <td>[{'peopleNm': '김태연', 'peopleNmEn': 'KIM Tai-ye...</td>
    </tr>
    <tr>
      <td>60394</td>
      <td>20061262</td>
      <td>마이 리틀 월드</td>
      <td>My Little World</td>
      <td>2001.0</td>
      <td>NaN</td>
      <td>장편</td>
      <td>기타</td>
      <td>한국</td>
      <td>NaN</td>
      <td>한국</td>
      <td>...</td>
      <td>기타</td>
      <td>장편</td>
      <td>[{'nationNm': '한국'}]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[{'showTypeGroupNm': '필름', 'showTypeNm': '필름'}]</td>
      <td>[]</td>
      <td>[{'auditNo': '', 'watchGradeNm': ''}]</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>60395</td>
      <td>20061278</td>
      <td>망월동 行 25-2</td>
      <td>The Line 25-2 To Mangwol-dong</td>
      <td>2000.0</td>
      <td>NaN</td>
      <td>단편</td>
      <td>기타</td>
      <td>한국</td>
      <td>다큐멘터리</td>
      <td>한국</td>
      <td>...</td>
      <td>기타</td>
      <td>단편</td>
      <td>[{'nationNm': '한국'}]</td>
      <td>[{'genreNm': '다큐멘터리'}]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[{'showTypeGroupNm': '필름', 'showTypeNm': '필름'}]</td>
      <td>[]</td>
      <td>[{'auditNo': '', 'watchGradeNm': ''}]</td>
      <td>[{'peopleNm': '박성배', 'peopleNmEn': 'PARK Sung-...</td>
    </tr>
    <tr>
      <td>60396</td>
      <td>19910096</td>
      <td>칙칙이의 내일은 참피온</td>
      <td>Tomorrow's Champion</td>
      <td>1991.0</td>
      <td>19910803.0</td>
      <td>장편</td>
      <td>개봉</td>
      <td>한국</td>
      <td>코미디</td>
      <td>한국</td>
      <td>...</td>
      <td>개봉</td>
      <td>장편</td>
      <td>[{'nationNm': '한국'}]</td>
      <td>[{'genreNm': '코미디'}]</td>
      <td>[]</td>
      <td>[{'peopleNm': '장고웅', 'peopleNmEn': 'JANG Go-un...</td>
      <td>[{'showTypeGroupNm': '필름', 'showTypeNm': '필름'}]</td>
      <td>[]</td>
      <td>[{'auditNo': '91-221', 'watchGradeNm': ''}]</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
<p>60397 rows × 30 columns</p>
</div>




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
