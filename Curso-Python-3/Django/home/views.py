from django.shortcuts import render

# Create your views here.

def home(request):
    print('Request from home:', request)
    return render(request, 'home/index.html') # HOME