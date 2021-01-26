from gtts import gTTS
from selenium import webdriver
from time import sleep
import os
import pandas as pd

# Initial Details
file_dir = "C:/Users/91938/Desktop/GIT_HUB/Projects/Whatsapp_Messenger/Event/"
event = "Republic_Day"
contact_names = pd.read_csv(file_dir + event + "/Contact.csv")
msg = open(file_dir + event + "/txt.txt", "r").read()
media_files = file_dir + event + "/Media/"

# Text to Audio Converter
language = 'en'
output = gTTS(text=msg, lang=language, slow=False)
output.save(file_dir + event + "/0 Audio.mp3")

# Code to Save Login Details using cookies
options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome('C:/Users/91938/Desktop/GIT_HUB/chromedriver.exe', chrome_options=options)

# Open Website
driver.get('https://web.whatsapp.com/')
sleep(20)


# Function to Send Audio only When needed
def txt_to_audio(value):
    if value == 1:
        attachment_box = driver.find_element_by_xpath('//div[@title="Attach"]')
        attachment_box.click()
        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(file_dir + event + "/0 Audio.mp3")
        sleep(1)

        # Code to Send Media Files
        send_media_box = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
        send_media_box.click()
        sleep(2)


# Function to send Text only When needed
def txt_sender(value):
    if value == 1:
        # Code To send text message
        message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
        sleep(2)
        message_box.send_keys(msg)

        # Code to CLick Send Button
        message_sender = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
        message_sender.click()
        sleep(3)


# Main Function
def whatsapp_automater(name, audio_value, text_value):
    # Opening New chat Option
    user = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div/span')
    user.click()

    # Code to Find Element in the Search box
    search_box = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div['
                                              '1]/div/label/div/div[2]')
    search_box.click()
    search_box.send_keys(name)
    sleep(5)

    # Code to Click the Open first Chat box in Search Results
    opening_chat = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div['
        '1]/div/span/span')
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

    txt_to_audio(audio_value)

    txt_sender(text_value)


# Code to Send To Multiple Contacts
for num in range(len(contact_names["Contact_name"])):
    whatsapp_automater(contact_names.iloc[num, 0], contact_names.iloc[num, 1], contact_names.iloc[num, 2])

# Code to CLose Driver
driver.close()