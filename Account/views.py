from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from .forms import SignInForm, SignUpForm, OtpForm
from django.views.generic import View, CreateView
from .mixins import AuthenticatedMixin
from ShoppingGrill.settings import SMS
from .models import Otp, User
from random import randint


class SignInView(AuthenticatedMixin, View):
    template_name = 'account/sign_in.html'
    form_class = SignInForm

    def get(self, req):
        form = self.form_class
        return render(req, self.template_name, {"form": form})

    def post(self, req):
        form = self.form_class(req.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(req, user)
                return redirect('Home:home')
            else:
                form.add_error('email', "User not found please try again")
        return render(req, self.template_name, {"form": form})


class SignUpView(AuthenticatedMixin, CreateView):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        code = randint(1000, 9999)
        SMS.verification(
            {'receptor': form.cleaned_data["phone"], 'type': '1', 'template': 'randecode', 'param1': code}
        )
        Otp.objects.create(phone=form.cleaned_data['phone'], code=code)
        print(code)
        return redirect(reverse('Account:otp') + f'?phone={form.cleaned_data["phone"]}')

    def get(self, *args, **kwargs):
        return super(SignUpView, self).get(*args, **kwargs)


class CheckOtpView(View):
    template_name = 'account/verify_phone.html'
    form_class = OtpForm

    def get(self, req):
        form = self.form_class()
        return render(req, self.template_name, {'form': form})

    def post(self, req):
        form = self.form_class(req.POST)
        if form.is_valid():
            phone = req.GET.get('phone')
            if Otp.objects.filter(code=form.cleaned_data['code'], phone=phone).exists():
                user = User.objects.get(phone=phone)
                user.is_active = True
                user.save()
                login(req, user)
                return redirect('Home:home')
            else:
                form.add_error('code', 'code is invalid')
        return render(req, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, req):
        logout(req)
        return redirect('Account:sign_in')
