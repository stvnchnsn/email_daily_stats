import pickle
import os
import smtplib
import requests
import time
import numpy as np
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Email:
    def __init__(self):
        if not os.path.exists('creds.pk1'):
            print('path exists')
            self.Gmail = {}
            self.Gmail['email'] = ""
            self.Gmail['password'] = ""
            with open('creds.pk1','wb') as f:
                pickle.dump(self.Gmail, f)
        else:
            self.Gmail = pickle.load(open('creds.pk1', 'rb'))
            print('gmail loaded')
        self.smtpObj=smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.smtpObj.ehlo()
        self.smtpObj.login(self.Gmail['email'],self.Gmail['password'])
        
        
    def get_creds(self):
        return self.Gmail['email'], self.Gmail['password']
    
    def send_email(self,to_email,subject,body):
        self.to_email = to_email
        self.subject= "Subject: " + subject+ "\n"
        self.body = body
        self.email_msg = self.subject +self.body
        
        self.smtpObj.sendmail(self.Gmail['email'],self.to_email,self.email_msg)
        self.Obj.quit()
        

email = Email()
to_email = 'stvnchnsn@gmail.com'
subject = "Test"
message = "testing email"
email.send_email(to_email,subject, message)

