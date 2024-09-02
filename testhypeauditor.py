from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


# initialize an instance of the chrome driver (browser)
# for i in range(1,4):
driver = webdriver.Chrome(options=options)
# URL = f"https://hypeauditor.com/top-instagram/?p=1"
# driver.get(URL)
# driver.find_element(By.CSS_SELECTOR, "button.button.popup__button.button--theme-secondary.button--size-sm.button--tablet-grow").click()
# time.sleep(5)

# for i in range(2,5):    
#     URL2 = f"https://hypeauditor.com/top-instagram/?p={i}"
#     driver.get(URL2)
#     # inputs = driver.find_element(By.CLASS_NAME, "hype-form_input.js-error-wrap")
#     inputs = driver.find_elements(By.CSS_SELECTOR, "input.hype-input")
#     inputs[0].send_keys("bmspoortiaradhya2000@gmail.com")
#     # print(inputs.text)
#     time.sleep(100)
    # inputs[0] = driver.find_element(By.CSS_SELECTOR, "hype-form_input.js-error-wrap")
    # inputs[1] = driver.find_element(By.CSS_SELECTOR, "hype-form_input.js-error-wrap")
    # inputs.send_keys("bmspoortiaradhya2000@gmail.com")
    # inputs[1].send_keys("BMspoo@1204")
    # driver.find_element(By.CSS_SELECTOR, "button.button.button-big.button-block.js-btn-loader.js-disabled").click()

# driver.close()
    # visit your target site
# driver.get(URL)
# time.sleep(10)

    # scraping logic...

    # front page details
# top_list = driver.find_elements(By.CLASS_NAME, "row")[1:]

# for celebrity in top_list:
#     classes = celebrity.find_elements(By.CLASS_NAME, "row-cell")
#     # rank = classes[0].text
#     # img = classes[1].find_element(By.CLASS_NAME, "avatar.contributor__avatar.--circle").get_attribute("src")
#     name = classes[1].find_elements(By.CLASS_NAME, "avatar.contributor__avatar.--circle")
#     handle = classes[1].find_elements(By.CLASS_NAME, "contributor__name-content")
#     print(name , handle)


# release the resources allocated by Selenium and shut down the browser
# driver.quit()
    
for i in range(1,5):
    URL = f"https://hypeauditor.com/top-instagram/?p={i}"
    driver.get(URL)
    print("yes")

    if i == 1:
        driver.find_element(By.CSS_SELECTOR, "button.button.popup__button.button--theme-secondary.button--size-sm.button--tablet-grow").click()
    else:
        inputs = driver.find_elements(By.CSS_SELECTOR, "input.hype-input")
        inputs[0].send_keys("bmspoortiaradhya2000@gmail.com")
        inputs[1].send_keys("BMspoo@1204")
        # login = driver.find_element(By.CSS_SELECTOR, "button.button.button-big.button-block.js-btn-loader.js-disabled")
        inputs[1].send_keys(Keys.ENTER)
        time.sleep(15)
        print("done")


    top_list = driver.find_elements(By.CLASS_NAME, "row")[1:]

    for celebrity in top_list:
        classes = celebrity.find_elements(By.CLASS_NAME, "row-cell")
        rank = celebrity.find_element(By.TAG_NAME, "span").text
        img = celebrity.find_element(By.TAG_NAME, "img").get_attribute("src")
        handle = celebrity.find_element(By.CLASS_NAME, "contributor__name-content").text
        name = celebrity.find_element(By.CLASS_NAME, "contributor__title").text
        print(rank, name, img, handle)