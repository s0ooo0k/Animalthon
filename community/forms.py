from django import forms
from .models import newJogging, newCare, commentJogging

class newJoggingform(forms.ModelForm):
    class Meta:
        model = newJogging
        fields=['animal_kind', 'area', 'start_time', 'end_time', 'kind', 'caution', 'price', 'image', 'title', 'content']


class newCareform(forms.ModelForm):
    class Meta:
        model = newCare
        fields=['animal_kind', 'area', 'start_time', 'end_time', 'kind', 'caution', 'price', 'image', 'title', 'content']

class commentJoggingform(forms.ModelForm):
    class Meta:
        model = commentJogging
        fields = ['comment']