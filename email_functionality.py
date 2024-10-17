import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_with_program(email, program):
    try:
        # Email configuration
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        smtp_server = "smtp.gmail.com"  
        smtp_port = 587  

        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = "Your Personalized Training Program"

        # Add body
        body = f"""
        Here is your personalized training program:

        {program}

        Thank you for using our service!
        """
        message.attach(MIMEText(body, "plain"))

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)

        return True
    except Exception as e:
        return False