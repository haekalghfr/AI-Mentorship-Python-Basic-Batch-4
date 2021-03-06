
import os #sebenernya ga harus tapi lebih baik taro sensitive
#information into environment variables
import smtplib

EMAIL_ADDRESS = os.environ.get('DB_USER')
EMAIL_PASSWORD = os.environ.get('DB_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp: #karena kita pake gmail
    #587 port number yg kita gunain soalnya kita gunain plain smtp
    smtp.ehlo() #identify ourselves with the email server we are
    #using
    #kalo pake SMTP_SSL port number nya 465 dan ga pake ehlo dan 
    #starttls
    smtp.starttls() #we encrypt our traffic
    smtp.ehlo() #re-run ehlo lagi to re-identify ourselves as an
    #encrypted connection

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Lorem Ipsum'
    body = 'Lorem Ipsum'

    msg = 'Subject: {}\n\n{}'.format(subject,body) #dua new lines biar masuk ke body
    

    smtp.sendmail(EMAIL_ADDRESS, 'haekal.pythontest@gmail.com', msg)
    #smtp.sendemail(SENDER,RECEIVER, msg)

    smtp.quit()




#references
#https://www.kite.com/python/answers/how-to-remove-newline-character-from-a-list-in-python#:~:text=Use%20str.,well%20as%20newline%20characters%20removed.
#automate the boring stuff with python AL SWEIGART
#https://www.youtube.com/watch?v=JRCJ6RtE3xU&ab_channel=CoreySchafer
