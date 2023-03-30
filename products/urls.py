from django.urls import path

from .views import ProductView, ProductsView, get_categories


urlpatterns = (
    path('', ProductsView.as_view(), name="products"),
    path('<int:id>/', ProductView.as_view(), name="product"),
    path('categories/', get_categories, name="categories"),
)
