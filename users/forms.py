from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(help_text="Required for password reset purpose")
    username = forms.CharField(max_length=20, help_text="Used for Login" ,widget=forms.TextInput(attrs={'placeholder':'cherised_empire'}))
    full_name = forms.CharField(max_length=20,help_text="Shown in Posts",widget=forms.TextInput(attrs={'placeholder':'Jane Doe', 'name':'full_name'}))


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('full_name', 'email') 

    field_order = ['username', 'full_name', 'email', 'password1', 'password2']
    

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
