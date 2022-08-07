from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.urls import reverse_lazy


def register(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password_1 = form.cleaned_data.get('password_1')
            User.objects.create(email=email, username=username, password=password_1)
            return redirect('index:index')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {"form": form})
