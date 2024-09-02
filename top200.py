from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pandas import DataFrame
import requests

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

ranks = []
imgs= []
names = []
handles= []
followers= []
countries= []
topics= []

driver = webdriver.Chrome()
URL = f"https://socialbook.io/instagram-channel-rank/top-200-instagrammers"
driver.get(URL)
time.sleep(10)

driver.find_element(By.CLASS_NAME, "got-it-btn.btn.btn-secondary.secondary").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "adroll_consent_button").click()
time.sleep(15)
# allow_all = driver.find_element(By.CLASS_NAME, "btn-light.btn[0]").click()
# time.sleep(15)

top_200 = driver.find_elements(By.TAG_NAME, "tr")
# print(len(top_200))

for celebrity in top_200:
    rank = driver.find_element(By.CLASS_NAME, "index.top3").text
    print(rank)

driver.close()