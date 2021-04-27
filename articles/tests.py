from django.test import TestCase
from .models import Article,Author,Categorie
from datetime import date

# Create your tests here.

class ArticleTest(TestCase):
    def setUp(self):
        boss=Author.objects.create(name='ok',nationality='fr',birthdate=date.today())
        categ=Categorie.objects.create(name='lourd')
        art = Article.objects.create(title='ooh',content='aah',last_modified=date(2018,2,25))
        art.author.add(boss)
        art.categorie.add(categ)

    def test_last_modified(self):
        boss=Author.objects.create(name='ok',nationality='fr',birthdate=date.today())
        categ=Categorie.objects.create(name='lourd')
        art=Article.objects.create(title='ooh',content='aah')
        art.author.add(boss)
        art.categorie.add(categ)
        art.last_modified = date(2018,12,25)
        self.assertNotEqual(art.last_modified,date.today())
        art.save()
        self.assertEqual(art.last_modified,date.today())

