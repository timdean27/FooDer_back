from pyexpat import model
from rest_framework import serializers
from .models import Gfood
from django.contrib.auth.models import User

class GfoodSerializer(serializers.HyperlinkedModelSerializer):

    gfood_url = serializers.ModelSerializer.serializer_url_field(
        view_name='gfood_detail'
    )       
    class Meta:
        model = Gfood
        fields = ('id','gfood_url', 'name', 'image_url', 'user_string', 'created_at', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password')
        extra_kwargs = {'password': {
            'write_only':True,
            'required':True
        }}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user