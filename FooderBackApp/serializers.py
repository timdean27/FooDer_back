from rest_framework import serializers
from .models import Gfood

class GfoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gfood
        fields = '__all__'