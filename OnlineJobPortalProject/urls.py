from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from users.forms import UserLoginForm
from users import views as user_views



urlpatterns = [
    path('', include('portal.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.jobseeker_register, name='register'),
    path('employer/register/', user_views.employer_register,
         name='employer-register'
    ),
    path('login/', user_views.login_request, name='login'),
    
]
