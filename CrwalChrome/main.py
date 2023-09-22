
def getScreen():
    from time import sleep
    import pandas as pd
    import tqdm
    from selenium import webdriver


    # CSV 파일 로드
    df = pd.read_csv('../DATA/job.csv')
    mini_df = df.head()
    print("CSV load complete")
    # START!
    for _ in df['English']:
        KEYWORD = _
        URL = "https://google.com/search?q="+KEYWORD+"&tbm=isch"

        # 웹 드라이버 생성
        driver = webdriver.Chrome()

        # 링크 열기
        driver.get(URL)
        driver.fullscreen_window()

        # 스크린샷 찍기
        screenshot_path = '../screenshot/job_' + KEYWORD + '.png'
        driver.save_screenshot(screenshot_path)

        # 페이지 종료
        driver.quit()


if __name__ == "__main__":
    getScreen()
    print("DONE!")
