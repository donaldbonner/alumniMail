#!/usr/bin/env python3
"""
Sample code from Scott Kuhls github
https://github.com/skuhl/autograder/blob/master/ag-email.py
"""

import sys, os
import getpass, smtplib

if sys.hexversion < 0x030000F0:
    print('This script requires Python 3')
    sys.exit(1)

emailSession = None

def emailLogin(senderEmail, mypassword):
    global emailSession
    emailSession = smtplib.SMTP('smtp.gmail.com', 587)
    emailSession.ehlo()
    emailSession.starttls()
    emailSession.ehlo
    emailSession.login(senderEmail, mypassword)

def emailLogout():
    global emailSession
    emailSession.quit()

def sendEmail(senderEmail, recipients, subject, body):
    headers = ['From: ' + senderEmail,
               'Subject: ' + subject,
               #'To: ' + ', '.join(recipients),  
               #Use this to send to a list of people
               'To: ' + recipients,
               'MIME-Version: 1.0',
               'Content-Type: text/plain']
    headers = '\r\n'.join(headers)
    global emailSession
    emailSession.sendmail(senderEmail, recipients, headers + '\r\n\r\n' + body)

print('Who is this sent to?')
recipientEmail = sys.stdin.readline().strip()

print('Enter the subject line for the email message.')
subject = sys.stdin.readline().strip()

print('Enter the content for the email message.')
content = sys.stdin.readline().strip()

# Login to email server
print('Enter your username')
senderEmail = sys.stdin.readline().strip()
mypassword = getpass.getpass('Password for ' + senderEmail + ': ')
emailLogin(senderEmail, mypassword)

sendEmail(senderEmail, recipientEmail, subject, content)
print('Sent email to ' + recipientEmail + ' email successfully.')

# logout
emailLogout()