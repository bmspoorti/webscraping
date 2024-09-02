from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from pandas import DataFrame
import requests

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome()
URL = f"https://www.mykhel.com/cricket/most-runs-in-odi-rs1/"
driver.get(URL)
time.sleep(10)


driver.find_element(By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button").click()
time.sleep(10)

# driver.find_element(By.LINK_TEXT, "https://www.mykhel.com/cricket/")
# time.sleep(10)
# driver.find_element(By.LINK_TEXT, "https://www.mykhel.com/cricket/records-stats/")
# time.sleep(10)
# driver.find_element(By.LINK_TEXT, "https://www.mykhel.com/cricket/most-runs-in-odi-rs1/")
# time.sleep(10)

cricketers = driver.find_elements(By.TAG_NAME, "tr")
print(len(cricketers))
driver.close()
