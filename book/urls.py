from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookView

router = DefaultRouter()
router.register('', BookView)

urlpatterns = router.urls
