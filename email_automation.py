import smtplib
import pandas as pd
from email.mime.text import MIMEText

# Gmail credentials (use App Password if 2FA enabled)
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"

# Load contacts
contacts = pd.read_csv("contacts.csv")  # columns: name,email

# Create SMTP session
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, PASSWORD)

for index, row in contacts.iterrows():
    name = row['name']
    to_email = row['email']
    
    subject = "Hello from Python Script!"
    body = f"Hi {name},\n\nThis is a test email sent using Python.\n\nBest regards"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to_email
    
    server.sendmail(EMAIL, to_email, msg.as_string())
    print(f"Email sent to {name} ({to_email})")

server.quit()
