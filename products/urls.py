from django.urls import path

from .views import (
    ProductView, ProductsView, get_categories
)

from favorite.views import get_product_favorited_users


urlpatterns = (
    path('', ProductsView.as_view(), name="products"),
    path('<int:id>/', ProductView.as_view(), name="product"),
    path('categories/', get_categories, name="categories"),
    path('<int:id>/favorites/', get_product_favorited_users, name='favorite_users'),
)
