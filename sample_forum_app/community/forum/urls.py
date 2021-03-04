from django.contrib import admin
from django.urls import path
from . import views
# from .views import PostListView

app_name = "forum"

urlpatterns = [
    #Made by Rohan Nunugonda. Maps the forum urls. 
    # path('', PostListView.as_view(), name='postList')
    path('home/',views.home,name="home"),
    path('about/', views.about, name="about"),
    path('termsConditions/', views.termsAndConditions, name="termsConditions"),
    #path('newPost/', views.newPost, name="newPost"),
    path('newPost/', views.AddPostView.as_view(), name='newPost'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='postDetail'),
   
    
]
