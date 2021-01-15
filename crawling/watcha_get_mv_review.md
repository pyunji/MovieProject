```python
"""
watcha_mv_code_sort_by_voter_final.csv 파일 사용

"""
```


```python
# !pip install selenium
```


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

from selenium.common.exceptions import WebDriverException
```


```python
df = pd.read_csv('./watcha_mv_code_sort_by_voter_final.csv', index_col=0)
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
from tqdm import tqdm_notebook
```


```python
from selenium.webdriver.common.keys import Keys
```


```python
def get_review(driver, df):
    """review 가져와 저장하는 함수"""
    # 빈 리스트에 해당 범위의 영화코드의 리뷰 관련된 것 들 다 담을거임
    try:
        list_=[]

        for code in tqdm_notebook(df['movie_code']):
            lst = []
            url = f'https://watcha.com/ko-KR/contents/{code}/comments'
            driver.get(url)
            try:
            # 코멘트가 없는 영화의 경우 다음과 같이 설정 후 다음 영화코드로 넘어간다.
                driver.find_element_by_class_name('css-wnwcvo-Comment')
            except NoSuchElementException:
                list_.append((code, np.nan, np.nan, np.nan, np.nan, np.nan))
                # 다음 영화코드로 실행 재개
                continue
            # scroll height 가져오기
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                # 아래로 Scroll down -> scroll height 갱신
                driver.execute_script(f"window.scrollTo(0, {last_height});")
    #             time.sleep(0.5)
                # Wait to load page
                # explicitly wait. 코드를 넣은 위치에서만 wait
                try:
                    WebDriverWait(driver, 2).until(
                        # comment box가 모두 존재할 때 까지 기다렷
                        # x는 driver 일..걸..?
                        lambda x : x.execute_script("return document.body.scrollHeight") != last_height
                        # 불리언 타입이 이 곳에 들어갈 순 없고, driver가 연관된 함수만 들어올 수 있다.
                        # last_height != driver.execute_script("return document.body.scrollHeight")
                    )
                except TimeoutException:
                    break
                # new scroll height과 last scroll height 비교-> 맨 밑일때 break.
                new_height = driver.execute_script("return document.body.scrollHeight")
                last_height = new_height
            # co_box(comment box) -> 아직 특성별로 정제되지 않은 상태
            co_box = driver.find_elements_by_class_name('css-wnwcvo-Comment')
            for box in co_box:        
                # href 맨 마지막 자리에 아이디 존재
                id_ = box.find_element_by_class_name('css-1f9m1s4-StylelessLocalLink'
                                                    ).get_attribute('href').split('/')[-1]
                # title에 닉네임 존재
                nick_name = box.find_element_by_class_name('css-1f9m1s4-StylelessLocalLink'
                                                          ).get_attribute('title')
                # em 태그에 좋아요 수 존재
                like = box.find_element_by_tag_name('em').text

                # comment에 spoiler 있는 경우    
                try:
                    comment = box.find_element_by_class_name('css-o67ghx-Text-handleRenderInner').text    
                except NoSuchElementException:
                    # spoiler는 더보기 버튼 안누르면 클래스가 다른 클래스명으로 obscure.
                    # spoiler가 포함 된 comment는 더보기를 안누르면 가져올 수 없게 hidden.
                    # 더보기 버튼 눌러서라도 가져옴
                    xpath_view = """//*[@id="root"]/div/div/section/section/div/div/div/ul/div/div/span/button"""
                    driver.find_element_by_xpath(xpath_view).send_keys(Keys.ENTER)
                    time.sleep(0.2)
                    comment = box.find_element_by_class_name('css-o67ghx-Text-handleRenderInner').text    
                try:
                # 코멘트는 하고 별점은 안 준 경우
                    star = box.find_element_by_class_name('css-1eyufz5-UserActionStatus').text
                except NoSuchElementException:    
                    star = np.nan
                # 결측치 발생 우려해 tuple로 묶어서 저장
                lst.append((code, id_, nick_name, star, comment, like))
            print(code, len(lst))
            list_ = list_+lst
        # kwrd(keyword) : 컬럼명 지정해준 것임
        kwrd = ['movie_code', 'id', 'nick_name', 'ratings', 'comment', 'like']
        # cont(contents) : 컬럼명에 해당하는 내용 담을것임.
        # list_내의 tuple에는 정확히 5개의 원소가 들어가므로 이들을 각각 묶어서 분류
        cont = list(zip(*list_))
        # DataFrame으로 만들어 return.
        # 한개의 코드마다 한개의 DataFrame생성됨.
        # 이후 리스트에 다 담아서 한번에 concat하면됨
    except WebDriverException:
        print('WebDriverException 발생!!! : ', code)
    finally:
        driver.quit()
    return DataFrame(dict(zip(kwrd, cont)))
```


```python
from queue import Queue

from multiprocessing.pool import ThreadPool
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
# -편현지
options.add_argument("--disable-web-security")
```


```python
def run_save_review(start_num, end_num):
    """두 argument의 차이가 5의 배수여야 정상적 작동 가능"""
    split_num = int((end_num-start_num)/5)

    q = Queue(maxsize = 5)
    for _ in range(q.maxsize):
        driver = webdriver.Chrome('./driver/chromedriver.exe'
                                  , options = options
                                 ) 
        q.put(driver)

    with ThreadPool(5) as tp:
        reviews = tp.starmap(
            get_review
            , [
                (login(q.get()), df[start_num+i*split_num:start_num+(i+1)*split_num])
                 for i in range(0, 5)
            ]    
        )

    ext_reviews = pd.concat(reviews).reset_index()
    del ext_reviews['index']

    ext_reviews.to_csv(f'./mv_review/mv_review{start_num}-{end_num-1}.csv')    
```


```python
# #======================================
# #사용자 지정값 (여기만 바꾸면 됩니다~)
# start_num = 10000
# end_num = 10010
# #======================================
# run_save_review(start_num, end_num)
```


```python
# 0~500, 100
# ===================================
first_num=50000
last_num=55000
split_num =100
# ===================================

num_list = [(first_num+i*split_num, first_num+(i+1)*split_num) for i in range(int((last_num-first_num)/split_num))]

for start_num, end_num in num_list:
    run_save_review(start_num, end_num)
    # num_list    
```


```python
# df1_timeout=5 : 72823개 , 대략 2시간
```


```python
pd.read_csv('./mv_review/mv_review_before/mv_review1100-1109.csv', index_col=0)
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
      <td>m9dBPzW</td>
      <td>DgwxAeQYNxrMj</td>
      <td>이동진 평론가</td>
      <td>4.0</td>
      <td>여전히 로맨틱 코미디 장르를 대표하는 사랑스런 이름들.</td>
      <td>554</td>
    </tr>
    <tr>
      <td>1</td>
      <td>m9dBPzW</td>
      <td>R6OvKywXWxN8V</td>
      <td>윤지욱</td>
      <td>4.0</td>
      <td>안보일 때 생각나고 보고싶고, 같이 있으면 행복하고 외롭지 않게 하는 이성 친구가 ...</td>
      <td>406</td>
    </tr>
    <tr>
      <td>2</td>
      <td>m9dBPzW</td>
      <td>nb4xkkKmdxOAz</td>
      <td>황성욱</td>
      <td>4.0</td>
      <td>잠시 후, 사진 중앙에 앉아있는\n아주머니가 말한다.\n"나도 저 여자가 먹는 걸로...</td>
      <td>361</td>
    </tr>
    <tr>
      <td>3</td>
      <td>m9dBPzW</td>
      <td>ZBm5R4Vz9qd46</td>
      <td>청명이오빠</td>
      <td>4.0</td>
      <td>이덜 아이덜 니덜 나이덜 \n포테이로 포타로 틈메이러 틈마러</td>
      <td>241</td>
    </tr>
    <tr>
      <td>4</td>
      <td>m9dBPzW</td>
      <td>YMKqmnXjRvloD</td>
      <td>happy chu</td>
      <td>5.0</td>
      <td>요즘은 이런 로맨스를 찾아보기 힘들다</td>
      <td>201</td>
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
      <td>18183</td>
      <td>mO0gvBa</td>
      <td>ZBm5RnWEy5d46</td>
      <td>7785332</td>
      <td>2.5</td>
      <td>하...</td>
      <td>0</td>
    </tr>
    <tr>
      <td>18184</td>
      <td>mO0gvBa</td>
      <td>Pznx9Jlyzq761</td>
      <td>식식</td>
      <td>2.0</td>
      <td>너무 형편없다. 이런 영화가 더 괘씸하게 느껴진다. 여성원탑에 남자들을 죽이는 킬러...</td>
      <td>0</td>
    </tr>
    <tr>
      <td>18185</td>
      <td>mO0gvBa</td>
      <td>NP9vLoMNPq6kl</td>
      <td>수빈</td>
      <td>3.0</td>
      <td>신하균 드디어 볼만한걸 찍나요</td>
      <td>0</td>
    </tr>
    <tr>
      <td>18186</td>
      <td>mO0gvBa</td>
      <td>yKZx3ENjbv4dJ</td>
      <td>전여빈</td>
      <td>4.0</td>
      <td>김옥빈의 액션신에 박수를!!!!\n왜 악녀지 근데??</td>
      <td>-1</td>
    </tr>
    <tr>
      <td>18187</td>
      <td>mO0gvBa</td>
      <td>Mr95nXpzlqZPG</td>
      <td>부유물</td>
      <td>NaN</td>
      <td>음.....안보는 걸로...</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
<p>18188 rows × 6 columns</p>
</div>

