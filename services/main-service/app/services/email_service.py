from fastapi import APIRouter
import smtplib
from email.message import EmailMessage
import os
from config.logging import setup_logging

from database.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])
db = get_db()
logger = setup_logging()

async def send_email(email: str, subject: str, content: str) -> bool:
    sender_email = os.getenv("MAIL_SENDER")
    sender_password = os.getenv("MAIL_PASSWORD")
    mail_server = os.getenv("MAIL_SERVER")
    mail_port = int(os.getenv("MAIL_PORT")) or None
    receiver_email = email

    if (not sender_email or not sender_password or not receiver_email or not mail_port or not mail_server):
        print("❌Missing credentials")
        return False

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(content)

    try:
        with smtplib.SMTP(mail_server, mail_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            return True
    except Exception as e:
        print(f"❌ Email error: {e}")
        logger.info(e)
        return False