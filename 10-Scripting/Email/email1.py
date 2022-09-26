# import smtplib

# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)
 
# # start TLS for security
# s.starttls()
 
# # Authentication
# s.login("erikyoung217@gmail.com", "pdzqxqsaubbbdknv")
 
# # message to be sent
# message = "yup I sent this email via Python"
 
# # sending the mail
# s.sendmail("erikyoung217@gmail.com", "panwarprerak98@gmail.com", message)
 
# # terminating the session
# s.quit()


# -----------------------------------------------------------------

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Erik Young'
email['to'] = 'panwarprerak98@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a python master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('erikyoung217@gmail.com', 'pdzqxqsaubbbdknv')
  smtp.send_message(email)
  print('all good boss!')