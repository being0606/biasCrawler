
def getScreen():
   
    from selenium import webdriver
    from time import sleep

    # 접속 url
    # 검색 키워드
    KEYWORD = "웹프로그래밍"
    URL = "https://google.com/search?q="+KEYWORD+"&tbm=isch"

    # 웹 드라이버 생성
    driver = webdriver.Chrome()

    # 링크 열기
    driver.get(URL)

    # 스크린샷 찍기
    screenshot_path = './screenshot.png'  # 원하는 경로를 지정하세요.
    driver.save_screenshot(screenshot_path)

    # 페이지 종료
    driver.quit()