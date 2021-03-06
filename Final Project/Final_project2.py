import os 
import smtplib
import imghdr #buat ngirim foto, buat ngasih tau file typenya
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('DB_USER')
EMAIL_PASSWORD = os.environ.get('DB_PASS')

a = []

with open('receiver_list.txt','r') as contact:
    a = contact.readlines()
    
contact = []

for i in a:
    contact.append(i.strip())

subject = 'Lorem Ipsum'
body = 'Lorem Ipsum \n\nImage attached...'

msg = EmailMessage()
msg['Subject'] = subject
msg['To'] = contact
msg['From'] = EMAIL_ADDRESS
msg.set_content(body)
file_data1 = ['pemandangan_1.jpg','pemandangan_2.jpg']
file_data2 = ['pemandangan_1.pdf']


for file in file_data1:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name) #buat ngasih tau ini    
        #file type nya apa butuh kalo image
        #kalo misalnya pdf ga usah
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    #kalo misalnya pdf subtype='octet-stream' , maintype='application'

for file in file_data2:
    with open(file, 'rb') as f:
        file_data = f.read()    
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)


    smtp.quit()
