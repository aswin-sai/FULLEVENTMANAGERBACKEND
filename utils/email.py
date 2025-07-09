from flask_mail import Message
from extensions import mail
from flask import current_app

def send_inquiry_email(inquiry):
    msg = Message(
        subject="New Event Inquiry",
        sender=current_app.config.get('MAIL_DEFAULT_SENDER'),
        recipients=[current_app.config.get('MAIL_DEFAULT_SENDER')],  # Send to admin
        reply_to=inquiry.email,  # Set reply-to as the user's email
        body=f"New inquiry from {inquiry.name} ({inquiry.email}):\n\n{inquiry.message}"
    )
    mail.send(msg)
