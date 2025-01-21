import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from celery import Celery

from config import SMTP_USER, SMTP_PORT, SMTP_PASSWORD

celery = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@celery.task
def send_email(email: str, letter: str):
    msg = MIMEText(f'{letter}', 'plain', 'utf-8')
    msg['Subject'] = Header('Всероссийский патриотический проект «Карта памяти»', 'utf-8')
    msg['From'] = SMTP_USER
    msg['To'] = ', '.join(email)

    try:
        with smtplib.SMTP_SSL('smtp.yandex.ru', SMTP_PORT) as s:
            s.login(SMTP_USER, SMTP_PASSWORD)
            s.sendmail(msg['From'], email, msg.as_string())
    except Exception as ex:
        print(f'Failed to send email: {ex}')


@celery.task
def send_email_html(email: str, letter: str):
    try:
        # Формирование HTML письма
        msg = MIMEText(letter, 'html', 'utf-8')  # Используем 'html', а не 'plain'
        msg['Subject'] = Header('Всероссийский патриотический проект «Карта памяти»', 'utf-8')
        msg['From'] = formataddr((str(Header("Карта памяти", "utf-8")), SMTP_USER))
        msg['To'] = email  # Оставляем строку, так как email передается как строка

        # Отправка письма через SMTP с SSL
        with smtplib.SMTP_SSL('smtp.yandex.ru', SMTP_PORT) as s:
            s.login(SMTP_USER, SMTP_PASSWORD)
            s.sendmail(SMTP_USER, email, msg.as_string())
        print(f"Email sent successfully to {email}")
    except Exception as ex:
        print(f"Failed to send email to {email}: {ex}")