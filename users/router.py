from rest_framework import routers
from .viewset import userViewset

app_name="users" #app should include router.py file
#creates a default router
router=routers.DefaultRouter()
router.register('users',userViewset) #/users endpoint
