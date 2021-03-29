from selenium import webdriver
from time import sleep

# Gmail Login Credentials
sender_email = " "
sender_password = " "

# Gmail text
receiver_email = " "
subject = " "
body = " "

# Chrome Driver
driverpath ='C:/Users/91938/Desktop/GIT_HUB/chromedriver.exe'

# Open Chrome
driver = webdriver.Chrome(driverpath)
driver.maximize_window()

# Open Gmail Page
driver.get("http://www.gmail.com")
sleep(2)

# Loginng in
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(sender_email)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(sender_password)
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
sleep(7)

# Compose
try:
    driver.find_element_by_css_selector('.z0>.L3').click()
except:
    driver.find_element_by_css_selector('.z0>.L3::before').click()
sleep(1)

# Close Browser
driver.close()