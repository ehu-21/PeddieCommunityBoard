from django.shortcuts import render,redirect
from .forms import UserRegistration
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthorized_user

# Create your views here.
"""
This code was heavily dependent on the following two tutorials:
1. https://www.youtube.com/watch?v=6ypVV1Z2TYc
2. https://www.youtube.com/watch?v=KiENzOOeP0I 

"""

def home(request):
    return render(request,'userprofile/login.html')

def gauth(request):
    return render(request, 'userprofile/gauth.html')

@unauthorized_user #See decorators for code. 
def userRegistration(request):
    """
    File made and written by Rohan. Uses the UserRegistration model and other django methods
    to handle user registration for the site. 
    """
    form = UserRegistration()
    if request.method == 'POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.info(request, username+ ' your account is created. Login to continue.')
            return redirect('userprofile:login')
    context={'form': form} 
    return render(request,'userprofile/register.html',context)

@unauthorized_user
def userLogin(request):
    """
     File made and written by Rohan. Uses django methods
    to handle user login for the site. 
    """
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
    """
    File made and written by Rohan. Uses django methods to logout
    """
    logout(request)
    #return render(request, 'forum/index.html')
    return redirect('userprofile:login')

@login_required(login_url='userprofile:login') #profile page is only seen when user is logged in
def profile(request):
    return render(request, 'userprofile/profile.html')


    