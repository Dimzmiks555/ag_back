from rest_framework import serializers, fields

from .models import Etalon, EtalonProperty

class EtalonPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = EtalonProperty
        fields = ('id', 'name', 'value')




class EtalonSerializer(serializers.ModelSerializer):
    etalon_properties = EtalonPropertySerializer(many=True, required=False)

    def create(self, validated_data):
        etalon_properties = validated_data.pop('etalon_properties')
        etalon = Etalon.objects.create(**validated_data)
        for etalon_property in etalon_properties:
            EtalonProperty.objects.create(etalon=etalon, **etalon_property)
        return etalon

    def update(self, instance, validated_data):
        etalon_properties = validated_data.pop('etalon_properties')

        for item in validated_data:
            if Etalon._meta.get_field(item):
                setattr(instance, item, validated_data[item])

        EtalonProperty.objects.filter(etalon=instance).delete()

        for etalon_property in etalon_properties:
            EtalonProperty.objects.create(etalon=instance, **etalon_property)

        instance.save()
        return instance

    class Meta:
        model = Etalon
        fields = ('id','title', 'created_at', 'description', 'etalon_properties')
