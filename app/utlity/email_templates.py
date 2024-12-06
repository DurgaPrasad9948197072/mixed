# email_templates.py
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
COMPANY_NAME = os.getenv("COMPANY_NAME")
COMPANY_ADDRESS = os.getenv("COMPANY_ADDRESS")
CONTACT_EMAIL = os.getenv("CONTACT_EMAIL")
WEBSITE_LINK = os.getenv("WEBSITE_LINK")
DOCUMENTS_LINKS = os.getenv("DOCUMENTS_LINKS")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")
HELP = os.getenv("HELP")

def subscription_confirmation(product: str, username: str, plan: str, price: float, password: str):
    subject = f"Your Subscription to {product} is Confirmed!"
    body = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333;
                    line-height: 1.6;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 20px auto;
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
                .header {{
                    text-align: center;
                    font-size: 24px;
                    color: #0073e6;
                    margin-bottom: 20px;
                }}
                .section {{
                    margin-bottom: 20px;
                }}
                .section h3 {{
                    color: #333;
                    font-size: 18px;
                    margin-bottom: 8px;
                }}
                .content {{
                    font-size: 16px;
                    color: #555;
                }}
                .footer {{
                    text-align: center;
                    font-size: 14px;
                    color: #888;
                    margin-top: 40px;
                    border-top: 1px solid #eee;
                    padding-top: 20px;
                }}
                .button {{
                    background-color: #0073e6;
                    color: white;
                    text-align: center;
                    padding: 10px 20px;
                    border-radius: 5px;
                    text-decoration: none;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h2>Your Subscription to {product} is Confirmed!</h2>
                </div>

                <div class="section">
                    <h3>Dear {username},</h3>
                    <p class="content">
                        Thank you for subscribing to the <strong>{plan}</strong> plan on <strong>{product}</strong>! We're excited to have you onboard and provide you with the tools and services to help you achieve your goals.
                    </p>
                </div>

                <div class="section">
                    <h3>Subscription Summary:</h3>
                    <ul class="content">
                        <li><strong>Plan:</strong> {plan}</li>
                        <li><strong>Billing:</strong> ${price} per month</li>
                        <li><strong>Next Billing Date:</strong> 2025-01-01</li>
                        <li><strong>Renewal:</strong> Your subscription will automatically renew on this date.</li>
                        <li><strong>Payment Method:</strong> Credit Card</li>
                    </ul>
                </div>

                <div class="section">
                    <h3>Your Account Details:</h3>
                    <ul class="content">
                        <li><strong>Username:</strong> {username}</li>
                        <li><strong>Password:</strong> {password}</li>
                    </ul>
                    <p class="content">
                        *If you wish to reset your password, please visit your account settings.*
                    </p>
                </div>

                <div class="section">
                    <h3>Website Production Links:</h3>
                    <ul class="content">
                        <li><strong>Website URL:</strong> <a href="https://www.yoursite.com">www.yoursite.com</a></li>
                        <li><strong>Admin Dashboard URL:</strong> <a href="https://www.yoursite.com/admin">Admin Dashboard</a></li>
                        <li><strong>Preview Links:</strong></li>
                        <ul>
                            <li><a href="#">Link 1</a></li>
                            <li><a href="#">Link 2</a></li>
                        </ul>
                    </ul>
                </div>

                <div class="section">
                    <h3>Admin Credentials:</h3>
                    <ul class="content">
                        <li><strong>Admin Username:</strong> {username}</li>
                        <li><strong>Admin Password:</strong> {password}</li>
                    </ul>
                    <p class="content">
                        *Make sure to change this password after logging in for the first time to ensure account security.*
                    </p>
                </div>

                <div class="section">
                    <h3>Additional Links and Information:</h3>
                    <ul class="content">
                        <li><strong>Support:</strong> If you need any assistance, please contact our support team at <a href="mailto:support@example.com">support@example.com</a>.</li>
                        <li><strong>Documentation:</strong> Access our detailed guides and resources at <a href="https://www.yoursite.com/docs">Documentation</a>.</li>
                    </ul>
                </div>

                <div class="section">
                    <h3>What’s Next:</h3>
                    <p class="content">
                        After logging into the admin dashboard, you will be able to manage your website, track user activity, modify content, and more.
                    </p>
                </div>

                <div class="footer">
                    <p>Thank you for choosing {product}! We're here to support you every step of the way.</p>
                    <p>{COMPANY_NAME} | {COMPANY_ADDRESS} | <a href="mailto:{CONTACT_EMAIL}">Contact Email</a> | <a href="mailto:{SUPPORT_EMAIL}">Support Email</a></p>
                    <p><a href="{WEBSITE_LINK}">Website</a></p>
                </div>
            </div>
        </body>
    </html>
    """
    return subject, body

def reset_password_email(reset_link: str, username: str):
    subject = "Reset Your Password"
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333333;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                padding: 20px;
                border: 1px solid #dddddd;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                background-color: #007bff;
                color: #ffffff;
                padding: 20px;
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                border-radius: 8px 8px 0 0;
            }}
            .content {{
                padding: 20px;
                font-size: 16px;
                line-height: 1.6;
                text-align: center;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                font-size: 14px;
                color: #777777;
            }}
            .button {{
                display: inline-block;
                background-color: #007bff;
                color: #ffffff;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 4px;
                font-size: 16px;
                margin-top: 20px;
            }}
            .button:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                Reset Your Password
            </div>
            <div class="content">
                <p>Hi {username},</p>
                <p>We received a request to reset the password for your account. You can reset your password by clicking the button below:</p>
                <a href="{reset_link}" class="button">Reset Password</a>
                <p>If you did not request this change, you can safely ignore this email. Your password will not be changed unless you take action by clicking the link above.</p>
                <p style="margin-top: 10px; font-size: 14px; color: #555;">This link will expire in 24 hours.</p>
            </div>
            <div class="footer">
                &copy; {datetime.now().year} Your Company. All rights reserved.
                <br>
                <a href="https://www.yourcompany.com" style="color: #007bff; text-decoration: none;">Visit our website</a>
            </div>
        </div>
    </body>
    </html>
    """
    return subject, body
    
def subscription_canceled(product: str, username: str, plan: str, cancellation_date: str):
    subject = f"Your Subscription to {product} Has Been Canceled"
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f9f9f9;
                color: #333;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                padding: 20px;
                border: 1px solid #dddddd;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                background-color: #ff6b6b;
                color: #ffffff;
                padding: 10px 0;
                font-size: 24px;
                border-radius: 8px 8px 0 0;
            }}
            .content {{
                padding: 20px;
                font-size: 16px;
                line-height: 1.6;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                font-size: 14px;
                color: #777777;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                Subscription Cancellation Notice
            </div>
            <div class="content">
                <p>Dear {username},</p>
                <p>We regret to inform you that your subscription to the <strong>{plan}</strong> plan for <strong>{product}</strong> has been canceled, effective <strong>{cancellation_date}</strong>.</p>
                <p>If this cancellation was made in error or you’d like to renew your subscription, please contact our support team or visit your account dashboard to re-subscribe.</p>
                <p>Thank you for being a valued customer. We hope to have the opportunity to serve you again in the future.</p>
                <p>Best regards,</p>
                <p><strong>{COMPANY_NAME}</strong></p>
            </div>
            <div class="footer">
               &copy; {datetime.now().year}  {COMPANY_NAME}. All rights reserved.
            </div>
        </div>
    </body>
    </html>
    """
    return subject, body

def support_request_acknowledgment(username: str):
    subject = "Customize Request Acknowledgment"
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f9f9f9;
                color: #333;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                padding: 20px;
                border: 1px solid #dddddd;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                background-color: #0078D7;
                color: #ffffff;
                padding: 10px 0;
                font-size: 24px;
                border-radius: 8px 8px 0 0;
            }}
            .content {{
                padding: 20px;
                font-size: 16px;
                line-height: 1.6;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                font-size: 14px;
                color: #777777;
            }}
            .button {{
                display: inline-block;
                background-color: #0078D7;
                color: #ffffff;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 4px;
                font-size: 16px;
                margin-top: 20px;
            }}
            .button:hover {{
                background-color: #005BB5;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                Customize Request Received
            </div>
            <div class="content">
                <p>Dear {username},</p>
                <p>Thank you for reaching out to our support team. We have received your request and our team is already working to address your concerns.</p>
                <p>As part of the resolution process, we will provide you with:</p>
                <ul>
                    <li>Previews for all relevant devices (Desktop, Tablet, Mobile).</li>
                    <li>Comprehensive professional data and recommendations.</li>
                </ul>
                <p>Our team will contact you at the earliest with updates and a resolution. If you need to provide additional details, feel free to reply to this email or contact us at <a href="mailto:{SUPPORT_EMAIL}" style="color: #0078D7;">{SUPPORT_EMAIL}</a>.</p>
                <p>We appreciate your patience and are committed to providing you with the best possible support experience.</p>
                <a href="https://www.yourcompany.com/support" class="button">View Support Dashboard</a>
                <p>Thank you for choosing our services.</p>
                <p>Best regards,</p>
                <p><strong>Your Company Support Team</strong></p>
            </div>
            <div class="footer">
                &copy; {datetime.now().year} {COMPANY_NAME}. All rights reserved.
                <br>
                Need further assistance? Visit our <a href="{HELP}" style="color: #0078D7;">Help Center</a>.
            </div>
        </div>
    </body>
    </html>
    """
    return subject, body



def product_offer_email(product_name: str, offer_percentage: int, original_price: float, offer_price: float, offer_expiry: str, shop_now_link: str):
    subject = f"Exclusive {offer_percentage}% Off on {product_name} – Limited Time Offer!"
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                color: #333333;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                padding: 20px;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                background-color: #28a745;
                color: #ffffff;
                padding: 20px;
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                border-radius: 8px 8px 0 0;
            }}
            .content {{
                padding: 20px;
                font-size: 16px;
                line-height: 1.6;
                text-align: center;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                font-size: 14px;
                color: #777777;
            }}
            .button {{
                display: inline-block;
                background-color: #28a745;
                color: #ffffff;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 4px;
                font-size: 16px;
                margin-top: 20px;
            }}
            .button:hover {{
                background-color: #218838;
            }}
            .offer-details {{
                background-color: #f8f9fa;
                padding: 15px;
                border: 1px dashed #28a745;
                margin: 20px 0;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                Hurry! Get {offer_percentage}% Off on {product_name} 🎉
            </div>
            <div class="content">
                <p>Don't miss out on this exclusive offer! For a limited time only, enjoy a massive <strong>{offer_percentage}% discount</strong> on our top-selling product, <strong>{product_name}</strong>.</p>
                <div class="offer-details">
                    <p><strong>Original Price:</strong> ${original_price:.2f}</p>
                    <p><strong>Offer Price:</strong> <span style="color: #28a745;">${offer_price:.2f}</span></p>
                    <p><strong>Offer Ends:</strong> {offer_expiry}</p>
                </div>
                <p>Take advantage of this deal now and elevate your experience with {product_name}.</p>
                <a href="{shop_now_link}" class="button">Shop Now</a>
                <p style="margin-top: 10px; font-size: 14px; color: #555;">*Terms and conditions apply. Offer valid until {offer_expiry}.</p>
            </div>
            <div class="footer">
                &copy; {datetime.now().year} {COMPANY_NAME}. All rights reserved.
                <br>
                <a href="{WEBSITE_LINK}" style="color: #28a745; text-decoration: none;">Visit our website</a>
            </div>
        </div>
    </body>
    </html>
    """
    return subject, body


def verify_otp(user_name: str, otp: str, expiration_time: str):
    subject = "Your OTP Code for Verification"
    body = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #333;
                font-size: 24px;
                text-align: center;
            }}
            p {{
                color: #555;
                font-size: 16px;
                line-height: 1.5;
            }}
            .otp {{
                font-size: 24px;
                font-weight: bold;
                color: #4CAF50;
                display: block;
                margin: 20px 0;
                text-align: center;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #888;
                margin-top: 40px;
            }}
            .footer a {{
                color: #4CAF50;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <h1>Hello {user_name},</h1>
            <p>Thank you for requesting an OTP for verification. Below is your One-Time Password (OTP) to complete your request:</p>
            <div class="otp">{otp}</div>
            <p>This OTP will expire in <strong>{expiration_time}</strong>, so please use it before then.</p>
            <p>If you did not request this, please ignore this email or contact our support team for further assistance.</p>
            <p>Thank you for being with us!</p>
            <div class="footer">
                <p>If you have any questions, feel free to <a href="{SUPPORT_EMAIL}">contact us</a>.</p>
                <p>&copy; {datetime.now().year} {COMPANY_NAME}. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return subject, body
