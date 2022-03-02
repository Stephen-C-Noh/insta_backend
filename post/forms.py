from django import forms
from .models import Post, Comment

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
    
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'comment-form',
        'size': '70px',
        'placeholder': 'Add a comment...',
        'maxlength': '40', }))
    
    class Meta:
        model = Comment
        fields = ['content']