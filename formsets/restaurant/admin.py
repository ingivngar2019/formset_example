from django.contrib import admin
from .models import *

# Register your models here.
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo','descripcion', 'id')

admin.site.register(Receta, RecetaAdmin)

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'receta','id')

admin.site.register(Ingrediente, IngredienteAdmin)

class InstruccionAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'receta','id')

admin.site.register(Instruccion, InstruccionAdmin)
