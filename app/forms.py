from django import forms
from app.models import *

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()

class SuryaGFListForm(forms.ModelForm):
    class Meta:
        model=SuryaGFList
        fields='__all__'


