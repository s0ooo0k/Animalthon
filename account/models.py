from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     have_choice= [
#         ('Y', '네'),
#         ('N', '아니오'),
#     ]
#     gender_choice = [
#         ('L', '여성'),
#         ('M', '남성'),
#         ('N', '비공개')
#     ]
#     animal_have = models.CharField(max_length=2, choices=have_choice)
#     nickname = models.CharField(max_length=10)
#     gender = models.CharField(max_length=2, choices=gender_choice)
    
#     def __str__(self):
#         return self.nickname
