from typing import Any
import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible

#deconstructible class will allow django to perfrom migratetions
@deconstructible
class generateProfileImagePath(object):
    def __init__(self):
        pass
    #instance->refers to profile
    def __call__(self,instance,filename):
        ext=filename.split('.')[-1]
        path=f'media/accounts/{instance.user.id}/images/'
        name=f'profile_image.{ext}'
        return os.path.join(path,name)
user_profile_image_path=generateProfileImagePath()



# class Profile inherits from models.model.
class Profile(models.Model):
                                   #delete profile on delete of user
    user=models.OneToOneField(User,on_delete=models.CASCADE) 
    image=models.FileField(upload_to=user_profile_image_path,blank=True,null=True)
    
    def __str__(self) :
        return f'{self.user.username}\'s Profile'
