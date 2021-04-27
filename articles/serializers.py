from rest_framework.serializers import ModelSerializer
from .models import Author,Categorie,Article

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','birthdate','nationality']

class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id','name']

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','content','author','categorie','last_modified']
