from django.shortcuts import render
from .serializers import ArticleSerializer,AuthorSerializer,CategorieSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from .models import Article,Author,Categorie
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class ArticleViewset(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset= Article.objects.all()
    serializer_class=ArticleSerializer

class AuthorViewset(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset= Author.objects.all()
    serializer_class=AuthorSerializer

class CategorieViewset(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset= Categorie.objects.all()
    serializer_class=CategorieSerializer