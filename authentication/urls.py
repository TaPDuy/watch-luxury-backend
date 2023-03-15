from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterView, LoginView, VerifyEmailView,
    UserView, change_password
)


urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserView.as_view(), name="users"),
    path('users/<int:id>/', UserView.as_view(), name="user"),
    path('users/<int:id>/change_password/', change_password, name='change_password'),
    path('verify/', VerifyEmailView.as_view(), name="verify_email"),
)