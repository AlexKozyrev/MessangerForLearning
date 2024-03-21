from django.db import models
from django.contrib.auth.models import User


class ActiveUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg')


class GroupChat(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='group_chats')
    group_avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg')


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(ActiveUser, on_delete=models.CASCADE)
    group_chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
