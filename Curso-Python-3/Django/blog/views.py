from django.shortcuts import render

# Create your views here.
def blog(request):
    print('Request from blog:', request)
    return render(request, 'blog/index.html') # blog

def exemplo(request):
    print('Request from blog:', request)
    return render(request, 'blog/exemplo.html') # blog