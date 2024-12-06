from fastapi import FastAPI, HTTPException, Form,BackgroundTasks
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.utlity.email_templates import subscription_confirmation,subscription_canceled,support_request_acknowledgment,reset_password_email,verify_otp,product_offer_email
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# SMTP configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL = os.getenv("EMAIL")

def send_email_support(from_email: str,to_email: str, subject: str, body: str):
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = from_email  # Match the sender email to the authenticated one
        message["To"] = EMAIL
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL, from_email, message.as_string())

    except smtplib.SMTPSenderRefused as e:
        raise HTTPException(
            status_code=400,
            detail=f"Sender email address not allowed: {e.smtp_error.decode()}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")


def get_email_template(template_name: str, *args):
    templates = {
        "subscription_confirmation": subscription_confirmation,
        "reset_password_email": reset_password_email,
        "subscription_canceled": subscription_canceled,
        "support_request_acknowledgment": support_request_acknowledgment,
        "verify_otp": verify_otp,
        "product_offer_email": product_offer_email,
    }

    if template_name not in templates:
        raise HTTPException(status_code=400, detail="Template not found")

    return templates[template_name](*args)


def send_email_dynamic(to_email: str, subject: str, body: str):
    try:
        sandbox_email = "kanuri.durgaprasad1997@gmail.com"
        # Create the email message
        message = MIMEMultipart()
        message["From"] = EMAIL  # Match the sender email to the authenticated one
        message["To"] = sandbox_email #replace to_email when production
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL, sandbox_email, message.as_string())

    except smtplib.SMTPSenderRefused as e:
        raise HTTPException(
            status_code=400,
            detail=f"Sender email address not allowed: {e.smtp_error.decode()}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

