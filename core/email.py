import smtplib
from email.message import EmailMessage
from pathlib import Path
from fastapi import BackgroundTasks


def send_email(subject: str, body: str, to_email: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "noreply@example.com"
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP("smtp.example.com", 587) as smtp:
        smtp.starttls()
        smtp.login("username", "password")
        smtp.send_message(msg)


def send_email_background(background_tasks: BackgroundTasks, subject: str, body: str, to_email: str) -> None:
    background_tasks.add_task(send_email, subject, body, to_email)
