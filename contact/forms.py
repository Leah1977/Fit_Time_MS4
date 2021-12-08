from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Create a form to contact us
    """
    class Meta:
        model = Contact
        fields = ['name', 'title', 'message', 'email' ]

    def __init__(self, *args, **kwargs):
        """ Insert placeholders for form """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'title': 'Title',
            'message': 'Message',
            'email': 'Email',
        }
