							Whatsapp Messenger
							¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

Date - 18-01-2021															Author - unKNOWN-G

In this Project we would be automating python to send a birthday Wish "Voice" Message without any Human Intervention
Step-1 : Firstly, The message thats being typed by us is converted to audio format using librart gtts. That will then be saved in a local folder
Step-2 : Next step is the code opens the chrome driver in the computer. Searched "http://www.webwhatsapp.com" and then enters using the login details stored previous using the cookies(Skipping the QR code authentication)
Step-3 : Then it searches the contact name in the serch box
Step-4 : Then it attaches the audio file to the message and waits for 10s.
Step-5 : Then it sends the message to the user


Language Used : Python

 
  Update Count	   Date							Description
  ¯¯¯¯¯¯¯¯¯¯¯¯	   ¯¯¯¯							¯¯¯¯¯¯¯¯¯¯¯
	1	18-01-2021		In this update a Basic Code file which was able to send an Image input to a contact number was made
	2	19-01-2021		Found Some bugs of the code not able to detect contact if its not on the front page and mad changes to Search
	3	22-01-2021		Text to audio speech Converter is made
	4	23-01-2021		Errors in Finding the name box were partially rectified
	5	24-01-2021		Added the folders part where Images of the person can be included and coded for accesing them and sending them at a 2s delay


Advancements that can be made
1) Search for the contact photos in the gallery using CNN and Send it along with the message
2) Send Messages on a particular time
3) Keep all the Remainder Details in a Excel File and make the code recognize those dates autmatically and send messages
4) Keep this in some colab or something and make it automatic