import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

input_text = input("Enter Your Search Text : ")
driver = webdriver.Chrome('C:/Users/91938/Desktop/GIT_HUB/chromedriver.exe')
new_folder_path = 'C:/Users/91938/Desktop/{0}/'.format(input_text)
# os.mkdir(new_folder_path)


def google_searcher(search_word):
    driver.get("https://www.google.com/search?q=" + search_word)
    sleep(2)
    sub_results = driver.find_elements_by_xpath("//div[@class='hlcw0c']")
    n1 = min(5, len(sub_results))
    google_search_results = []
    print("----------------------------------------------------------------")
    print('Top {1} Google Search Results for "{0}" : '.format(search_word, n1))
    for i in range(n1):
        google_search_results.append(
            sub_results[i].find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute("href"))
        # driver.execute_script("window.open('{0}');".format(results[i]))
        print(google_search_results[i])

def youtube_searcher(search_word):
    driver.get("https://www.youtube.com/results?search_query=" + search_word)
    sleep(2)
    youtube_results = driver.find_elements_by_xpath("//div[@id='title-wrapper']")
    n2 = min(5, len(youtube_results))
    youtube_search_results = {}
    print("----------------------------------------------------------------")
    print('Top {1} Youtube Search Results for "{0}" : '.format(search_word, n2))
    youtube_search_results = [[0] * 2] * n2
    for i in range(n2):
        ## Title and Link

        t1 = youtube_results[i].find_element_by_xpath(".//a[@id='video-title']")
        youtube_search_results[i][0] = t1.get_attribute("title")
        youtube_search_results[i][1] = t1.get_attribute("href")
        # #driver.execute_script("window.open('{0}');".format(youtube_search_results[i]))
        print(youtube_search_results[i])

def google_scholar(search_word,count):
    driver.get("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + search_word + "&btnG=")
    sleep(2)
    sub_results = driver.find_elements_by_xpath("//h3[@class='gs_rt']/a")
    n1 = min(count, len(sub_results))
    google_scholar_results = []
    print("----------------------------------------------------------------")
    print('Top {1} Google Search Results for "{0}" : '.format(search_word, n1))
    for i in range(n1):
        print(sub_results[i].text)
        google_scholar_results.append(sub_results[i].get_attribute("href"))
        # driver.execute_script("window.open('{0}');".format(results[i]))
        print(google_scholar_results[i])
    print("----------------------------------------------------------------")
    return google_scholar_results

