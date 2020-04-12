from django import forms

from .models import Post

help_text = """
    Examples:
    <ul>
        <li>Believer</li>
        <li>Bimbaakash Najeek</li>
        <li>Working Class Hero by Green Day</li>
        <li>Tmro Nyano</li>
        <li>Rap God</li>
        <li>Mayama by Sushant Kc</li>
    </ul>
"""

class PostForm(forms.ModelForm):
    #  post_from = forms.CharField(label="From",widget=forms.TextInput(attrs={'placeholder': 'Ram Bahadur'}))
     post_to = forms.CharField(label="To",widget=forms.TextInput(attrs={'placeholder': 'Sita Kumari'}))
     message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Heartfelt Message'}))
     song_description = forms.CharField(label="Song Info",help_text=help_text,widget=forms.TextInput(attrs={'placeholder': 'Dance Monkey'}))

     class Meta:
        model = Post
        fields = ['post_to', 'message', 'song_description']

class PostFormPublic(forms.ModelForm):
    post_from_public = forms.CharField(label="From", required= True,widget=forms.TextInput(attrs={'placeholder': 'Ram Bahadur', 'name': 'post_from_public'}))
    post_to = forms.CharField(label="To",widget=forms.TextInput(attrs={'placeholder': 'Sita Kumari'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Heartfelt Message'}))
    song_description = forms.CharField(label="Song Info",help_text=help_text,widget=forms.TextInput(attrs={'placeholder': 'Dance Monkey'}))

    class Meta:
        model = Post
        fields = ['post_from_public', 'post_to', 'message', 'song_description']