import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, to_emails):
    smtp_server = 'smtp.gmail.com'  # or any SMTP site
    smtp_port = 587  
    smtp_username = 'yourname@gmail.com'  # replace with you own email
    smtp_password = 'abcd1234efgh5678'  # you may need to create an app password. for more see README.md file

    # Create message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    # Attach body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send email
    server.send_message(msg)
    server.quit()


# run app
if __name__ == "__main__":
    subject = ""  # put in your subject here
    body = ""
    to_email = ["john@example.com",
                "julie@example.com"]  # Replace with recipient's email address. for more than one, add comma then a new string to the list
    send_email(subject, body, to_email)

# By Luke.n.Programming
