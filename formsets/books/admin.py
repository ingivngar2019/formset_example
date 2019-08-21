from django.contrib import admin
from .models import *
# Register your models here.



class Genredmin(admin.ModelAdmin):
    list_display = ('desc', 'id')

admin.site.register(Genre, Genredmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre','id' )

admin.site.register(Book, BookAdmin)