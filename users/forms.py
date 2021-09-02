
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        widget=forms.TextInput(
           attrs={'placeholder': 'مثلا: علی محمدی',}
           )
        )
    email = forms.EmailField(
        label='آدرس ایمیل',
        widget=forms.TextInput(
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
    
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='آدرس ایمیل',
        widget=forms.TextInput(
           attrs={'placeholder': 'آدرس ایمیل خود را وارد کنید'}
            )
        )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'رمز عبور خود را وارد کنید'}
            )
        )