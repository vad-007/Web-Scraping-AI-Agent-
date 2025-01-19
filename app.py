from selenium import webdriver
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_wbsite(wbsite):
    print('Launching chrome browser...')
   
    chrome_driver_path = "chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver=webdriver.Chrome(service=Service(chrome_driver_path), options=options)


    try:
        driver.get(wbsite)
        print('Scraping website...')
        html = driver.page_source
        time.sleep(5)

        return html
    finally:
        driver.quit()
        





