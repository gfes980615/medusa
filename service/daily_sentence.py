from .glob import create_driver_conn
from datetime import datetime
from bs4 import BeautifulSoup
from model.po import EnglishSentence

shanbayURL = "https://web.shanbay.com/op/quotes/"

def get_shanbay_daily_sentence():
    daily_url = set_daily_url()
    driver = create_driver_conn(daily_url)
    response_text = driver.page_source
    soup = BeautifulSoup(response_text, "html.parser")
    content = soup.select_one("div.quote p.content").getText()
    translation = soup.select_one("div.quote p.translation").getText()
    poItem = EnglishSentence(get_current_date(), content, translation)
    poItem.addItem()

def set_daily_url():
    date = get_current_date()
    return shanbayURL+date

def get_current_date():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    return date
