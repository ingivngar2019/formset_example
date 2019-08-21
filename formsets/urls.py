"""formsets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from .books.views import create_book_normal, create_book_fixed

urlpatterns = [
    path('secrets/', admin.site.urls), # url change for security
    re_path(r'^formset/$', create_book_normal, name='example'),
    re_path(r'^formset2/$', create_book_fixed, name='example2'),


    re_path(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/formset/'}, name='logout'),
]
