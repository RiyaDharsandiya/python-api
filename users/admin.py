from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields=('id',) #adds a column ID 


admin.site.register(Profile,ProfileAdmin)