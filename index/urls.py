from django.contrib import admin
from django.urls import (path, include)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from .views import login_view
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('book.urls')),
    path('users/', include('user.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html',
                                     redirect_authenticated_user=True,), name="login"),
    # path('login/', login_view),
    path('api/token/', obtain_auth_token),
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),
]
