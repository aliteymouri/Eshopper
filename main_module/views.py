from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from product_module.models import Category , Product


# Create your views here.


class HomeView (TemplateView):
    template_name = 'main/index.html'

