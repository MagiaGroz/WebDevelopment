from rest_framework import serializers

from api.models import Company,Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(max_length=1000)
    city = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    def create(self, validated_data):
        category = Company.objects.create(validated_data)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('name', instance.description)
        instance.city = validated_data.get('name', instance.city)
        instance.address = validated_data.get('name', instance.address)
        instance.save()
        return instance