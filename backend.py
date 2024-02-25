import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "xyhupsvnecwvwnxd"
SENDER = "muralimano86@gmail.com"
RECEIVER = "muralimano86@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer Showed Up!"
    email_message.set_content("Look who showed up today")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    gmail_smtp.ehlo()
    gmail_smtp.starttls()
    gmail_smtp.login(SENDER, PASSWORD)
    gmail_smtp.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail_smtp.quit()

if __name__ == "__main__":
    send_email("images/10.png")