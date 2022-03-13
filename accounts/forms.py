from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class SignupForm(UserCreationForm):
    username = forms.CharField(label='ID for Login', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': 'Special Characters and Blanks are not allowed',
    }))

    nickname = forms.CharField(label='Nick Name')
    picture = forms.ImageField(label='Profile Picture', required=False)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('This nickname is already in use.')
        return nickname

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if not picture:
            picture = None
        return picture

    def save(self):
        user = super().save()
        Profile.objects.create(
            user=user,
            nickname = self.cleaned_data['nickname'],
            picture=self.cleaned_data['picture'],
        )
        return user

