from django.db import models

# Create your models here.

class Receta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion


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
