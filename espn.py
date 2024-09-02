
from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from pandas import DataFrame

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome()
URL = f"https://www.espncricinfo.com/records/most-runs-in-career-83548"
driver.get(URL)
time.sleep(10)

driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
time.sleep(10)

names = []
matchs = []
inngs = []
run = []
hs = []
avg = []
sr = []
hundred = []
fifty = []
zero = []
four = []
six = []

players = driver.find_elements(By.TAG_NAME, "tr")

for player in players:
    tds = player.find_elements(By.TAG_NAME, "td")
    name = tds[0].text
    matches = tds[2].text 
    innings = tds[3].text
    runs = tds[5].text
    highest_score = tds[6].text
    average = tds[7].text
    strike_rate = tds[9].text
    hundreds = tds[10].text
    fifties = tds[11].text
    zeroes = tds[12].text
    fours = tds[13].text
    sixes = tds[14].text

    names.append(name)
    matchs.append(matches)
    inngs.append(innings)
    run.append(runs)
    hs.append(highest_score)
    avg.append(average)
    sr.append(strike_rate)
    hundred.append(hundreds)
    fifty.append(fifties)
    zero.append(zeroes)
    four.append(fours)
    six.append(sixes)

    print(name, matches, innings, runs, highest_score,average, strike_rate, hundreds, fifties, zeroes, fours, sixes)

driver.close()

df = DataFrame({ "Name": names, "Matches": matchs, "Innings": inngs, "Runs": run, "Highest_score": hs , "Average": avg, "Strike_Rate" : sr, 
                "Hundreds": hundred, "Fifties": fifty, "Zeroes": zero , "Fours": four, "Sixes": six})
print(df)
df.to_csv("espn.csv", index=True)




