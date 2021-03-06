import os 
import smtplib
import imghdr #buat ngirim foto, buat ngasih tau file typenya
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('DB_USER')
EMAIL_PASSWORD = os.environ.get('DB_PASS')

contact = ['haekal.pythontest@gmail.com', 'haekalghfr@gmail.com']
subject = 'Lorem Ipsum'
body = ''

msg = EmailMessage()
msg['Subject'] = subject
msg['To'] = contact
msg['From'] = EMAIL_ADDRESS
msg.set_content(body)

msg.add_alternative("""
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html') #triple (") berarti ini bakal menjadi
#multi line strings
#entire string html diatas itu satu argumen

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)

    smtp.quit()