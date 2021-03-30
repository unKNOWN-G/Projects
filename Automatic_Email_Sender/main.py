from EmailSender import EmailSender
import pandas

# Read Emails
contact_emails = pandas.read_csv("./Recipients_list.csv")
Emails = contact_emails["Email"]

# Send Emails
mailer = EmailSender(sender_email=" ", sender_password=" ",
                     mail_subject=" ", mail_body=""" """)
mailer.send_mails(driver_path="./chromedriver.exe", emails=Emails)
