from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from bootstrap_modal_forms.generic import BSModalCreateView

# Create your views here.
def home(request):
    return render(request, 'forum/index.html')

class PostCreateView(BSModalCreateView):
    template_name = 'templates/forum/create_post.html'
    form_class = PostForm
    success_message = 'Success: Post was created!'
    success_url = reverse_lazy('index')
