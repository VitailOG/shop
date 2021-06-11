from django.core.mail import send_mail

from shop.celery import app
from .service import sending_welcome_message_on_email_user


@app.task
def send_message_on_email(email_user):
    sending_welcome_message_on_email_user(email_user)


@app.task
def sending_report_of_month():
    send_mail(
        'static',
        'Ми будемо регулярно вас повідомляти про новинки в нашому інтернет-магазині',
        'vzaharkiv28@gmail.com',
        ['vzaharkiv28@gmail.com'],
        fail_silently=False
    )
