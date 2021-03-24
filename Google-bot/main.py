import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

search_word = input("Enter Your Search Text : ")
input_count = int(input("How many results do you need? "))
driver = webdriver.Chrome('C:/Users/91938/Desktop/GIT_HUB/chromedriver.exe')
new_folder_path = 'C:/Users/91938/Desktop/{0}/'.format(search_word)
os.mkdir(new_folder_path)
print("----------------------------------------------------------------")

def google_searcher(input_text,count):
    driver.get("https://www.google.com/search?q=" + input_text)
    sleep(1)
    sub_results = driver.find_elements_by_xpath("//div[@class='g']")
    n1 = min(count, len(sub_results))
    google_search_results = []
    print('Top {1} Google Search Results for "{0}" : '.format(input_text, n1))
    for i in range(n1):
        google_search_results.append(
            sub_results[i].find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute("href"))
        # driver.execute_script("window.open('{0}');".format(results[i]))
        print(google_search_results[i])
    print("----------------------------------------------------------------")

def youtube_searcher(input_text,count):
    driver.get("https://www.youtube.com/results?search_query=" + input_text)
    sleep(2)
    youtube_results = driver.find_elements_by_xpath("//div[@id='title-wrapper']")
    n2 = min(count, len(youtube_results))
    print('Top {1} Youtube Search Results for "{0}" : '.format(input_text, n2))
    youtube_search_results = [[0] * 2] * n2
    for i in range(n2):
        ## Title and Link

        t1 = youtube_results[i].find_element_by_xpath(".//a[@id='video-title']")
        youtube_search_results[i][0] = t1.get_attribute("title")
        youtube_search_results[i][1] = t1.get_attribute("href")
        # #driver.execute_script("window.open('{0}');".format(youtube_search_results[i]))
        print(youtube_search_results[i])
    print("----------------------------------------------------------------")

def google_scholar(search_word,count):
    driver.get("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + search_word + "&btnG=")
    sleep(1)
    sub_results = driver.find_elements_by_xpath("//h3[@class='gs_rt']/a")
    n1 = min(count, len(sub_results))
    google_scholar_results = []
    print('Top {1} Google Scholar Search Results for "{0}" : '.format(search_word, n1))
    for i in range(n1):
        google_scholar_results.append(sub_results[i].get_attribute("href"))
        # driver.execute_script("window.open('{0}');".format(results[i]))
        print(sub_results[i].text)
        print(google_scholar_results[i])
    print("----------------------------------------------------------------")
    return google_scholar_results

def sciHub(input_text,count):
    print("Downloads form Sci Hub XD")
    Link_elements = google_scholar(input_text,count)
    for i in range(len(Link_elements)):
        driver.get("https://sci-hub.do/" + Link_elements[i])
        sleep(2)
        try:
            pdf_download_link = driver.find_element_by_xpath('//*[@id="buttons"]/ul/li/a')
            pdf_download_link.click()
            print("PDF Downloaded")
        except:
            print(Link_elements[i])
    print("----------------------------------------------------------------")
        # driver.execute_script("window.open('{0}');".format(Link_elements[i]))

def google_image_screenshot_taker(input_text, count):
    os.mkdir(new_folder_path + 'photos')
    driver.get("https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl")
    image_url = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input').send_keys(input_text, Keys.ENTER)
    j = 0
    pred_count = count+int(count/25)+1
    for i in range(0,pred_count):
        if i % 25 == 0:
            print("Skipped ",i)
            continue
        else:
            try:
                driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').screenshot(
                    new_folder_path + 'photos/' + "{0}.png".format(j))
                j = j + 1
            except:
                try:
                    print("Arghh a problem at ",i)
                    driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[4]/div[2]/input').click()
                except:
                    pred_count = pred_count + 1
                    pass
    print("{0} Images of {1} hav been downloaded from google".format(j,input_text))
    print("----------------------------------------------------------------")


google_image_screenshot_taker(search_word,input_count)
google_searcher(search_word,input_count)
sciHub(search_word,input_count)
youtube_searcher(search_word,input_count)
