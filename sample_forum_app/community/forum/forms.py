from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    """
    Created by Rohan Nunugonda. This model creates the post form; however, this implementation
    was not needed after we used models.py
    """
    class Meta:
        model = Post
        fields = ['user', 'title', 'content']