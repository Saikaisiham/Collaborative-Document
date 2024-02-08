from django.urls import path 
from .views import login_request, index, register_request, profile

urlpatterns = [
	path('', index, name='index'),
    path('register', register_request, name='register'),
    path('login', login_request, name='login'),
    path('profile', profile, name='profile')
]
