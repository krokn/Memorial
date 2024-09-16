import smtplib
from email.header import Header
from email.mime.text import MIMEText

from celery import Celery

from config import SMTP_USER, SMTP_PORT, SMTP_PASSWORD

celery = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@celery.task
def send_email(email: str, letter: str):
    msg = MIMEText(f'{letter}', 'plain', 'utf-8')
    msg['Subject'] = Header('Мобильная игра Шифр', 'utf-8')
    msg['From'] = SMTP_USER
    msg['To'] = ', '.join(email)

    try:
        with smtplib.SMTP_SSL('smtp.yandex.ru', SMTP_PORT) as s:
            s.login(SMTP_USER, SMTP_PASSWORD)
            s.sendmail(msg['From'], email, msg.as_string())
    except Exception as ex:
        print(f'Failed to send email: {ex}')