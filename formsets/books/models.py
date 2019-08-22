from django.db import models

class Genre(models.Model):
    desc = models.CharField(max_length=50)

    class Meta:
        db_table = 'genre'
        verbose_name_plural = 'Generos'
        ordering = ('desc',)

    def __str__(self):
        return self.desc

# Create your models here.
class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)
    genre = models.ForeignKey(Genre,on_delete=models.PROTECT)

    class Meta:
        db_table = 'book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name


class Autor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name

class Libro(models.Model):
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.title


