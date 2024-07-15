from rest_framework import serializers

from .models import Xarajatlar

class XarajatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xarajatlar
        fields = '__all__'