from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, ProfileForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from django.urls import reverse


def index(request):
    return render(request, 'user/index.html', {'title':'index'})


def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('user/profile')
        
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form':form, 'title':'register here'})



def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})



def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                print(request.POST) 
                return redirect('user/profile')  
            else:
                return HttpResponseNotAllowed('User not authenticated. Please log in.')  
        else:
            form_url = reverse('user/profile')  
            return HttpResponseNotAllowed(f'Form submission invalid. Please check your inputs. <a href="{form_url}">Go back to the form</a>')  
    else:
        return HttpResponseNotFound('Page not found. Please check the URL.')  

