from django.db.models import Q
from django.shortcuts import render, redirect
from Product.models import Product, Category, Comment
from django.views.generic import DetailView, ListView, View


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product

    def post(self, req, *args, **kwargs):
        text = req.POST.get('text')
        if text:
            Comment.objects.create(text=text, author=req.user, product=self.get_object())
        return redirect('product:product_detail', self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:5]
        return context


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


class CategoryDetailView(View):
    template_name = 'product/category_detail.html'

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        products = category.categories.all()
        return render(request, self.template_name, {'products': products})
