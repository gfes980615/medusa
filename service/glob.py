from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

options = Options()
webdriver_path = '/usr/local/medusa/dist/chromedriver'
# webdriver_path = './chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def create_driver_conn(url):
    driver = webdriver.Chrome(executable_path=webdriver_path, options=options,chrome_options=chrome_options)
    driver.get(url)
    return driver