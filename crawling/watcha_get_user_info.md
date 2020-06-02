```python
import numpy as np
from pandas import DataFrame, Series
import pandas as pd

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

import time

from tqdm import tqdm_notebook

from queue import Queue
from multiprocessing.pool import ThreadPool

class User:
    def __init__(self, path):
        self.df = pd.read_csv(path, index_col=0)

    def login(self, driver):
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