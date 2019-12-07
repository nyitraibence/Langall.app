from django import forms
from .models import TeacherProfile, Lesson
from django.utils.translation import gettext_lazy as _


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['introduction', 'base_price', 'teach_lang_1', 'teach_lang_2','teach_lang_3']


class PingTeacherForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['language', 'note']
        labels = {
            'language': _('Milyen nyelven?'),
            'note': _('Üzenet'),
        }