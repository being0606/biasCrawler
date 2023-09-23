from time import sleep
import pandas as pd
import tqdm
from selenium import webdriver
from bs4 import BeautifulSoup

def getScreen():
    # CSV 파일 로드
    df = pd.read_csv('../DATA/job.csv')
    mini_df = df.head()
    print("CSV load complete")

    # START!
    for _ in mini_df['English']:
        KEYWORD = _
        URL = "https://google.com/search?q="+KEYWORD+"&tbm=isch"

        # 웹 드라이버 생성
        driver = webdriver.Chrome()

        # 링크 열기
        driver.get(URL)
        driver.fullscreen_window()

        # 페이지의 HTML 가져오기
        html = driver.page_source

        # BeautifulSoup으로 파싱
        soup = BeautifulSoup(html, 'lxml')

        # 클래스 이름을 사용하여 이미지 태그를 선택합니다.
        img_tag = soup.find('img', class_='rg_i Q4LuWd')

        # 이미지의 Base64 데이터를 가져옵니다.
        if img_tag and 'src' in img_tag.attrs:
            base64_data = img_tag['src']
            print(f"이미지의 Base64 데이터: {base64_data}")
        else:
            print("이미지를 찾을 수 없습니다.")

        # 스크린샷 찍기
        screenshot_path = '../screenshot/job_' + KEYWORD + '.png'
        driver.save_screenshot(screenshot_path)

        # 페이지 종료
        driver.quit()



if __name__ == "__main__":
    getScreen()
    print("DONE!")
