from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text="<ul><li>Used for Login</li></ul>",widget=forms.TextInput(attrs={'placeholder':'cherised_empire'}))
    full_name = forms.CharField(max_length=20,help_text="<ul><li>Shown in Posts</li></ul>",widget=forms.TextInput(attrs={'placeholder':'Jane Doe', 'name':'full_name'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('full_name',) 

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
