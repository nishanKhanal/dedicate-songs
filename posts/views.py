from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView, 
    DeleteView
)
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post
from .forms import PostForm, PostFormPublic

import os

#python library imports
import requests 



# Create your views here.

def search(request):
    try:
        search_string = request.GET.get('search')
    except:
        search_string = ""
    
    print(search_string)
    object_list = Post.objects.filter(Q(post_from__username__contains=search_string)| Q(post_from__first_name__in=search_string) | Q(post_from__last_name__in=search_string) | Q(post_to__contains=search_string) | Q(video_title__contains=search_string))
    object_list =object_list.order_by('-date_created')
    return render(request, 'posts/post_list.html', {'object_list': object_list})


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    # ordering = ['-date_created']
    def get_queryset(self):
        posts = Post.objects.filter(test_post=False).order_by('-date_created')
        return posts
    paginate_by = 8

class TestPostListView(ListView):
    model = Post
    template_name = "posts/test_posts.html"
    def get_queryset(self):
        posts = Post.objects.filter(test_post=True).order_by('-date_created')
        return posts
    paginate_by = 8



class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_new.html"
    login_url = reverse_lazy('login')
    # fields = ['post_from', 'post_to', 'message', 'song_description']
    success_url = reverse_lazy('posts:post_list')



    def form_valid(self, form):
        self.object = form.instance
        search_url = "https://www.googleapis.com/youtube/v3/search"
        search_params = {
            'part': 'snippet',
            'q' : self.object.song_description,
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 1,
            'type': 'video'
            
        }
        response = requests.get(search_url,params=search_params)
        video_Id = response.json()['items'][0]['id']['videoId']
        self.object.video_link =f"https://www.youtube.com/watch?v={video_Id}"
        self.object.embed_link = self.object.embed_link.replace('video_id', video_Id)



        video_url = "https://www.googleapis.com/youtube/v3/videos"
        video_params = {
            'part': 'snippet',
            'id': video_Id,
            'maxResults':1,
            'key': settings.YOUTUBE_DATA_API_KEY,
        }
        response = requests.get(video_url,params=video_params)
        self.object.video_title = response.json()['items'][0]['snippet']['title']

        self.object.post_from = self.request.user
        # self.object.post_from_id = self.request.user.id

        self.object.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())


class PostCreateViewPublic(CreateView):
    model = Post
    form_class = PostFormPublic
    template_name = "posts/post_new_public.html"
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        self.object = form.instance
        search_url = "https://www.googleapis.com/youtube/v3/search"
        search_params = {
            'part': 'snippet',
            'q' : self.object.song_description,
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 1,
            'type': 'video'
            
        }
        response = requests.get(search_url,params=search_params)
        video_Id = response.json()['items'][0]['id']['videoId']
        self.object.video_link =f"https://www.youtube.com/watch?v={video_Id}"
        self.object.embed_link = self.object.embed_link.replace('video_id', video_Id)



        video_url = "https://www.googleapis.com/youtube/v3/videos"
        video_params = {
            'part': 'snippet',
            'id': video_Id,
            'maxResults':1,
            'key': settings.YOUTUBE_DATA_API_KEY,
        }
        response = requests.get(video_url,params=video_params)
        self.object.video_title = response.json()['items'][0]['snippet']['title']


        try:
            publicuser = get_user_model().objects.get(username="publicuser")
        except:
            publicuser = get_user_model().objects.create_user(username="publicuser")
        finally:
            self.object.post_from = publicuser
        self.object.post_from_public = form.cleaned_data['post_from_public']


        # Identifying test posts
        condition1 = self.object.post_from_public == self.object.post_to == self.object.message
        condition2 = 'test' in [self.object.post_from_public.lower(), self.object.post_to.lower()]
        if condition1 or condition2:
            print('something')
            self.object.test_post = True
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('posts:test_posts'))
        
        self.object.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = 'post'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    login_url = reverse_lazy('login')
    fields = ['post_to', 'message', 'song_description']

    def test_func(self):
        obj = self.get_object()
        return obj.post_from == self.request.user


    def form_valid(self, form):
        self.object = form.instance

        search_url = "https://www.googleapis.com/youtube/v3/search"

        search_params = {
            'part': 'snippet',
            'q' : self.object.song_description,
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 1,
            'type': 'video'
            
        }

        print(self.object.song_description)
        response = requests.get(search_url,params=search_params)
        video_Id = response.json()['items'][0]['id']['videoId']
        print(video_Id)
        self.object.video_link =f"https://www.youtube.com/watch?v={video_Id}"
        self.object.embed_link = f"https://www.youtube.com/embed/{video_Id}?controls=1"

        video_url = "https://www.googleapis.com/youtube/v3/videos"
        video_params = {
            'part': 'snippet',
            'id': video_Id,
            'maxResults':1,
            'key': settings.YOUTUBE_DATA_API_KEY,
        }
        response = requests.get(video_url,params=video_params)
        self.object.video_title = response.json()['items'][0]['snippet']['title']

        self.object.post_from = self.request.user
        # self.object.post_from_id = self.request.user.id

        self.object.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
        model = Post
        template_name = "posts/post_delete.html"
        context_object_name = "post"
        success_url = reverse_lazy('posts:post_list')

        def test_func(self):
            obj = self.get_object()
            return obj.post_from == self.request.user
    

def post_new_public_confirm(request):
    return render(request,'posts/post_new_public_confirm.html')