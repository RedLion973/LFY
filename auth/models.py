from django.db import models
from django.contrib.auth.models import User

def get_avatar_upload_to(instance, filename):
    return settings.MEDIA_ROOT + 'user/' + instance.user.id + '/' + filename

class LFYUserProfile(models.Model):
    # Attributes
    user = models.ForeignKey(User, unique=True)
    avatar = models.ImageField(upload_to=get_avatar_upload_to)

    # Methods
    def __unicode__(self):
	return u'Profil de %s' % (self.user)

    def create_user_profile(sender, instance, created, **kwargs):  
        if created:  
            profile, created = UserProfile.objects.get_or_create(user=instance)  
        post_save.connect(create_user_profile, sender=User)

    # Meta
    class Meta:
	(verbose_name, verbose_name_plural) = (u'Profil Utilisateur', u'Profils Utilisateurs')
