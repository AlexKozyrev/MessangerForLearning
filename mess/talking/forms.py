from django import forms
from .models import ActiveUser


class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = ActiveUser
        fields = ['nickname', 'avatar']
