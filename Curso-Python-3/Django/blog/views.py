from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('Request:', request)
    return HttpResponse("Hello, Blog APP!")

def exemplo(request):
    print('Request:', request)
    return HttpResponse("Hello, exemplo APP!")