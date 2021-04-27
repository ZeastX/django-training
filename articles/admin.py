from django.contrib import admin
from .models import Author,Categorie,Article

# Register your models here.

admin.register(Author)
admin.register(Article)
admin.register(Categorie)