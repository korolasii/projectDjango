from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import *


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
    else:
        form = AuthenticationForm()
    
    
    return render(request, 'members/login_or_signup.html', {'title':'Login','form':form})

def singup_view(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SingupForm()
    
    return render(request, 'members/login_or_signup.html', {'title':'Signup','form':form})


@login_required()
def profile_view(request):
    return render(request, 'members/profile.html')


@login_required()
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'members/login_or_signup.html', {'form':form})