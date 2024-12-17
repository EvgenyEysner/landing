from django.core import validators
from django.forms import ModelForm, EmailField, Form, CharField, Textarea

from .models import Rating


class FormContact(Form):
    name = CharField(max_length=128, required=True)
    phone = CharField(max_length=128, required=True)
    email = EmailField(
        required=True,
        validators=[
            validators.EmailValidator(
                message="Bitte geben Sie eine valide Email Adresse ein"
            )
        ],
    )
    message = CharField(required=True, widget=Textarea)


class FormPrice(Form):
    lastname = CharField(max_length=128, required=True)
    userphone = CharField(max_length=64, required=True)
    useremail = EmailField(
        required=True,
        validators=[
            validators.EmailValidator(
                message="Bitte geben Sie eine valide Email Adresse ein"
            )
        ],
    )


class FormReview(ModelForm):

    class Meta:
        model = Rating
        fields = ["star", "address", "team", "review"]
