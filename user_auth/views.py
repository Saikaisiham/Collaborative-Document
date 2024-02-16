from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, ProfileForm
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from django.contrib.auth import logout
from .models import Profile, Notification

@login_required
def index(request): 
    profile = Profile.objects.get(user=request.user) 
    return render(request, 'user/index.html', {'title':'index', 'profile':profile})


def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('/user/profile')
        
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
            messages.info(request, f'account done not exit please sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})



def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        print("Files:", request.FILES)  
        if form.is_valid():
            if request.user.is_authenticated:
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                print("Profile saved:", profile)  
                return redirect('/user/index')
            else:
                return HttpResponseNotAllowed('User not authenticated. Please log in.')
        else:
            print("Form errors:", form.errors)  
            return render(request, 'user/profile.html', {'form': form, 'error_message': 'Form submission invalid. Please check your inputs.'})
    else:
        form = ProfileForm()
        return render(request, 'user/profile.html', {'form': form})
    

def logout_request(request):
    logout(request)
    return redirect('/') 


def notifications_view(request):
    user_notifications = Notification.objects.filter(user=request.user)
    notification_count = user_notifications.count()
    return render(request, 'user/index.html', {'notifications': user_notifications})