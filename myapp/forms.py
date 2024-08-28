from django import forms
from .models import mytable

class myform(forms.ModelForm):
    class Meta:
        model = mytable
        fields = '__all__'