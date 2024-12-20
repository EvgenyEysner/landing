from django.core import validators
from django.forms import ModelForm, EmailField, Form, CharField, Textarea

from .models import Rating


class FormContact(Form):
    name = CharField(
        max_length=128,
        required=True,
        error_messages={"required": "Bitte geben Sie Ihren Namen ein."},
    )
    phone = CharField(
        max_length=128,
        required=True,
        error_messages={"required": "Bitte geben Sie Ihre Telefonnummer ein."},
    )
    email = EmailField(
        required=True,
        validators=[
            validators.EmailValidator(
                message="Bitte geben Sie eine valide Email Adresse ein"
            )
        ],
        error_messages={"required": "Bitte geben Sie Ihre E-Mail-Adresse ein."},
    )
    message = CharField(
        required=True,
        widget=Textarea,
        error_messages={"required": "Bitte geben Sie Ihre Nachricht ein."},
    )


class FormPrice(Form):
    lastname = CharField(
        max_length=128,
        required=True,
        error_messages={"required": "Bitte geben Sie Ihren Nachnamen ein."},
    )
    userphone = CharField(
        max_length=64,
        required=True,
        error_messages={"required": "Bitte geben Sie Ihre Telefonnummer ein."},
    )
    useremail = EmailField(
        required=True,
        validators=[
            validators.EmailValidator(
                message="Bitte geben Sie eine valide Email Adresse ein"
            )
        ],
        error_messages={"required": "Bitte geben Sie Ihre E-Mail-Adresse ein."},
    )


class FormReview(ModelForm):

    class Meta:
        model = Rating
        fields = ["star", "address", "team", "review"]
