from rest_framework import serializers
from . import models
class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.PlayList
