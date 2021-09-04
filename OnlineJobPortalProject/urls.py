from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from portal.forms import UserLoginForm
from portal.views import jobseeker_register, employer_register, login_request, home_page



urlpatterns = [
    path('emoloyer/', include('employer.urls')),
    path('', home_page, name='home-page'),
    path('admin/', admin.site.urls),
    path('register/', jobseeker_register, name='register'),
    path('employer/register/', employer_register, name='employer-register'),
    path('login/', login_request, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    