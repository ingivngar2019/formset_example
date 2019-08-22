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
from django.views.generic import TemplateView

from .books.views import create_book_normal, create_book_fixed, create_book_related

from .restaurant import  views as rest_views

urlpatterns = [
    path('secrets/', admin.site.urls), # url change for security
    re_path(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),
    re_path(r'^formset/$', create_book_normal, name='example'),
    re_path(r'^formset2/$', create_book_fixed, name='example2'),
    re_path(r'^formset3/$', create_book_related, name='example3'),

    # Restaurant related URls
    re_path(r'^recetas/$', rest_views.recetas, name='lista'),
    re_path(r'^recetas/registrar/$', rest_views.registro_edicion, name='registrar'),
    re_path(r'^recetas/(?P<receta_id>\d+)/$', rest_views.registro_edicion, name='editar'),


    re_path(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
]
