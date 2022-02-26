from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    photo = forms.ImageField(label='', required=False)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content', 
        'row': 5, 
        'cols': 50, 
        'placeholder': 'Up to 140 charactors.',
    }))
    
    class Meta:
        model = Post
        fields = ['photo', 'content']
    
    