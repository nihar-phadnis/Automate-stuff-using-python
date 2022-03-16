# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:00:31 2022

@author: Nihar Phadnis
"""

import os
import smtplib
from email.message import EmailMessage
import imghdr

email_address = os.environ.get('email')
password = os.environ.get('pass')

contacts =  ["youraddress@example.com", "anotheraddress@example"]

msg = EmailMessage()
msg['Subject'] = 'Profile picture options. Sent using python'
msg['From'] = email_address
msg['To'] = (contact for contact in contacts) #as we are sending to multiple contacts
msg.set_content("Here's the images you asked for..")

files = ['unnamed.jpg', 'photo.jpg']

#to send more than 1 image over gmail, we use for loop 

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
    

    msg.add_attachment(file_data, maintype = "image", subtype=file_type, filename = f.name)

#we connect to the gmail port as we are sending over gmail
#we also use a context manager as this itself closes our application rather than us us doing manually

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, password)
    
    smtp.send_message(msg)
