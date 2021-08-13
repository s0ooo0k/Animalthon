from django.db import models
from django.db.models.fields import related
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class newJogging(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_choices = [
        ('DOG', 'dog'),
        ('CAT', 'cat'),
        ('ETC', 'other')
    ]
    area_choices = [
        ('SE', '서울특별시'),
        ('GG', '경기도'),
        ('CH', '충청도'),
        ('GS', '경상도'),
        ('JL', '전라도'),
        ('GW', '강원도'),
        ('JJ', '제주도')
    ]
    animal_kind=models.CharField(max_length=3, choices=animal_choices)
    area=models.CharField(max_length=2, choices=area_choices)
    start_time=models.DateTimeField(default=now)
    end_time=models.DateTimeField(default=now)
    kind=models.CharField(max_length=50)
    caution=models.TextField(blank=True)
    price=models.IntegerField(blank=True)
    image=models.ImageField(upload_to="jogimages/", blank=True, null=True)
    title=models.CharField(max_length=100)
    content=models.TextField(blank=True)

    def __str__(self):
        return self.title



class newCare(models.Model):
    animal_choices = [
        ('DOG', 'dog'),
        ('CAT', 'cat'),
        ('ETC', 'other')
    ]
    area_choices = [
        ('SE', '서울특별시'),
        ('GG', '경기도'),
        ('CH', '충청도'),
        ('GS', '경상도'),
        ('JL', '전라도'),
        ('GW', '강원도'),
        ('JJ', '제주도')
    ]
    animal_kind=models.CharField(max_length=3, choices=animal_choices)
    area=models.CharField(max_length=2, choices=area_choices)
    start_time=models.DateTimeField(default=now)
    end_time=models.DateTimeField(default=now)
    kind=models.CharField(max_length=50)
    caution=models.TextField(blank=True)
    price=models.IntegerField(blank=True)
    image=models.ImageField(upload_to="careimages/", blank=True, null=True)
    title=models.CharField(max_length=100)
    content=models.TextField(blank=True)

    def __str__(self):
        return self.title



class commentJogging(models.Model):
    post = models.ForeignKey(newJogging, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)

    def __str__(self):
        return self.comment


class commentCare(models.Model):
    post = models.ForeignKey(newCare, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)

    def __str__(self):
        return self.comment