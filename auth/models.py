from django.db import models
from django.contrib.auth.models import User

def get_avatar_upload_to(instance, filename):
    return settings.MEDIA_ROOT + 'user/' + instance.user.id + '/' + filename

class LFYUserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    avatar = models.ImageField(upload_to=get_avatar_upload_to)
