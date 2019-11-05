from django import forms
from .models import TeacherProfile

class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['introduction', 'base_price', 'teach_lang_1', 'teach_lang_2','teach_lang_3']