import email.message
import smtplib

def send_certification_letter(userEmail, randomNumber):
	password = 'oexjbuezcgbmzlfs'
	account = 'yali860208@gmail.com'

	msg = email.message.EmailMessage()

	msg['From'] = 'yali860208@gmail.com'
	msg['To'] = userEmail
	msg['Subject'] = 'HP2020LineBot 認證碼'

	content = '您好，歡迎註冊HP2020LineBot\n\t你的認證碼是：{}'.format(randomNumber)

	msg.set_content(content)

	server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server.login(account, password)
	server.send_message(msg)
	server.close()