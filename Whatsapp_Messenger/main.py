from gtts import gTTS

language = 'en'
output = gTTS(text="Worst fellow pora", lang=language,slow=False)

output.save("C:/Users/91938/Desktop/test.mp3")


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome('C:/Users/91938/Desktop/chromedriver.exe',chrome_options=options)
driver.get('https://web.whatsapp.com/')
sleep(7)

file_path = "C:/Users/91938/Desktop/test.mp3"
group_name = "Wangmai"

user = driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"]')
user.send_keys(group_name)
user.click()

sleep(1)
opening_chat = driver.find_element_by_xpath('//div[@class="_7W_3c"]')
opening_chat.click()



attachment_box = driver.find_element_by_xpath('//div[@title="Attach"]')
attachment_box.click()

image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(file_path)
# message_box = driver.find_element_by_xpath('//div[@class="_2HE1Z ugx-m QkEzS"]')
# sleep(2)
# message_box.send_keys("Hiiiiii")
sleep(10)
text_box = driver.find_element_by_xpath('//span[@data-icon="send"]')
text_box.click()

# message_sender = driver.find_element_by_xpath('//span[@data-icon="send"]')
# message_sender.click()
# sleep(3)
#
# send_button.click()
#

# #