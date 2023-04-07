from django.urls import path

from .views import (
    UserView, change_password, get_users
)

from favorite.views import get_user_favorite_products


urlpatterns = (
    path('', get_users, name="users"),
    path('<int:id>/', UserView.as_view(), name="user"),
    path('<int:id>/change_password/', change_password, name='change_password'),
    path('<int:id>/favorites/', get_user_favorite_products, name='favorite_products'),
)