from django import forms
from .models import Work

class BookForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('title','rar_file')