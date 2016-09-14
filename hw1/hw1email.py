import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def bananaReminder():
	person = raw_input("Enter your name: ")
	print("Hello, " + person + ".")

	breakfast = raw_input("What did you have for breakfast? ")

	if breakfast == "oats":
		print("Okay, " + person + ", you had "+ breakfast + " for breakfast.")
		question = raw_input("Did you run out of bananas again? y/n: ")
		if question == "y":
			print("You ran out of bananas again! Sending you a reminder now.")
			
			fromaddr = "brogj411@newschool.edu"
			toaddr = "brogj411@newschool.edu"
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = toaddr
			msg['Subject'] = "BANANAS"

			body = "Jason, don't forget to buy bananas."
			msg.attach(MIMEText(body, 'plain'))

			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(fromaddr, "PASSWORD")
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
			server.quit()

		else:
			print("You didn't run out of bananas this time!")
	else:
		print("Yum!")

bananaReminder()