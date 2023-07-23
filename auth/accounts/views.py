from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm
from django.http import HttpResponse
from .models import EmailConfirmation


# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            send_confirmation_email(email) 
            return redirect('home')
    return render(request, 'accounts/signup.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        login(request, user)
        return redirect('profile')
    return render(request, 'accounts/login.html')

def send_confirmation_email(email):
    email_confirmation = EmailConfirmation.objects.create(email=email)
    subject = 'Confirm Your Email'
    confirmation_link = f'http://127.0.0.1:8000/confirm/{email_confirmation.token}'
    message = f'Please click the following link to confirm your email: {confirmation_link}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def confirm_email(request, token):
    try:
        email_confirmation = EmailConfirmation.objects.get(token=token)
    except EmailConfirmation.DoesNotExist:
        return redirect('signup')

    email_confirmation.is_confirmed = True
    email_confirmation.save()

    return redirect('profile')

def profile(request):
    return render(request, 'accounts/profile.html')