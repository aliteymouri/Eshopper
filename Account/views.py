from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SignInForm


class SignInView(View):
    template_name = 'account/sign_in.html'
    form_class = SignInForm

    def get(self, req):
        form = self.form_class
        return render(req, self.template_name, {"form": form})

    def post(self, req):
        form = self.form_class(req.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(req, user)
                return redirect('Home:home')
            else:
                form.add_error('email', "User not found please try again")
        return render(req, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, req):
        logout(req)
        return redirect('Account:sign_in')
