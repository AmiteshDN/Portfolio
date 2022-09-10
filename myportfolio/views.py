from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'myportfolio/html/index.html')

def blog(request):
    return render(request, 'myportfolio/html/blog.html')
