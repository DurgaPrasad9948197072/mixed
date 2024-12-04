from fastapi import FastAPI, HTTPException, Form
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()

# SMTP configuration
SMTP_SERVER = "smtp.elasticemail.com"
SMTP_PORT = 587
SMTP_USERNAME = "kanuri.durgaprasad1997@gmail.com" 
SMTP_PASSWORD = "4C97F63469D8BE4F15252AF03E605DB43856"


def send_email_support(to_email: str, subject: str, body: str):
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = SMTP_USERNAME  # Match the sender email to the authenticated one
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, to_email, message.as_string())

        print("Email sent successfully.")

    except smtplib.SMTPSenderRefused as e:
        raise HTTPException(
            status_code=400,
            detail=f"Sender email address not allowed: {e.smtp_error.decode()}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")




