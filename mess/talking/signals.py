from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.conf import settings
import os
from .models import ActiveUser


@receiver(pre_save, sender=ActiveUser)
def delete_old_avatar(sender, instance, **kwargs):
    try:
        old_instance = ActiveUser.objects.get(pk=instance.pk)
        if old_instance.avatar:
            if not old_instance.avatar.name == 'avatars/default_avatar.jpg':
                path = os.path.join(settings.MEDIA_ROOT, old_instance.avatar.name)
                if os.path.exists(path):
                    os.remove(path)
    except ActiveUser.DoesNotExist:
        pass
