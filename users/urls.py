from django.urls import path

from .views import (
    UserView, change_password, get_users
)

urlpatterns = (
    path('', get_users, name="users"),
    path('<int:id>/', UserView.as_view(), name="user"),
    path('<int:id>/change_password/', change_password, name='change_password'),
)