from django.db.models import Q
from django.views.generic import DetailView, ListView
from Product.models import Product


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product


class ProductListView(ListView):
    template_name = 'product/shop.html'
    model = Product
    paginate_by = 10


class SearchView(ListView):
    template_name = "product/search.html"
    model = Product
    paginate_by = 1

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Product.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))

