import selenium.webdriver as webdriver
from time import sleep

search_word = "Hema"
driver = webdriver.Chrome('C:/Users/91938/Desktop/GIT_HUB/chromedriver.exe')
driver.get('https://google.com')
sleep(4)
search_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
search_box.click()
search_box.send_keys(search_word)
clicker = driver.find_elements_by_xpath("//html/body/div[1]/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
clicker.click()

links = driver.find_element_by_xpath('//div[@class="yuRUbf"]//a')
for link in links:
    print(link.get_attribute("href"))