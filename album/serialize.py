from rest_framework import serializers
from . import models

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Album