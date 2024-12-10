from django.http import HttpResponse

# Create your views here.

def home(request):
    print('Request:', request,'home')
    return HttpResponse("Hello, Home APP!")