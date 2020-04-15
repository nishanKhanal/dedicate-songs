from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    search,
    PostCreateViewPublic,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    post_new_public_confirm,
    TestPostListView,
)

app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/',PostDetailView.as_view(),name="post_detail" ),
    path('<int:pk>/update/',PostUpdateView.as_view(),name="post_update" ),
    path('<int:pk>/delete/',PostDeleteView.as_view(),name="post_delete"),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('new_public/',PostCreateViewPublic.as_view(), name="post_new_public" ),
    path('search/', search,name="search"),
    path('new_public_confirm/',post_new_public_confirm, name="post_new_public_confirm" ),
    path('test_posts/',TestPostListView.as_view(), name="test_posts" )
]
