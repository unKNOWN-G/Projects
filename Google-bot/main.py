import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

input_text = input("Enter Your Search Text : ")
driver = webdriver.Chrome('C:/Users/91938/Desktop/GIT_HUB/chromedriver.exe')
new_folder_path = 'C:/Users/91938/Desktop/{0}/'.format(input_text)
os.mkdir(new_folder_path)


def google_searcher(search_word):
    driver.get("https://www.google.com/search?q=" + search_word)
    sleep(2)
    sub_results = driver.find_elements_by_xpath("//div[@class='g']")
    n1 = min(5, len(sub_results))
    google_search_results = []
    print("----------------------------------------------------------------")
    print('Top {1} Google Search Results for "{0}" : '.format(search_word, n1))
    for i in range(n1):
        google_search_results.append(
            sub_results[i].find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute("href"))
        # driver.execute_script("window.open('{0}');".format(results[i]))
        print(google_search_results[i])

