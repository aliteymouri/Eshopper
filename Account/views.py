from django.views.generic import View, CreateView, UpdateView, FormView
from .forms import SignInForm, SignUpForm, OtpForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from .mixins import AuthenticatedMixin, RequiredLoginMixin
from django.shortcuts import render, redirect, reverse
from Eshopper.settings import SMS
from django.urls import reverse_lazy
from .models import Otp, User
from random import randint
from uuid import uuid4


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
                return redirect('home:home')
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
            {'receptor': form.cleaned_data["phone"], 'type': '1', 'templates': 'randecode', 'param1': code}
        )
        token = str(uuid4())
        Otp.objects.create(phone=form.cleaned_data['phone'], code=code, token=token)
        print(code)
        return redirect(reverse('Account:otp') + f'?token={token}')

    def get(self, *args, **kwargs):
        return super(SignUpView, self).get(*args, **kwargs)


class CheckOtpView(AuthenticatedMixin, FormView):
    template_name = 'account/otp.html'
    form_class = OtpForm

    def form_valid(self, form):
        token = self.request.GET.get('token')
        if Otp.objects.filter(code=form.cleaned_data['code'], token=token).exists():
            otp = Otp.objects.get(token=token)
            user = User.objects.get(phone=otp.phone)
            user.is_active = True
            user.save()
            login(self.request, user)
            otp.delete()
            return redirect('home:home')
        else:
            form.add_error('code', 'Code is invalid')
        return render(self.request, self.template_name, {"form": form})


class EditProfileView(RequiredLoginMixin, UpdateView):
    template_name = 'account/edit_profile.html'
    success_url = reverse_lazy('home:home')
    form_class = EditProfileForm
    model = User

    def get_object(self, *args, **kwargs):
        return self.request.user

