from django import forms
from .models import ContactForm

class ContactForms(forms.ModelForm):
    class Meta:
        model = ContactForm  

        fields = ['name', 'subject', 'phone', 'email', 'message']
        labels = {
            'name': 'Ad',
            'subject': 'Konu',
            'phone': 'Telefon',
            'email': 'Email',
            'message': 'Mesaj'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        error_messages = {
            'name': {'required': 'Ad boş bırakılamaz.'},
            'subject': {'required': 'Konu boş bırakılamaz.'},
            'phone': {'required': 'Telefon boş bırakılamaz.'},
            'email': {'required': 'Email boş bırakılamaz.'},
            'message': {'required': 'Mesaj boş bırakılamaz.'},
        }