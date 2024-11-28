import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import HtmlTestRunner
import time

class Mypage(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://member.myrealtrip.com/mypage")

        self.login()

    def login(self):
        
        time.sleep(2)
        
        login_email = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/fieldset/div[3]/div[3]/button')
        login_email.click()

        id_box = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))
        )
        id_box.click()
        id_box.send_keys("email")

        pw_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))
        )
        pw_box.click()
        pw_box.send_keys("pw")

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/form/div[4]/div/button[1]')
        login_btn.click()

        time.sleep(2)

    #마이페이지 진입
    def test_001_Login_Check_URL(self):
        print("Starting test_001")

        # 현재 URL 확인
        get_url = self.driver.current_url

        # 상태 코드 확인
        response = requests.get(get_url)

        # 조건 검증
        self.assertTrue(get_url == "https://member.myrealtrip.com/mypage" and response.status_code == 200)

    #이메일 수신 동의
    def test_002_Emailmarketing_Agree_Check(self):
        print("Starting test_002")

        #이메일 수신 동의 체크
        email_marketing_agree = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/main/div[3]/form/div[1]/div[2]/button')
        email_marketing_agree.click()
        
        time.sleep(2)

        #확인 알럿
        alret01 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/footer/div/button'))
        )
        alret01.click()

        # 현재 URL 확인
        get_status = email_marketing_agree.get_attribute('data-state')

        # 조건 검증
        self.assertTrue(get_status == "checked")



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(open_in_browser=True))