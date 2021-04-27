from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birthdate = models.DateField()
    def __str__(self):
        return self.name

class Categorie(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    categorie = models.ManyToManyField(Categorie)
    author = models.ManyToManyField(Author)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.title