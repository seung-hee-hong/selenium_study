import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import HtmlTestRunner

class Mainhome(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.myrealtrip.com")

    #메인홈에서 로고
    def test_001_Mainhome_Check_URL(self):
        print("Starting test_001")

        # 광고 닫기
        close_ad = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div[2]/div/div[2]/button[2]'))
        )
        close_ad.click()

        # 메인홈 로고 클릭
        main_logo = self.driver.find_element(By.XPATH, '//*[@id="mrt-main-header"]/nav/div[1]/button')
        main_logo.click()

        # 현재 URL 확인
        get_url = self.driver.current_url

        # 상태 코드 확인
        response = requests.get(get_url)

        # 조건 검증
        self.assertTrue(get_url == "https://www.myrealtrip.com/" and response.status_code == 200)

    
    #메인홈에서 항공 버티컬 클릭
    def test_002_Flight_Check_URL(self):
        print("Starting test_002")

        # 광고 닫기
        close_ad = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div[2]/div/div[2]/button[2]'))
        )
        close_ad.click()

        # 항공 버티컬 클릭
        flight_home = self.driver.find_element(By.XPATH, '//*[@id="mrt-main-header"]/div/nav/div/div[2]/a')
        flight_home.click()

        # 현재 URL 확인
        get_url = self.driver.current_url

        # 상태 코드 확인
        response = requests.get(get_url)


        # 조건 검증
        self.assertTrue(get_url == "https://flights.myrealtrip.com/air/b2c/AIR/INT/AIRINTTRP0100100000.k1?KSESID=air:b2c:SELK138RB:SELK138RB::00" and response.status_code == 200)

    #메인홈에서 숙소 버티컬 클릭
    def test_003_Accommodation_Check_URL(self):
        print("Starting test_003")

        # 광고 닫기
        close_ad = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div[2]/div/div[2]/button[2]'))
        )
        close_ad.click()

        # 숙박 버티컬 클릭
        accommodation_home = self.driver.find_element(By.XPATH, '//*[@id="mrt-main-header"]/div/nav/div/div[3]/a')
        accommodation_home.click()

        # 현재 URL 확인
        get_url = self.driver.current_url

        # 상태 코드 확인
        response = requests.get(get_url)

        # 조건 검증
        self.assertTrue(get_url == "https://accommodation.myrealtrip.com/union?isDomestic=false&exposureSubCategory=HOTEL_RESORT" and response.status_code == 200)

    #메인홈에서 투어티켓 버티컬 클릭
    def test_004_TourTickt_Check_URL(self):
        print("Starting test_004")

        # 광고 닫기
        close_ad = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div[2]/div/div[2]/button[2]'))
        )
        close_ad.click()

        # 투어티켓 버티컬 클릭
        flight_home = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mrt-main-header"]/div/nav/div/div[5]/a'))
        )
        flight_home.click()

        # 현재 URL 확인
        get_url = self.driver.current_url

        # 상태 코드 확인
        response = requests.get(get_url)

        # 조건 검증
        self.assertTrue(get_url == "https://www.myrealtrip.com/experiences/" and response.status_code == 200)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(open_in_browser=True))