from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_page, name='login'),
    path('profile/', profile, name='profile'),
    path('confirm/<uuid:token>/', views.confirm_email, name='confirm-email'),
]