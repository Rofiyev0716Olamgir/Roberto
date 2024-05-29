from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your Name',
            'name': 'message-name',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your Email',
            'name': 'message-email',
        })

        self.fields['message'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your Message',
            'name': 'message-message',
        })