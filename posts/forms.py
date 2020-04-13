from django import forms

from .models import Post

help_text = """
    Examples:
    <ul>
        <li>Believer</li>
        <li>Bimbaakash Najeek lyrics</li>
        <li>Working Class Hero by Green Day</li>
        <li>Tmro Nyano</li>
        <li>Rap God</li>
        <li>Mayama by Sushant Kc</li>
    </ul>
"""

placeholder = """
If nothing else, I hope you know that I love you so much with every ounce of my being. I hope you realize your importance not only to me, but to everyone who has been lucky enough to know you. I hope you know that when you're feeling down, I only ever strive for your happiness. I hope you remember that no matter what, I'm here for you and fully intended of saying this for quite some time. I hope you recognize the fact that I appreciate and adore you without restraints, and that will never ever change.
"""

class PostForm(forms.ModelForm):
    #  post_from = forms.CharField(label="From",widget=forms.TextInput(attrs={'placeholder': 'Ram Bahadur'}))
     post_to = forms.CharField(label="To",widget=forms.TextInput(attrs={'placeholder': 'Sita Kumari'}))
     message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': placeholder}))
     song_description = forms.CharField(label="Song Info",help_text=help_text,widget=forms.TextInput(attrs={'placeholder': 'Dance Monkey with lyrics'}))

     class Meta:
        model = Post
        fields = ['post_to', 'message', 'song_description']

class PostFormPublic(forms.ModelForm):
    post_from_public = forms.CharField(label="From", required= True,widget=forms.TextInput(attrs={'placeholder': 'Ram Bahadur', 'name': 'post_from_public'}))
    post_to = forms.CharField(label="To",widget=forms.TextInput(attrs={'placeholder': 'Sita Kumari'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': placeholder}))
    song_description = forms.CharField(label="Song Info",help_text=help_text,widget=forms.TextInput(attrs={'placeholder': 'Dance Monkey'}))

    class Meta:
        model = Post
        fields = ['post_from_public', 'post_to', 'message', 'song_description']