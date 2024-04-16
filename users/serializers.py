from django.contrib.auth.models import User
from rest_framework import serializers

#create seralizer(take user model instances and convert into native python serializer into json -also to deserilize parsed data and convert into user model isntances )

class userSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=False)
    username=serializers.CharField(read_only=True)
    #called upon post req
    def create(self, validated_data):
        password=validated_data.pop('password')
        user=User.objects.create(**validated_data)
        user.set_password(password) #all hashing logic is done
        user.save()
        return user
    
    class Meta:
        model=User
        fields=['url','id','username','email','first_name','last_name','password']