from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import RegisterView, LoginView, UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserView.as_view(), name="users"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
