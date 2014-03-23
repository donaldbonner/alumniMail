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

# format the mailing list for usage
def processCsv(name):
    fileReader = csv.reader(open(name, 'r'), delimiter=',')
    print('This is the mailing list.')
    memberInfo = [row for row in fileReader]
    for row in memberInfo:
        print(row)
    return memberInfo

# Tell the person how much they suck
# 1 suck = 1 dollar owed to house
def insertSuckage(sucks, personal):
    suckage = round(float(amount))
    personal += 'The TKE Robot will now tell you how it feels about you.\n\n'
    if suckage > 0:
        personal += '1 suck = 1 dollar owed to house\n\n'
        for num in range(suckage):
            personal += 'You Suck! '
    else:
        personal += '1 congrats = 1 pat on the back\n\n'
        for num in range(suckage * -1):
            personal += 'You Rock! '
    return personal    

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

memberInfo = processCsv('debt.csv')

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

    # insert suckage if desired
    #personal = insertSuckage(amount, personal)

    print(personal)
    for letter in personal:
        if ord(letter) > 128:
            print('Illegal character:' + letter)
            sys.exit(1)

    sendEmail(senderEmail, recipEmail, subject, personal.strip())    
    print('email to ' + recipEmail + ' sent successfully.')   
    print('')

# logout
emailLogout()