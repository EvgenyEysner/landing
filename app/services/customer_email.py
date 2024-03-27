from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(name, phone, email, text):
    admin_msg = EmailMultiAlternatives(
        subject="Eine neue Anfrage über Homepage",
        from_email=settings.SERVER_EMAIL,
        to=[settings.ADMINS[0]],
    )
    body = render_to_string(
        "app/admin_mail.html",
        {
            "name": name,
            "telefon": phone,
            "email": email,
            "text": text,
        },
    )

    admin_msg.attach_alternative(body, "text/html")
    admin_msg.send()

    client_msg = EmailMultiAlternatives(
        subject=f"Hallo {name}!",
        from_email=settings.SERVER_EMAIL,
        to=[email],
    )
    body = render_to_string(
        "app/client_mail.html",
        {
            "msg": "Vielen Dank für Ihre Anfrage. Wir werden uns schnellstmöglich darum kümmern."
        },
    )

    client_msg.attach_alternative(body, "text/html")
    client_msg.send()
