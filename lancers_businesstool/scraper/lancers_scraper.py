import os
from time import sleep
from unicodedata import name

from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


'''
【取得】
ランサーズ: スクレイピング

【URL】
https://www.lancers.jp/

【コメント】
1. login
2. id・password 入力
3. 'スクレイピング'で検索
4. 一覧から詳細ページのURL取得
5. 詳細ページURLから各種レコード取得
'''

BASE_DIR = Path(__file__).resolve().parent.parent
print('BASE_DIR = ' + str(BASE_DIR))       # debug
DOTENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(DOTENV_PATH)

LANCERS_USER = os.environ.get("LANCERS_USER")
LANCERS_PASSWORD = os.environ.get("LANCERS_PASSWORD")


# options = Options()
# options.add_argument('--headless')        # ヘッドレスモード時, driverのoptionsに渡す.
# driver = webdriver.Chrome(executable_path="C:\Users\user\Desktop\div\__on_going\Lancers_businesstool\chromedriver",
#     options=options
# )
driver = webdriver.Remote(
    # command_executor=os.environ['SELENIUM_URL'],
    command_executor='http://172.17.0.3:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME.copy()
)       # <- docker

driver.implicitly_wait(15)

class LancersScraper:
    url = 'https://www.lancers.jp/'

    def __init__(self, driver):
        self.driver = driver
        self.project_df = pd.DataFrame(columns=['id', 'name', 'reward', 'descriptons', 'url', 'aplied', 'accepting', 'create_at', 'modified_at'])

        self.driver.get(self.url)

    def login(self):
        try:
            if self.driver.current_url == self.url:
                print(self.driver.current_url)
                print('during login process...')

                login_button = self.driver.find_element(By.CLASS_NAME, 'css-1eti57o')
                login_button.click()
                sleep(1)       # debug

                login_user_form = self.driver.find_element(By.NAME, 'data[User][email]')
                login_password_form = self.driver.find_element(By.NAME, 'data[User][password]')
                login_user_form.send_keys(LANCERS_USER)
                login_password_form.send_keys(LANCERS_PASSWORD)
                login_user_form.submit()
                sleep(1)       # debug

                if self.driver.find_element(By.CSS_SELECTOR, 'div.c-modal.p-mypage-modal.js-mypage-modal'):
                    close_button = self.driver.find_element(By.CSS_SELECTOR, 'button.c-modal__close.js-mypage-modal-close')
                    close_button.click()
                else:
                    pass
            else:
                print(str(self.driver.current_url))
                print('already logged in.')

        except Exception as e:
            print(e)
            driver.quit()

    def search_projects(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'span.css-v694h7').click()
            sleep(1)

            project_search_box = self.driver.find_element(By.CSS_SELECTOR, 'div.p-search-job__search-bar-inner.c-search-bar__inner.c-basic-search > input#Keyword')
            submit_button = self.driver.find_element(By.CSS_SELECTOR, 'div.p-search-job__search-bar-inner.c-search-bar__inner.c-basic-search > button#Search')
            project_search_box.send_keys('スクレイピング')
            submit_button.click()

        except Exception as e:
            print(e)
            driver.quit()

    def set_project_list(self):
        try:
            elems = self.driver.find_elements(By.CSS_SELECTOR, 'div.c-media__content__right > a.c-media__title')   
            for i, elem in enumerate(elems):
                name = elem.find_element(By.CSS_SELECTOR, 'span.c-media__title-inner').text
                # print(name)
                project_url = elem.get_attribute('href')
                # print(project_url)
                project_ser = pd.Series({
                    'name': name,  
                    'url': project_url
                })
                self.project_df = pd.concat([self.project_df, pd.DataFrame(project_ser).T])

        except Exception as e:
            print(e)
            driver.quit()
    
    def set_all_project_list(self):
        try:
            for i in range(3):
                self.set_project_list()
                WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, 'pager__item__anchor')))
                next_url = self.driver.find_element(By.CLASS_NAME, 'pager__item__anchor')
                if next_url:
                    next_url.click()
                else:
                    driver.quit()

        except Exception as e:
            print(e)
            driver.quit()

    def set_project_detail(self):
        pass

    def set_id(self):
        print(len(self.project_df))
        for i in range(len(self.project_df)):
            print(i)
            self.project_df.iloc[i, 0] = i

    # @property     # attributeerrorでるので要調査. おそらくdfを@prorertyすることで起こる.
    # def project_df(self):
    #     return self.project_df
    
LS = LancersScraper(driver)
LS.login()
LS.search_projects()
LS.set_all_project_list()
LS.set_id()
print(LS.project_df)       # debug

sleep(3)
driver.quit()