from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from posts.models import Post
# Register your models here.

class PostInline(admin.StackedInline):
    model = Post
    extra = 1


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff']
    inlines = [
        PostInline,
    ]


admin.site.register(CustomUser, CustomUserAdmin)
