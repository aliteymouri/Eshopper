from django.views.generic import DetailView, ListView
from Product.models import Product


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product


class ProductListView(ListView):
    template_name = 'product/shop.html'
    model = Product
    paginate_by = 10
