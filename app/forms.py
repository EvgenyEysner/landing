from django.forms import ModelForm, EmailField
from .models import Contact


class FormContact(ModelForm):
    email = EmailField(max_length=255, help_text='Bitte eine email eingeben...')

    class Meta:
        model = Contact
        fields = '__all__'

