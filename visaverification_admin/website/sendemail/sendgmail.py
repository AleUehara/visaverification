#!/usr/bin/python
import smtplib
import sys

def send(password):
  print "Envia"
  print password
  SMTP_SERVER = 'smtp.gmail.com'
  SMTP_PORT = 587
 
  sender = 'alexpromo66@gmail.com'
  recipient = 'uehara.alexandre@gmail.com'
  subject = 'Gmail SMTP Test'
  body = 'blah blah blah'
 
  "Sends an e-mail to the specified recipient."
 
  body = "" + body + ""
 
  headers = ["From: " + sender,
             "Subject: " + subject,
             "To: " + recipient,
             "MIME-Version: 1.0",
             "Content-Type: text/html"]
  headers = "\r\n".join(headers)
 
  session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
  session.ehlo()
  session.starttls()
  session.ehlo
  session.login(sender, password)
 
  session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
  session.quit()


if __name__ == '__main__':
    send(sys.argv[1])  