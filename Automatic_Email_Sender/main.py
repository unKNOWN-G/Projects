from selenium import webdriver
from time import sleep
import pandas as pd

# Gmail Login Credentials
sender_email = "sender@gmail.com"
sender_password = "sender_passoword"

# Gmail text
subject = "Mail_subject"
body = "Mail_body"

# Read Emails
contact_emails = pd.read_csv("./Recipients_list.csv")
Emails = contact_emails["Email"]
print(Emails)

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


for i in range(len(Emails)):
    # Compose
    try:
        driver.find_element_by_css_selector('.z0>.L3').click()
    except:
        driver.find_element_by_css_selector('.z0>.L3::before').click()
    sleep(1)

    # Input Recipient
    driver.find_element_by_css_selector(".oj div textarea").send_keys(Emails[i])
    sleep(0.5)

    # Input Subject
    driver.find_element_by_css_selector(".aoD.az6 input").send_keys(subject)
    sleep(0.5)

    # Input Text
    driver.find_element_by_css_selector(".Ar.Au div").send_keys(body)
    sleep(0.5)

    print("Email Sent to " + Emails[i])

# Close Browser
driver.close()