from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)
        return user


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
