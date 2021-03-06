from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_view(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('events:home')
        else:
            messages.success(request, f"There was an error login in:{username}@{password}")
            return redirect('members:login')
    return render(request, 'members/login.html')
