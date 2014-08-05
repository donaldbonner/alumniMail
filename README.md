pyMail
------

This is a server wrote in python that will process a large amount of information to send out via email.

### Premise

My fraternity has a large alumni base.  A few (okay more than a few) members still have debt.  This script will process the alumni (and active) names, emails, and debt to tailor an email message to each to politely ask for them to update their debt.

### Functionality

This is a list of the metrics for the program.  An outline for how it will function

* Input the information from a spreadsheet(.crv) file.  Column information will go as ordered. Name, Email, Current Debt

* Create a generic text file to input as the email body.  There will be unique characters in each message that will be replaced on sending with first and last name, the email, and current debt owed.

* Add support for input variables.  This will allow to clear lines of alumni who have paid debt, update for partial payments, or add members to debt list.  All information will be updated in spreadsheet.

### Format

***The following format must be followed or the script will not work***

*	The input of money owed must be in the file called debt.csv.  The format must be in 3 columns.  The first is Name, the second is Email address, the third is amount owed.

*	The body of the email must be in an ascii file called moneyOwed.  The paramaters to be replaced must be in the ascii file as [[NAME]], and [[MONEY]].

Source code is of course there to modify to the specific application!
