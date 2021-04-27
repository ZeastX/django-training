from rest_framework.routers import DefaultRouter
from .views import ArticleViewset,AuthorViewset,CategorieViewset

router = DefaultRouter()
router.register(r'categorie',CategorieViewset)
router.register(r'author',AuthorViewset)
router.register(r'article',ArticleViewset)
urlpatterns = router.urls
#setup du router