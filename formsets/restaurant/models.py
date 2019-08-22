from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.

class Receta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('editar', kwargs={'receta_id': self.id})


class Ingrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion


class Instruccion(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    numero = models.PositiveSmallIntegerField(help_text='Paso número')
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion
