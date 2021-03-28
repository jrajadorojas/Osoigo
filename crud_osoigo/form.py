# Django
from django import forms

# Models
from crud_osoigo.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"