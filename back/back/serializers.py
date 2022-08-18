from rest_framework import serializers, fields

from .models import Etalon, EtalonProperty

class EtalonPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = EtalonProperty
        fields = ('name', 'value')


class EtalonSerializer(serializers.ModelSerializer):
    etalon_properties = EtalonPropertySerializer(many=True)
    class Meta:
        model = Etalon
        fields = ('title', 'description', 'etalon_properties')
