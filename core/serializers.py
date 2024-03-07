from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'name','email','password']
        extra_kwargs = {
            'password': {'write_only' : True}
        }#password wont retun in the response because it is a write only    

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # this hashes the password created
        instance.save()
        return instance
