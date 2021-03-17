import selenium.webdriver as webdriver
from time import sleep

search_word = "Hemangani"
driver = webdriver.Chrome('C:/Users/91938/Desktop/GIT_HUB/chromedriver.exe')
driver.get("https://www.google.com/search?q="+search_word)
sleep(2)

links = driver.find_elements_by_xpath('//div[@class="yuRUbf"]//a')
urls = []
for i in range(min(len(links),5)):
    urls.append(links[i].get_attribute("href"))
print(urls)
driver.close()