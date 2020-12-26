from .glob import create_driver_conn
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
from model.bo import maple_bulletin
from repository.mysql.maple import add_to_maple_bulletin, get_all_bulletin
from repository.redis.maple import redis_cache_maple_bulletin
from utils.file import readFile
import time
import re
from database.redis import r
import json

rootURL = "https://tw.beanfun.com/maplestory/"
mainURL = "https://tw.beanfun.com/maplestory/main"

def init_redis_bulletin():
    items = get_all_bulletin()
    for item in items:
        r.set(item.url, item.id)

def get_realtime_bulletin():
    driver = create_maple_driver_conn()
    firstPageResult = driver.page_source
    result, _ = get_bulletin_content(firstPageResult)
    unRecordResult = get_unRecord_bulletin(result)
    add_to_maple_bulletin(unRecordResult)
    redis_cache_maple_bulletin(unRecordResult)

    if len(unRecordResult) > 0:
        while True:
            driver = next_page_driver(driver)
            response_text = driver.page_source
            result, _ = get_bulletin_content(response_text)
            subUnRecordResult = get_unRecord_bulletin(result)
            if len(subUnRecordResult) == 0:
                break
            add_to_maple_bulletin(subUnRecordResult)
            redis_cache_maple_bulletin(subUnRecordResult)
            for sub in subUnRecordResult:
                unRecordResult.append(sub)

    driver.close()
    if len(unRecordResult) != 0:
        r.lpush("maple_bulletin", json.dumps(unRecordResult))

    return unRecordResult

def get_init_bulletin(date):
    driver = create_maple_driver_conn()
    firstPageResult = driver.page_source
    result, endDate = get_bulletin_content(firstPageResult)
    add_to_maple_bulletin(result)

    if endDate < date:
        print("")
    else:
        while True:
            driver = next_page_driver(driver)
            response_text = driver.page_source
            pageResult, endDate = get_bulletin_content(response_text)
            add_to_maple_bulletin(pageResult)

            if endDate < date:
                break 
    
    init_redis_bulletin()
    driver.close()
    return "done"

def get_unRecord_bulletin(result):
    unRecordResult = []
    for item in result:
        if r.get(item.url) == None:
            unRecordResult.append(item)
    return unRecordResult

def get_bulletin_content(response_text):
    soup = BeautifulSoup(response_text, "html.parser")
    a_items = soup.select("a.mBulletin-items-link")
    result = []
    endDate = ""
    for a_item in a_items:
        url = checkURL(a_item.get("href"))
        date = a_item.select("div.mBulletin-items-date")[0].text.strip()
        category = a_item.select("div.mBulletin-items-cate")[0].text.strip()
        title = a_item.select("div.mBulletin-items-title")[0].text.strip()
        result.append(maple_bulletin(url, date, category, title))
        endDate = replaceDate(date)
    
    return result, endDate

def create_maple_driver_conn():
    driver = create_driver_conn(mainURL)
    return driver

def next_page_driver(driver):
    button = driver.find_element_by_xpath("//li[@class='page-item next']")
    driver.execute_script("arguments[0].click();", button)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "mBulletin-items-link")))
    return driver

def checkURL(url):
    r = re.compile(r'https://(.*)')
    if r.match(url):
        return url
    else:
        return rootURL+url

def replaceDate(date):
    new_date = date.replace(".", "-")
    return new_date
