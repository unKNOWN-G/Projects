from gtts import gTTS
from selenium import webdriver
from time import sleep
import os

# Initial Details
file_dir = "C:/Users/91938/Desktop/GIT_HUB/Projects/Whatsapp_Messenger/Birthday/"
contact_name = "Daddy"
msg = open(file_dir + contact_name + "/txt.txt", "r").read()
media_files = file_dir + contact_name + "/Media/"

# Text to Audio Converter
language = 'en'
output = gTTS(text=msg, lang=language, slow=False)
output.save(media_files + "0 Audio.mp3")

# Code to Save Login Details using cookies
options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome('C:/Users/91938/Desktop/chromedriver.exe', chrome_options=options)

# Open Website
driver.get('https://web.whatsapp.com/')
sleep(10)

# Code to Find Element in the Search box
user = driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"]')
user.send_keys(contact_name)
user.click()
sleep(15)

# Code to Click the Open first Chat box in Search Results
opening_chat = driver.find_element_by_xpath(
    '//*[@id="pane-side"]/div[1]/div/div/div[15]/div')
opening_chat.click()
sleep(5)

# Listing Files in the folder
files = os.listdir(media_files)

for i in range(len(files)):
    attachment_box = driver.find_element_by_xpath('//div[@title="Attach"]')
    attachment_box.click()
    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(media_files + files[i])
    sleep(1)

    # Code to Send Media Files
    send_media_box = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
    send_media_box.click()
    sleep(2)
sleep(2)

# Code To send text message
message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
sleep(2)
message_box.send_keys(msg)

# Code to CLick Send Button
message_sender = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
message_sender.click()
sleep(3)

# Code to CLose Driver
driver.close()
