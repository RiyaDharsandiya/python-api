#owner authenticated -all permissions but some users(unauthenticated) get only post and get method
from rest_framework import permissions
class isUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    ''' 
    custom permission for userViewset to only allow to edit their profile.Otherwise ,get and post only
    '''
    #called anythime incase of get /post
    def has_permission(self, request, view):
        return True
    
    #false-never called
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #owners can edit
        if not request.user.is_anonymous:
            return request.user==obj   #obj->user model object
        
        return False
