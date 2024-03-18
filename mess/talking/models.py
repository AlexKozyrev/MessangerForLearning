from django.db import models
from django.contrib.auth.models import User


class ActiveUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg')
