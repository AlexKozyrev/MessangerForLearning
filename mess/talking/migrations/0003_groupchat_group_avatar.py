# Generated by Django 4.2.11 on 2024-03-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talking', '0002_groupchat_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='group_avatar',
            field=models.ImageField(default='avatars/default_avatar.jpg', upload_to='avatars/'),
        ),
    ]