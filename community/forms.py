from django import forms
from .models import newJogging, newCare

class newJogging(forms.ModelForm):
    class Meta:
        model = newJogging
        fields=['animal_kind', 'area', 'start_time', 'end_time', 'kind', 'caution', 'price', 'image', 'title', 'content']


class newCare(forms.ModelForm):
    class Meta:
        model = newCare
        fields=['animal_kind', 'area', 'start_time', 'end_time', 'kind', 'caution', 'price', 'image', 'title', 'content']