from rest_framework import serializers
from . import models


class hello_serializers(serializers.Serializer):
    name = serializers.CharField(max_length=10)



class Userprofileserilazer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
    


    
    class Meta :
        model = models.User_profiels
        fields = ("id" , "name"  , "email"  , "password" )

        extra_kwargs = {
            "password":{
                "write_only" : True , 
                "style" : {"input_type" : "password"}     
                          
                          
          }
        }

    def create(self , validated_data) :
        user = models.User_profiels.objects1.create_user(
            name = validated_data["name"] ,
            email = validated_data["email"] ,
            password = validated_data["password"])


        print(validated_data["password"])
        return user 
    

    

