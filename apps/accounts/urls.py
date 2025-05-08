from django.urls import path
from .views import my_login, register

urlpatterns = [
    path('login/', my_login, name='login'),
    path('register/', register, name='register')
]