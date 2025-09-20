from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'subject', 'message', 'consent']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6}),
        }