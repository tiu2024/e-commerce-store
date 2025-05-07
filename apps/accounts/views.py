from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid:
            user = form.get_user()
            login(request, user)

        
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {'form': form})