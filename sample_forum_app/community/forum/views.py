from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# Create your views here.
def home(request):
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
    model = Post
    template_name = 'forum/newPost.html'
    fields = '__all__'

# class PostListView(ListView):
#     model = Post