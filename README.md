pyMail
------

This is a server wrote in python that will process a large amount of information to send out via email.

***premise

My fraternity has a large alumni base.  A few (okay more than a few) members still have debt.  This script will process the alumni names, emails, and debt to tailor an email message to each to politely ask for them to update their debt.

***Functionality

This is a list of the metrics for the program.  An outline for how it will function

*	Input the information from a spreadsheet(.crv) file.  Column information will go as ordered. First Name, Last Name, Email, Current Debt

*	Create a generic text file to input as the email body.  There will be unique characters in each message that will be replaced on sending with first and last name, the email, and current debt owed.

*	Add support for input variables.  This will allow to clear lines of alumni who have paid debt, update for partial payments, or add members to debt list.  All information will be updated in spreadsheet.