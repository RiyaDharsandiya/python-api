#to avoid mannualy create a pofile when a user gets created (automate the profile process)
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Profile

#everytime we save in user model run this function
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    #just created then create profile and link to actual user
    if created:
        Profile.objects.create(user=instance) #instance=User


@receiver(pre_save,sender=User)
def set_username(sender,instance,**kwargs):
    #if no username then create
    if not instance.username: #instance=User
        username=f'{instance.first_name}_{instance.last_name}'.lower()
        counter=1
        while User.objects.filter(username=username):
            username=f'{instance.first_name}_{instance.last_name}_{counter}'.lower()
            counter+=1
        instance.username=username
