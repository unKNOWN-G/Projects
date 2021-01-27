from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import pandas as pd


# Text to Audio Converter using gTTs
def txt_to_audio_converter():
    language = 'en'
    output = gTTS(text=msg, lang=language, slow=False)
    output.save(file_dir + event + "/0 Audio.mp3")


# Function to Send Audio only When needed
def audio_sender(value):
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
        message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        sleep(2)
        message_box.send_keys(msg)

        # Code to CLick Send Button
        message_sender = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
        message_sender.click()
        sleep(2)


# Function to send "all media" only When needed
def media_sender(files, value):
    if value == 1:
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


# Function select the person/group name
def chat_selector(person_name):
    # Opening New chat Option
    user = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div/span')
    user.click()

    # Code to Find Element in the Search box
    search_box = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div['
                                              '1]/div/label/div/div[2]')
    search_box.click()
    search_box.send_keys(person_name)
    sleep(6)

    # Code to Click the Open first Chat box in Search Results
    opening_chat = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]')
    opening_chat.click()
    sleep(5)


# Main Function
def whatsapp_automater(name, audio_value, text_value, media_value):
    chat_selector(name)

    # Listing Files in the folder
    file_data = os.listdir(media_files)

    media_sender(file_data, media_value)
    audio_sender(audio_value)
    txt_sender(text_value)
    sleep(2)


# Initial Details
dir = "C:/Users/91938/Desktop/GIT_HUB/Projects/Whatsapp_Messenger/"
file_dir = dir +"Event/"
event = "Republic_Day"
contact_names = pd.read_csv(file_dir + event + "/Contact.csv")
msg = open(file_dir + event + "/txt.txt", "r").read()
media_files = file_dir + event + "/Media/"

# Adding Arguments to chrome browser so that it wont Crash
options = Options();
options.add_argument('--user-data-dir=./User_Data')
options.add_argument("start-maximized");
options.add_argument("disable-infobars");
options.add_argument("--disable-extensions");
options.add_argument("--disable-gpu");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--no-sandbox");
driver = webdriver.Chrome('C:/Users/91938/Desktop/GIT_HUB/chromedriver.exe', options=options)

# Open Website
driver.get('https://web.whatsapp.com/')
sleep(15)

# Code to Convert Text to Audio
txt_to_audio_converter()

# Code to Send To Multiple Contacts
for num in range(len(contact_names["Contact_name"])):
    whatsapp_automater(contact_names.iloc[num, 0], contact_names.iloc[num, 1], contact_names.iloc[num, 2],
                       contact_names.iloc[num, 3])

# Code to Close Driver
driver.close()
