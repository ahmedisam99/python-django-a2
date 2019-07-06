from django.contrib import admin
from django.urls import (path, include)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('books/', include('book.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
