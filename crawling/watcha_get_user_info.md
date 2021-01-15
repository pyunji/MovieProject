```python
import numpy as np
from pandas import DataFrame, Series
import pandas as pd
```


```python
from selenium import webdriver
```


```python
import time
```


```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```


```python
from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import TimeoutException
```


```python
df= pd.read_csv('./watcha_user/user_id_sort_by_rating_count_final.csv', index_col = 0)

df
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
      <td>17ovVgGBL5zyn</td>
      <td>20120.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>YMKqmjXMkvloD</td>
      <td>16657.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Qgy51zEAZxDjk</td>
      <td>11152.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>XZBm5RYOavd46</td>
      <td>10716.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>WRQxDOw1V5dl9</td>
      <td>10676.0</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>215443</td>
      <td>nb4xk8PZKqOAz</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>215444</td>
      <td>zNM5NpDpdq26j</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>215445</td>
      <td>nkPvrPm9Krxga</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>215446</td>
      <td>87Gv7jyBGqE6o</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>215447</td>
      <td>6NW5QKko6q1Yo</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>215448 rows × 2 columns</p>
</div>




```python
df = df.loc[df.rating_count>5]
df.reset_index(drop=True, inplace=True)
```


```python
df
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
      <td>17ovVgGBL5zyn</td>
      <td>20120.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>YMKqmjXMkvloD</td>
      <td>16657.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Qgy51zEAZxDjk</td>
      <td>11152.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>XZBm5RYOavd46</td>
      <td>10716.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>WRQxDOw1V5dl9</td>
      <td>10676.0</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>207788</td>
      <td>zNM5NbVn2526j</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td>207789</td>
      <td>87Gv7GXjJvE6o</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td>207790</td>
      <td>WRQxDPYZnxdl9</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td>207791</td>
      <td>3BnvwnbbDKqPA</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td>207792</td>
      <td>6NW5QPN9kv1Yo</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
<p>207793 rows × 2 columns</p>
</div>




```python
# 의도적으로 오류 발생시키기 위함
# df.loc[df.id == 'JgAx8b48OvLbO', 'rating_count'] = 150
```


```python
from tqdm import tqdm_notebook
```


```python
from queue import Queue

from multiprocessing.pool import ThreadPool
```


```python
def login(driver):
    """login 후 login 완료된 driver return"""
    driver.get('https://watcha.com/ko-KR')

    xpath_login = """//*[@id="root"]/div/div[1]/header/nav/div/div/ul/li[2]/button"""
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_login))
    )
    driver.find_element_by_xpath(xpath_login).click()

    email_ = "hunji11@naver.com"
    pw_ = 'teamproject10'
#     email_ = "sistersbomb@naver.com"
#     pw_ = "qorzjtm1346"
    elem_id = driver.find_element_by_id('sign_in_email')
    elem_id.clear()
    elem_id.send_keys(email_)

    elem_pw = driver.find_element_by_id('sign_in_password')
    elem_pw.clear()
    elem_pw.send_keys(pw_)

    xpath_login_click = """//*[@id="root"]/div/div[2]/div/div/div/section/div/div/form/button"""
    driver.find_element_by_xpath(xpath_login_click).click()
    return driver
```


```python
import requests
from bs4 import BeautifulSoup
```


```python
def user_info(driver, test_df):
    try:
        lst_true = []
        lst_false = []
        for user_id in tqdm_notebook(test_df['id']):
            temp_ = []
            url = f'https://watcha.com/ko-KR/users/{user_id}/contents/movies/ratings'
            if int(test_df.loc[test_df.id==user_id, 'rating_count'])<10:
                res = requests.get(url)
                html = res.text
                soup = BeautifulSoup(html, 'html.parser')
                soups = soup.find_all(class_='e3fgkal0')
                for elem in soups:
                    mv_code=elem.find('a').get('href').split('/')[-1]
                    ratings=float(elem.find(class_='e3fgkal4').text.lstrip('★'))
                    temp_.append((user_id, mv_code, ratings))
                    lst_true.append((user_id, mv_code, ratings))
            else:
                driver.get(url)
                last_height = str(driver.execute_script('return document.documentElement.scrollHeight'))
                repeat_num=1
                while True:
                    driver.execute_script(f'window.scrollTo(0, {last_height});')
                    time.sleep(0.5)
                    try:
                        WebDriverWait(driver, 5).until(
                            lambda x: str(x.execute_script('return document.documentElement.scrollHeight')
                                         ) != last_height
                        )
                    except TimeoutException:
                        difference = len(driver.find_elements_by_class_name('e3fgkal0'))\
                              - int(test_df.loc[test_df.id==user_id, 'rating_count'])
                        if difference<-9 and repeat_num<21:
                            print('=============================================================')
                            print(user_id, f": 개수가 맞지않아 {repeat_num}번째 재실행 중(오차 {difference}개)")
                            print('=============================================================')
                            repeat_num = repeat_num+1
                            continue
                        else :
                               break
                    last_height = str(driver.execute_script('return document.documentElement.scrollHeight'))
                
                if repeat_num>20:
                    lst_false.append(user_id)
                    print(user_id, ": 반복 횟수가 20번을 넘어 다음으로 넘어감(별도 저장됨)")
                    continue
                else:
                    rated_mvs = driver.find_elements_by_class_name('e3fgkal0')
                    for rated_mv in rated_mvs:
                        mv_code = rated_mv.find_element_by_tag_name('a'
                                                                   ).get_attribute('href').split('/')[-1]
                        ratings = float(rated_mv.find_element_by_class_name('e3fgkal4').text.lstrip('★'))
                        lst_true.append((user_id, mv_code, ratings))
                        temp_.append((user_id, mv_code, ratings))
            print('user_id : ', user_id, '평가한 영화 개수 : ', len(temp_))        
        kwd_true = ['user_id', 'mv_code', 'ratings']
        cont_true = list(zip(*lst_true))
        df_true = DataFrame(dict(zip(kwd_true, cont_true)))
        if lst_false:
            kwd_false = 'user_id'
            cont_false = lst_false
            df_false = DataFrame({kwd_false:cont_false})
        else:
            df_false = DataFrame()
    finally:
        driver.quit()
    return(df_true, df_false)
```


```python
options = webdriver.ChromeOptions()

prefs = {
    'profile.default_content_setting_values': {
          'cookies': 2, 'images': 2, 'plugins': 2
        , 'popups': 2, 'geolocation': 2, 'notifications': 2
        , 'auto_select_certificate': 2, 'fullscreen': 2, 'mouselock': 2
        , 'mixed_script': 2, 'media_stream': 2, 'media_stream_mic': 2
        , 'media_stream_camera': 2, 'protocol_handlers': 2, 'ppapi_broker': 2
        , 'automatic_downloads': 2, 'midi_sysex': 2, 'push_messaging': 2
        , 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 'protected_media_identifier': 2
        , 'app_banner': 2, 'site_engagement': 2, 'durable_storage': 2
    }
}

options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('headless')
options.add_argument("disable-gpu")
# console창에서 계속 에러가 발생하고 있는 것을 발견
# [0423/180816.169:INFO:CONSOLE(0)] "Uncaught (in promise) TypeError: Failed to fetch", source: https://watcha.com/sw.js (0)
# same origin policy는 결국 클라이언트인 웹 브라우저가 요청을 해도 되는지 판단해서 결정하는 것으로,
# 이 과정만 무시한다면 어디든 요청을 못할 이유는 없다
# 크롬같은 웹 브라우저들은 실행시 커맨드라인 옵션을 통해서 외부 도메인 요청가능 여부를 확인하는 동작을 무시하는 것이 가능.
# 동일출처정책(same-origin-policy) 참고
# https://enterkey.tistory.com/409
options.add_argument("--disable-web-security")
```


```python
def run_get_user_data(start_num, end_num, thread_num):    
    split_num = int((end_num-start_num)/thread_num)
    q = Queue(maxsize=thread_num)
    for _ in range(q.maxsize):
        driver = webdriver.Chrome('./driver/chromedriver.exe'
                                 , options = options
                                 )
        q.put(driver)
        
    with ThreadPool(thread_num) as tp:
        user_data = tp.starmap(
            user_info
            , [
                (login(q.get()), df[start_num+i*split_num:start_num+(i+1)*split_num])
                                  for i in range(0,thread_num)
            ]
        )
    pre_df_lst = list(zip(*user_data))
    df_true = pd.concat(pre_df_lst[0])
    df_false = pd.concat(pre_df_lst[1])
    return (df_true, df_false)
```


```python
df[5000:10000]
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
      <td>5000</td>
      <td>yKZx3wk4Gx4dJ</td>
      <td>1473.0</td>
    </tr>
    <tr>
      <td>5001</td>
      <td>DgwxAP6Am5rMj</td>
      <td>1473.0</td>
    </tr>
    <tr>
      <td>5002</td>
      <td>6ADvGpZPd5zZl</td>
      <td>1472.0</td>
    </tr>
    <tr>
      <td>5003</td>
      <td>4WLxZddomvroA</td>
      <td>1472.0</td>
    </tr>
    <tr>
      <td>5004</td>
      <td>8nPvy1kmDvYo0</td>
      <td>1472.0</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>9995</td>
      <td>yKZx3rl0Z54dJ</td>
      <td>1199.0</td>
    </tr>
    <tr>
      <td>9996</td>
      <td>7gdxd39yy5GYJ</td>
      <td>1199.0</td>
    </tr>
    <tr>
      <td>9997</td>
      <td>JgkqlAzWavX0b</td>
      <td>1199.0</td>
    </tr>
    <tr>
      <td>9998</td>
      <td>nb4xk9Yj3vOAz</td>
      <td>1198.0</td>
    </tr>
    <tr>
      <td>9999</td>
      <td>nb4xk0b0GqOAz</td>
      <td>1198.0</td>
    </tr>
  </tbody>
</table>
<p>5000 rows × 2 columns</p>
</div>




```python
# ======================
start_num = 170000
end_num = 170100
    
jump = 20 # 컴퓨터를 빨리 종료해야되는 경우에만 수를 적게 입력(driver가 자주 켜지면서 속도 감소하기 때문)
thread_num = 5
# ======================
for i in tqdm_notebook(range(int((end_num-start_num)/jump))):
    user_ratings = run_get_user_data(start_num + i*jump , start_num + (i+1)*jump, thread_num)
    if user_ratings[1].empty:
        user_ratings[0].to_csv(f'./watcha_user/temp2/user_data{start_num + i*jump}-{start_num + (i+1)*jump}.csv')
    else:
        user_ratings[0].to_csv(f'./watcha_user/temp2/user_data{start_num + i*jump}-{start_num + (i+1)*jump}.csv')
        user_ratings[1].to_csv(f'./watcha_user/temp3/error_user_data{start_num + i*jump}-{start_num + (i+1)*jump}.csv')
```


    HBox(children=(IntProgress(value=0, max=5), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))


    user_id :  ld0q0Z9pE56Xn 평가한 영화 개수 :  102
    user_id :  a9L5PZeMPqwg8 평가한 영화 개수 :  102
    user_id :  eVRZv4BZxr6yd 평가한 영화 개수 :  102
    user_id :  17ovVX1APxzyn 평가한 영화 개수 :  102
    user_id :  j4PxOMVNovp0Q 평가한 영화 개수 :  102
    user_id :  ZWpqM3KJl5rkn 평가한 영화 개수 :  102
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 1번째 재실행 중(오차 -48개)
    =============================================================
    user_id :  WRQxDMyzKmqdl 평가한 영화 개수 :  102
    user_id :  j4PxOn8wd5p0Q 평가한 영화 개수 :  102
    user_id :  VRZv474a1qr6y 평가한 영화 개수 :  102
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 2번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 3번째 재실행 중(오차 -48개)
    =============================================================
    user_id :  8nPvyeNPkvYo0 평가한 영화 개수 :  102
    user_id :  Q9L5p9y3KxNb0 평가한 영화 개수 :  102
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 4번째 재실행 중(오차 -48개)
    =============================================================
    user_id :  j4PxOn2pA5p0Q 평가한 영화 개수 :  102
    user_id :  zNM5Nj7y3526j 평가한 영화 개수 :  102
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 5번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 6번째 재실행 중(오차 -48개)
    =============================================================
    user_id :  yKZx32kyo54dJ 평가한 영화 개수 :  102
    
    user_id :  3BnvwnleBqPAY 평가한 영화 개수 :  102
    
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 7번째 재실행 중(오차 -48개)
    =============================================================
    user_id :  NP9vL2XOrox6k 평가한 영화 개수 :  102
    
    user_id :  WRQxDYzw6qdl9 평가한 영화 개수 :  102
    
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 8번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 9번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 10번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 11번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 12번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 13번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 14번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 15번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 16번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 17번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 18번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 19번째 재실행 중(오차 -48개)
    =============================================================
    =============================================================
    JgAx8b48OvLbO : 개수가 맞지않아 20번째 재실행 중(오차 -48개)
    =============================================================
    JgAx8b48OvLbO : 반복 횟수가 20번을 넘어 다음으로 넘어감(별도 저장됨)
    user_id :  Pznx9KnQkJv76 평가한 영화 개수 :  102
    user_id :  VRZv40Mmbvr6y 평가한 영화 개수 :  102
    
    


    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))


    user_id :  JZ4vBQQ34qRXO 평가한 영화 개수 :  102
    user_id :  8nPvyYrbOEvYo 평가한 영화 개수 :  102
    user_id :  YMKqmALVGqloD 평가한 영화 개수 :  102
    user_id :  YaR5YNAEoxgX1 평가한 영화 개수 :  102
    user_id :  jae5Wad0Xq1P3 평가한 영화 개수 :  102
    user_id :  6ewxayWmOxQ1m 평가한 영화 개수 :  102
    user_id :  jae5WlGZPx1P3 평가한 영화 개수 :  102
    user_id :  nb4xkGBZGxOAz 평가한 영화 개수 :  102
    user_id :  36lvXpwogvXdn 평가한 영화 개수 :  102
    user_id :  ld0q0l6LQq6Xn 평가한 영화 개수 :  102
    user_id :  Q9L5pky8KvNb0 평가한 영화 개수 :  102
    user_id :  VRZv46YkZxr6y 평가한 영화 개수 :  102
    user_id :  WwRqoGX4VqlzB 평가한 영화 개수 :  102
    user_id :  zNM5NjJGG526j 평가한 영화 개수 :  102
    user_id :  YaR5Y6loGxgX1 평가한 영화 개수 :  102
    user_id :  R6OvK2oW6qN8V 평가한 영화 개수 :  102
    
    user_id :  Mr95nJpBm95ZP 평가한 영화 개수 :  102
    
    user_id :  RE952Z2XZ5Q72 평가한 영화 개수 :  102
    
    user_id :  87Gv7dQGm5E6o 평가한 영화 개수 :  102
    
    user_id :  j4PxOyBZLvp0Q 평가한 영화 개수 :  102
    
    


    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))


    user_id :  2mwvgYjWgxMa7 평가한 영화 개수 :  102
    user_id :  JgkqleOgnvX0b 평가한 영화 개수 :  102
    user_id :  6ewxa4B485Q1m 평가한 영화 개수 :  102
    user_id :  87Gv7doDD5E6o 평가한 영화 개수 :  102
    user_id :  WRQxD6n2mvdl9 평가한 영화 개수 :  102
    user_id :  djaxbXPbMvLw8 평가한 영화 개수 :  102
    user_id :  JgkqlrKnb5X0b 평가한 영화 개수 :  102
    user_id :  jae5W3yV651P3 평가한 영화 개수 :  102
    user_id :  17ovVrbY4vzyn 평가한 영화 개수 :  102
    user_id :  dP8v6Xa8axWeJ 평가한 영화 개수 :  102
    user_id :  4WLxZDjbmvroA 평가한 영화 개수 :  102
    user_id :  Jgkqlr26D5X0b 평가한 영화 개수 :  102
    user_id :  RE952QP9lvQ72 평가한 영화 개수 :  102
    user_id :  ZWpqM84ERxrkn 평가한 영화 개수 :  102
    user_id :  2mwvgPpn35Ma7 평가한 영화 개수 :  102
    user_id :  WRQxDy72Dqdl9 평가한 영화 개수 :  102
    
    user_id :  djaxbrXWRkxLw 평가한 영화 개수 :  102
    
    user_id :  WRQxDo7865dl9 평가한 영화 개수 :  102
    
    user_id :  g64qz0GJR5ER0 평가한 영화 개수 :  102
    
    user_id :  3BnvwNWjOqPAY 평가한 영화 개수 :  102
    
    


    ---------------------------------------------------------------------------

