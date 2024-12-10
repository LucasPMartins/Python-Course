from django.urls import path
from . import views 

#blog/
urlpatterns = [
    path('',views.blog), # Blog
    path('exemplo/',views.exemplo), # Exemplo
]
