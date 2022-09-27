import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Erik Young'
email['to'] = 'receiver's email'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'Saitama'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('sender's email', 'password')
  smtp.send_message(email)
  smtp.quit()
  print('all good boss!')
