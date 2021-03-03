from django.shortcuts import render,redirect
from .forms import UserRegistration
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthorized_user

# Create your views here.

def home(request):
    return render(request,'userprofile/login.html')

def gauth(request):
    return render(request, 'userprofile/gauth.html')

@unauthorized_user
def userRegistration(request):
    form = UserRegistration()
    if request.method == 'POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.info(request, username+ ' your account is created. Login to continue.')
            return redirect('userprofile:login')
    context={'form': form} #still need to understand why dict is being used here
    return render(request,'userprofile/register.html',context)

@unauthorized_user
def userLogin(request):
    if request.method=='POST':
        username=request.POST.get('username') #grabbing the username
        password=request.POST.get('password') #grabbing the password
        user=authenticate(request,username=username,password=password)
        if user is not None: #checking to see if the user exists
            login(request, user)
            return redirect('forum:home')
        else:
            messages.info(request, 'username or password is incorrect')
    return render(request,'userprofile/login.html')

def userLogout(request):
    logout(request)
    return render(request, 'forum/index.html')

@login_required(login_url='userprofile:login')
def profile(request):
    return render(request, 'userprofile/profile.html')


    