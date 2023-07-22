from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'accounts/signup.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/login.html')
