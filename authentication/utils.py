import threading

from django.core.mail import EmailMessage


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        super().__init__()

    def run(self) -> None:
        self.email.send()


class EmailUtil:

    @staticmethod
    def send_email(subject, body, to):
        email = EmailMessage(subject, body, to=(to, ))
        EmailThread(email).start()
