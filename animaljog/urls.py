"""animaljog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
import community.views
import community.forms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', community.views.home, name="home"),
    path('new', community.views.new, name="new"),
    path('new/jogging/', community.views.createJogging, name="createJogging"),
    path('new/care/', community.views.createCare, name="createCare"),
    path('community/jogging', community.views.readJogging, name="readJogging"),
    path('community/care', community.views.readCare, name="readCare"),
    path('community/jogging/<int:jog_id>', community.views.detailJogging, name="detailJogging"),
    path('account/', include('account.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
