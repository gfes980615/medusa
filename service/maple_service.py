from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
from model.bo import maple_bulletin
from repository.maple import add_to_maple_bulletin
from utils.file import readFile
import time
import re

options = Options()
webdriver_path = './chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
rootURL = "https://tw.beanfun.com/maplestory/"
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

def get_page_bulletin():
    # driver = webdriver.Chrome(executable_path=webdriver_path, options=options,chrome_options=chrome_options)
    # driver.get('https://tw.beanfun.com/maplestory/main')
    # firstPageResult = driver.page_source
    firstPageResult = readFile("maple.txt")
    result = get_bulletin_content([], firstPageResult)
    # for index in range(1):
    #     button = driver.find_element_by_xpath("//li[@class='page-item next']")
    #     driver.execute_script("arguments[0].click();", button)
    #     WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "mBulletin-items-link")))
    #     response_text = driver.page_source
    #     result = get_bulletin_content(result, response_text)
    
    add_to_maple_bulletin(result)

    # driver.close()
    return result

def get_bulletin_content(result, response_text):
    soup = BeautifulSoup(response_text, "html.parser")
    a_items = soup.select("a.mBulletin-items-link")
    
    for a_item in a_items:
        url = checkURL(a_item.get("href"))
        date = a_item.select("div.mBulletin-items-date")[0].text.strip()
        category = a_item.select("div.mBulletin-items-cate")[0].text.strip()
        title = a_item.select("div.mBulletin-items-title")[0].text.strip()
        result.append(maple_bulletin(url, date, category, title))
    
    return result

def checkURL(url):
    r = re.compile(r'https://(.*)')
    if r.match(url):
        return url
    else:
        return rootURL+url
