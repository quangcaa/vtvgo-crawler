from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time


def get_m3u8_url(page_url: str):
    # Tạo ChromeOptions và bật performance logging
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    # Khởi tạo WebDriver với options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(page_url)

    time.sleep(10)  # Chờ đủ thời gian để video đc load

    logs = driver.get_log('performance')

    m3u8_links = []
    for entry in logs:
        message = entry['message']
        if '.m3u8' in message:
            urls = re.findall(r'https[^"]+\.m3u8[^"]*', message)
            m3u8_links.extend(urls)

    driver.quit()

    if m3u8_links:
        return m3u8_links[0]
    return None
