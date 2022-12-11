from django.views.generic import DetailView
from Product.models import Product


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product


