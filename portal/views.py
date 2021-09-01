from django.shortcuts import render

from users.models import JobSeeker


def home_page(request):
    return render(request, 'home_page.html')
