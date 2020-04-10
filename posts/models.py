from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    post_from = models.CharField(max_length=50)
    post_to = models.CharField(max_length=50)
    message = models.TextField(default=" ")
    video_link = models.CharField(max_length=200, default="https://youtube.com")
    embed_link = models.CharField(max_length=200, default="https://www.youtube.com/embed/video_id?controls=1")
    song_description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    video_title = models.CharField(max_length=250, default='Title of this song')

    def __str__(self):
        return f"from: {self.post_from}, to: {self.post_to}, message:{self.message}"

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.pk})
    
