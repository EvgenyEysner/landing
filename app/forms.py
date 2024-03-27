from django.forms import ModelForm, EmailField
from .models import Contact, Rating


class FormContact(ModelForm):
    email = EmailField(max_length=255, help_text='Bitte eine email eingeben...')

    class Meta:
        model = Contact
        fields = '__all__'


class FormReview(ModelForm):

    class Meta:
        model = Rating
        fields = ["star", "address", "team", "review"]


