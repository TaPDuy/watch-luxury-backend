from django.urls import path

from .views import (
    RegisterView, LoginView, VerifyEmailView, RefreshView
)


urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', RefreshView.as_view(), name='token_refresh'),
    path('verify/', VerifyEmailView.as_view(), name="verify_email"),
)