from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# Create your views here.
def home(request):
    """
    Written by Rohan Nunugonda. Simple methods that respond their corresponding HTML
    page.
    """
    return render(request, 'forum/index.html')

def termsAndConditions(request):
    return render(request, 'forum/termsConditions.html')

def about(request):
    return render(request, 'forum/about.html')


# def newPost(request):
#     template = 'forum/newPost.html'
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     else:
#         form = PostForm()
#     context = {'form':form}
#     return render(request, template, context)

class AddPostView(CreateView):
    """
    Written by Rohan Nunugonda. Class that uses the Post model to create a form that 
    allows users to add a post. Originally used forms.py to do this but redacted this 
    way of doing it. Code based on tutorial from this video: https://www.youtube.com/watch?v=m3efqF9abyg&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=4 
    """
    model = Post
    template_name = 'forum/newPost.html'
    fields = '__all__'

class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/postDetails.html'

