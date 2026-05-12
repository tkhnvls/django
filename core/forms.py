from django import forms
from .models import Otziv
class OtzivForm(forms.ModelForm):
    class Meta:
        model = Otziv
        fields = ['nik', 'tekst', 'ocenks']
