from django.urls import path, include
from .views import get_all_books, BookView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BookView)

urlpatterns = router.urls
