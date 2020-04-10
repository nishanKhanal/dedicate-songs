from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    search
)

app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('search/', search,name="search")
]
