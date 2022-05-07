from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete


def createProfile(sender, instance, created, **kwargs):
    print('updated successfully')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username, 
            email =user.email, 
            name= user.username,
        )






post_save.connect(createProfile, sender=User)
