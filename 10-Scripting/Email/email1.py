import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("sender's email", "password")
 
# message to be sent
message = "yup I sent this email via Python"
 
# sending the mail
s.sendmail("sender's email", "receiver's email", message)
 
# terminating the session
s.quit()


-----------------------------------------------------------------

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Erik Young'
email['to'] = 'receiver's email'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a python master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('sender's email', 'password')
  smtp.send_message(email)
  print('all good boss!')
