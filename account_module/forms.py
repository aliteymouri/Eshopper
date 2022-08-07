from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.shortcuts import redirect


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput({'class': "input100", "placeholder": "ایمیل"}))
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput({'class': "input100", "placeholder": "نام کاربری"}))
    password_1 = forms.CharField(widget=forms.PasswordInput({'class': "input100", "placeholder": "رمزعبور"}))
    password_2 = forms.CharField(widget=forms.PasswordInput({'class': "input100", "placeholder": " تکرار رمزعبور"}))

    def clean(self):
        if self.cleaned_data.get('password_1') != self.cleaned_data.get('password_2'):
            raise ValidationError('رمزعبور مشابه نیست')
        elif User.objects.filter(username=self.cleaned_data['username']):
            raise ValidationError(' نام کاربری از قبل وجود دارد ')
        elif User.objects.filter(email=self.cleaned_data['email']):
            raise ValidationError('ایمیل وارد شده از قبل وجود دارد')
