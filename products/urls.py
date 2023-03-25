from django.urls import path

from .views import ProductView, get_products


urlpatterns = (
    path('', get_products, name="products"),
    path('<int:id>/', ProductView.as_view(), name="product"),
)
