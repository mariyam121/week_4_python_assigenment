import smtplib
from email.message import EmailMessage
s`
sender_email = "sanobarmariyamtth@gmail.com"
receiver_email = "rizwanrizzu521@gmail.com"

# Use an app password, NOT your normal email password
app_password = "mariyam12345678"

message = EmailMessage()
message["Subject"] = "Internship Python Project"
message["From"] = sender_email
message["To"] = receiver_email

message.set_content(
    "Hello,\n\n"
    "This is an automated email sent using Python smtplib.\n\n"
    "Thank you."
)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(message)

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)