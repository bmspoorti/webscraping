from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from pandas import DataFrame
import requests

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome()
URL = f"https://www.bcci.tv/stats/odi?platform=international&type=men"
driver.get(URL)
time.sleep(10)

rank = []
name = []
match = []
inning = []
average = []
strike_rate = []
hundred = []
four = []
fifty = []
six = []

# bcci_header =  driver.find_elements(By.CSS_SELECTOR, "div.imw-tabs.international-tabs")
# bcci_header[0].find_element(By.CSS_SELECTOR, "div.click_menu(this)")
# ODI = driver.find_element(By.LINK_TEXT, "https://www.bcci.tv/stats/odi?platform=international&type=men").click()

players = driver.find_elements(By.TAG_NAME, "tr")

for player in players:
    tds = player.find_elements(By.TAG_NAME, "td")
    info = player.find_elements(By.TAG_NAME, "h6")
    # print(len(tds))
    # for td in tds:
    #     print(td.text)
    Rank = tds[0].text
    Name = tds[1].text
    Matches = info[0].text
    Innings = info[1].text
    Average = info[2].text
    Strike_rate = info[3].text
    Hundreds = info[4].text
    Fours = info[5].text
    Fifties = info[6].text
    Sixes = info[7].text
    rank.append(Rank)
    name.append(Name)
    match.append(Matches)
    inning.append(Innings)
    average.append(Average)
    strike_rate.append(Strike_rate)
    hundred.append(Hundreds)
    four.append(Fours)
    fifty.append(Fifties)
    six.append(Sixes)

    # Runs = tds[10].text
    # Runs_inngs = tds[11].text

    print(Rank, Name, Matches, Innings, Average, Strike_rate, Hundreds, Fours, Fifties)
driver.close()

df = DataFrame({"Rank": rank, "Name": name, "Matches": match, "Innings": inning, "Average": average, "Strike_Rate" : strike_rate,
                "Hundreds": hundred, "Fours": four, "Fifties": fifty, "Sixes": six})
print(df)
df.to_csv("bcci.csv", index=False)
