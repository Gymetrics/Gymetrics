from rest_framework import serializers
from .models import Gym


class GymSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    location_name = serializers.CharField(max_length=250)
    image = serializers.CharField(max_length=250, required=False)
    number_of_people = serializers.IntegerField()
    capacity = serializers.IntegerField(required=False)

    def create(self, validated_data):
        
        return Gym.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.location_name = validated_data.get('location_name', instance.location_name)
        instance.number_of_people = validated_data.get('number_of_people', instance.number_of_people)
        instance.save()
        return instance
