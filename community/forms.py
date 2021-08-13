from django import forms
from .models import newJogging, newCare, commentJogging, commentCare

class newJoggingform(forms.ModelForm):
    class Meta:
        model = newJogging
        fields=['animal_kind', 'area', 'start_time', 'end_time', 'kind', 'caution', 'price', 'image', 'title', 'content']
        labels={
            'animal_kind': '동물',
            'area': '지역',
            'start_time':'의뢰 시작 시간',
            'end_time': '끝나는 시간',
            'kind' : '품종',
            'caution' : '주의사항',
            'price' : '의뢰비',
            'image' :'동물 사진',
            'title' : '의뢰 제목',
            'content' : '의뢰 내용',
        }
        widgets={
            'caution':forms.Textarea(attrs={'rows':4}),
            'content':forms.Textarea(attrs={'rows':4}),
        }


class newCareform(forms.ModelForm):
    class Meta:
        model = newCare
        fields=['animal_kind', 'area', 'start_time', 'end_time', 'kind', 'caution', 'price', 'image', 'title', 'content']
        labels={
            'animal_kind': '동물',
            'area': '지역',
            'start_time':'의뢰 시작 시간',
            'end_time': '끝나는 시간',
            'kind' : '품종',
            'caution' : '주의사항',
            'price' : '의뢰비',
            'image' :'동물 사진',
            'title' : '의뢰 제목',
            'content' : '의뢰 내용',
        }
        widgets={
            'caution':forms.Textarea(attrs={'rows':4}),
            'content':forms.Textarea(attrs={'rows':4}),
        }

class commentJoggingform(forms.ModelForm):
    class Meta:
        model = commentJogging
        fields = ['comment']


class commentCareform(forms.ModelForm):
    class Meta:
        model = commentCare
        fields = ['comment']