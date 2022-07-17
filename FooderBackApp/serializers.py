from rest_framework import serializers
from .models import Gfood

class GfoodSerializer(serializers.HyperlinkedModelSerializer):

    gfood_url = serializers.ModelSerializer.serializer_url_field(
        view_name='gfood_detail'
    )       
    class Meta:
        model = Gfood
        fields = ('id','gfood_url', 'name', 'image_url', 'created_at')