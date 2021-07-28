from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException


class MailSender:
    @staticmethod
    def send_basic_email(data):
        message = Mail(from_email=From(settings.FROM_EMAIL),
                       to_emails=To(data['to_email']),
                       subject=Subject(data['email_subject']),
                       plain_text_content=PlainTextContent(data['email_body']))
        message = message.get()
        sendgrid_client = SendGridAPIClient(settings.EMAIL_HOST_PASSWORD)
        sendgrid_client.send(message=message)
