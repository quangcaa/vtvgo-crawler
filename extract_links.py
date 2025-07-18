from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def get_video_links(category_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(category_url)
    time.sleep(3)  # chờ load ban đầu

    SCROLL_PAUSE_TIME = 2
    seen_links = set()
    retry_same_height = 0
    max_retries = 5

    while retry_same_height < max_retries:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        current_links = set(
            "https://vtvgo.vn" + a["href"]
            for a in soup.find_all("a", href=True)
            if "/video/play/" in a["href"]
        )

        new_links = current_links - seen_links
        if new_links:
            seen_links.update(new_links)
            retry_same_height = 0  # reset nếu có thêm video mới
        else:
            retry_same_height += 1  # ko có thêm video → tăng retry

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

    driver.quit()
    return list(seen_links)
