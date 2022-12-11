from django.urls import path
from . import views

app_name = 'Product'
urlpatterns = [
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='product_detil')
]
