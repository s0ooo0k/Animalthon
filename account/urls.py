from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateResponseMixin
from .views import *
import account.views
import community.views


app_name = "account"
urlpatterns = [
    path('', community.views.home, name="home"),
    path('signup/', account.views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
