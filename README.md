# Email Automation

## What it does
This Python script automatically sends personalized emails to a list of contacts from a CSV file.  
It reads each contact's name and email, creates a custom message, and sends it via Gmail.

## How to use

1. Install required libraries if you don’t have them:
```bash
pip install pandas


2. Prepare your contacts.csv file

3. In email_automation.py, replace the placeholders with your Gmail and App Password

4.Run the script:
python email_automation.py

Emails will be sent automatically to each contact, and the terminal will print a confirmation message for each email.
Tools Used
Python
Pandas
smtplib
email.mime
