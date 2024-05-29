# Python Automation Mail App
## Prerequistits
1. intallation of 2 libraries : smtplib, email.mime; these should be automaticlly installed, if not:
   - `pip install smtplib`
   - `pip install email`
2.  An email account that can use smtp
3.  Installation of Python 3 
4.  An app password if you are using a host such as gmail
5.  Depending on your OS, a task schedular of sorts
6.  - For Windows 10/11 - Task Schedular is built-in to Windows
    - For Mac OSX - Automator is another built-in app for Mac users
    - For Linux Systems - Cron

## Configuration
### SMTP Server Configuration:

smtp_server: The address of your SMTP server. For example, Gmail's SMTP server is smtp.gmail.com.

smtp_port: The port number for the SMTP server. Typically, this is 587 for TLS connections.

smtp_username: Your email address.

smtp_password: Your email account's password. Note: For Gmail, you might need to create an app-specific password if you have two-factor authentication enabled. Refer to the [Gmail documentation](https://support.google.com/mail/answer/185833?hl=en-GB) for more information.

### Note for anyone considering sending bulk emails ⚠️:
---

⚠️You should note that a commercial domain like gmail,yahoo,outlook etc. will most likely not support LARGE numbers of emails sent at once. I would encourage anyone with large-scale email needs to invest into a SMTP server, many can be found online at various pricings.⚠️

---
### Email Content:

subject: The subject of your email.
body: The body text of your email.
to_emails: A list of recipient email addresses. Store as strings seperated by commas.

Run the Script:

Execute the script using Python:

`shell : 
python send_email.py`

or run it in an IDE like PyCharm


## Security
Storing email credentials in plain text within your scripts is not recommended for production use. Consider using environment variables or a configuration file with restricted access to store sensitive information.

## Author
Created by Luke.n.Programming
--- 
Feel free to contribute to this project or report any issues.
