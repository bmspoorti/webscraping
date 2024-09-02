from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
import pandas as pd
 
# initialize an instance of the chrome driver (browser)
URL = r"https://www.sacnilk.com/news/List_of_MostFollowed_Instagram_Handle_in_World"
options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


driver.get(URL)
time.sleep(10)

top_100 = driver.find_elements(By.TAG_NAME, "tr")[1:]

ranks = []
handles = []
followers_counts = []
topics_list = []
countries = []

for celebrity in top_100:
    tdc = celebrity.find_elements(By.TAG_NAME, "td")
    rank = tdc[0].text
    handle = tdc[1].text
    followers = tdc[2].text
    topics = tdc[4].text
    country = tdc[5].text
    # print(rank, handle, followers, topics, country)
    ranks.append(rank)
    handles.append(handle)
    followers_counts.append(followers)
    topics_list.append(topics)
    countries.append(country)
    print(rank, handle, followers, topics, country)
driver.close() 

data = {'Rank': ranks, 'Handle': handles, 'Followers': followers_counts, 'Topics': topics_list, 'Country': countries}
df = pd.DataFrame(data)
print(df)
df.to_csv("sacnilk.csv", index=False)





# release the resources allocated by Selenium and shut down the browser
# driver.quit()