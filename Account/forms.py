from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ValidationError
from .models import User
from django import forms


def start_with_09(value):
    if value[:2] != "09" or len(value) < 11:
        raise forms.ValidationError('Please enter a valid phone', code='start_with_09')


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password ',
                               widget=forms.PasswordInput({"placeholder": "password", 'class': 'form-control'}))
    confirm_password = forms.CharField(label='confirm_password',
                                       widget=forms.PasswordInput(
                                           {"placeholder": "Repeat password", 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone', 'password')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("passwords didn't match")
        elif len(password and confirm_password) < 8:
            raise ValidationError("your password is less than 8 characters")
        return confirm_password

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError("Please enter a valid phone")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="to change password <a href=\"../password/\">click here</a>"
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError("Please enter a valid phone")
        return phone

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone', 'password', 'image', 'is_active', 'is_admin')


class SignInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput({'class': "form-control", "placeholder": "Email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput({'class': "form-control", "placeholder": "Password", }),
    )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput({'class': "form-control", "placeholder": "Email"}),
    )
    fullname = forms.CharField(
        widget=forms.TextInput({'class': "form-control", "placeholder": "Fullname"}),
    )
    phone = forms.CharField(
        widget=forms.TextInput({'class': "form-control", "placeholder": "Phone", 'maxlength': 11}),
        validators=[start_with_09]
    )


class OtpForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput({'class': "form-control", "placeholder": "Code", 'maxlength': 4}),
    )
