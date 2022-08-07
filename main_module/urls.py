from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.Index.as_view(),name='index')
]
