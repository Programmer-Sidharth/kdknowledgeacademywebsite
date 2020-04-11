from django.shortcuts import render
from django.contrib.auth.models import User, auth
def prices(request):
    return render(request, 'prices.html')

def location(request):
    return render(request, 'location.html')


