from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        widget=forms.TextInput(
           attrs={'placeholder': 'مثلا: علی محمدی',}
           )
        )
    email = forms.EmailField(
        label='آدرس ایمیل',
        widget=forms.EmailInput(
           attrs={'placeholder': 'آدرس ایمیل خود را وارد کنید'}
            )
        )
    password1 = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'رمز عبور خود را وارد کنید'}
            )
        )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'رمز عبور خود راتکرار کنید'}
            )
        )
    
    error_messages = {
        'password_mismatch': "رمز عبور برابر نیست",
    }
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلا استفاده شده")
        return email

    class Meta:
        model = User
        fields=['full_name', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='آدرس ایمیل',
        widget=forms.EmailInput(
           attrs={'placeholder': 'آدرس ایمیل خود را وارد کنید'}
        )
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'رمز عبور خود را وارد کنید'}
        )
    )