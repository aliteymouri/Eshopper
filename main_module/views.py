from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from product_module.models import Category , Product


# Create your views here.


class Index(TemplateView):
    template_name = 'main/index.html'

