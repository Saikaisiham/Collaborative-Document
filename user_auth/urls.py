from django.urls import path 
from .views import test

urlpatterns = [
	path('resgister', test, name='register')
]
