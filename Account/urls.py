from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from . import views

app_name = 'Account'
urlpatterns = [
    path('sign_in', views.SignInView.as_view(), name='sign_in'),
    path('sign_up', views.SignUpView.as_view(), name='sign_up'),
    path('logout', LogoutView.as_view(next_page='home:home'), name='logout'),
    path('otp', views.CheckOtpView.as_view(), name='otp'),
    path('editprofile/<int:pk>/change', views.EditProfileView.as_view(), name='edit_profile'),
]


