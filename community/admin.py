from django.contrib import admin
from .models import newJogging, newCare, commentJogging

# Register your models here.
admin.site.register(newJogging)
admin.site.register(newCare)
admin.site.register(commentJogging)