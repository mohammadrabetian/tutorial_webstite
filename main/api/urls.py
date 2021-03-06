from django.urls import path
from .views.homepage import homepage
from .views.register import register

app_name = 'main'

urlpatterns = [
    path('home/', homepage, name='homepage'),
    path('register/', register, name='register'),
]
