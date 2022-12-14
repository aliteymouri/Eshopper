from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('products', views.ProductListView.as_view(), name='product_list'),
    path('search', views.SearchView.as_view(), name='search'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category_detail'),
]
