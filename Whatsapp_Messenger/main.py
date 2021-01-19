from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome('C:/Users/91938/Desktop/chromedriver.exe',chrome_options=options)
driver.get('https://web.whatsapp.com/')
sleep(12)

file_path = "C:/Users/91938/Desktop/Wallpapers/1.png"
group_name = "Amma"

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(group_name))
user.click()

attachment_box = driver.find_element_by_xpath('//div[@title="Attach"]')
attachment_box.click()

image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(file_path)

sleep(3)

send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()

sleep(3)
text_box = driver.find_element_by_xpath('//div[@class="_2HE1Z _1hRBM"]')
text_box.send_keys("Yo")
#