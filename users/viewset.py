#viewset-actions like CRUD operations
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import userSerializer
from .permission import isUserOwnerOrGetAndPostOnly

#inherit from ModelsViewSet
class userViewset(viewsets.ModelViewSet):
    permission_classes=[isUserOwnerOrGetAndPostOnly,]
    #all users in db
    queryset = User.objects.all()
    serializer_class=userSerializer