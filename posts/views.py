from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    CreateView,
    ListView
)
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.db.models import Q
from django.conf import settings

from .models import Post
from .forms import PostForm

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
    object_list = Post.objects.filter(Q(post_from__contains=search_string) | Q(post_to__contains=search_string) | Q(video_title__contains=search_string))
    object_list =object_list.order_by('-date_created')
    return render(request, 'posts/post_list.html', {'object_list': object_list})


def index(request):
    return HttpResponse("Index page")

class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    ordering = ['-date_created']
    paginate_by = 8


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_new.html"
    # fields = ['post_from', 'post_to', 'message', 'song_description']
    success_url = reverse_lazy('posts:post_list')



    def form_valid(self, form):
        self.object = form.save()
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
        self.object.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())

