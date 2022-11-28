from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ValidationError
from .models import User
from django import forms


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='گذرواژه ',
                               widget=forms.PasswordInput({"placeholder": "گذرواژه", "id": "pass"}))
    confirm_password = forms.CharField(label='تایید گذرواژه ',
                                       widget=forms.PasswordInput(
                                           {"placeholder": "تایید گذرواژه", "id": "confirm_pass"}))

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone', 'password')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("رمزعبور مشابه نیست")
        elif len(password and confirm_password) < 8:
            raise ValidationError("رمز عبور وارد شده کمتر از 8 کاراکتر میباشد")
        return confirm_password

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError("یک شماره تماس معتبر وارد کنید")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="برای تغییر گذرواژه <a href=\"../password/\">کلیک کنید</a>"
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError("یک شماره تماس معتبر وارد کنید")
        return phone

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone', 'password', 'image', 'is_active', 'is_admin')


class SignInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput({'class': "form-control", "placeholder": "Email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput({'class': "form-control", "placeholder": "Password",}),
    )


def start_with_09(value):
    if value[:2] != "09":
        raise forms.ValidationError('یک شماره تماس معتبر وارد کنید', code='start_with_09')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput({'class': "email-input", "placeholder": "پست الکترونیک"}),
    )
    fullname = forms.CharField(
        widget=forms.TextInput({'class': "email-input", "placeholder": "نام و نام خانوادگی"}),
    )
    phone_number = forms.CharField(
        widget=forms.TextInput({'class': "email-input", "placeholder": "شماره تماس", 'maxlength': 11}),
        validators=[start_with_09]
    )

