from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views

app_name = 'Account'
urlpatterns = [
    path('sign_in', views.SignInView.as_view(), name='sign_in'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]
