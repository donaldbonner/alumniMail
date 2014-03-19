#!/usr/bin/env python3
"""
DJ Bonner
Alumni Debt Mailing script
input: debt.csv - 3 column format of debt.  name, email, and amount owed.
input: moneyOwed - a ascii file for the message to send in the body
REPLACED STRINGS - [[NAME]] and [[MONEY]]

Requires working GMail account

Sampled code from Scott Kuhls github
https://github.com/skuhl/autograder/blob/master/ag-email.py
"""

import sys, os, csv
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

if os.path.isfile('debt.csv'):
    print('Member spreadsheet present')
else:
    print('Member spreadsheet not in directory')
    sys.exit(1)

if os.path.isfile('moneyOwed'):
    print('Email message present')
else:
    print('Email message not in directory')
    sys.exit(1)

# read the body message
emailMessage = open('moneyOwed', 'r+')
message = emailMessage.read()
print('Message before replacement')
print(message)

# format the mailing list for usage
fileReader = csv.reader(open('debt.csv', 'r'), delimiter=',')
print('This is the mailing list.')
memberInfo = [row for row in fileReader]
for row in memberInfo:
    print(row)

# Login to email server
print('Enter your gmail account')
senderEmail = sys.stdin.readline().strip()
mypassword = getpass.getpass('Password for ' + senderEmail + ': ')
emailLogin(senderEmail, mypassword)

# Subject line of email
print('Enter the subject line for the email message.')
subject = sys.stdin.readline().strip()

# parse the input spreadsheet.  Check for illegal characters.
# Any non ascii characters will make mail server throw an error.
# Updates as email sends.
for name, recipEmail, amount in [row for row in memberInfo]:
    print(', '.join([name, recipEmail, amount]))
    personal = message.replace('[[NAME]]', name)
    personal = personal.replace('[[MONEY]]', amount)

    for letter in personal:
        if ord(letter) > 128:
            print('Illegal character:' + letter)
            sys.exit(1)

    sendEmail(senderEmail, recipEmail, subject, personal.strip())    
    print('email to ' + recipEmail + ' sent successfully.')   
    print('')

# logout
emailLogout()