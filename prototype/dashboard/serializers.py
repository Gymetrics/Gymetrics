from rest_framework import serializers
from .models import Stream


class StreamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    status = serializers.CharField(max_length=50)
    live = serializers.BooleanField()

    def create(self, validated_data):
        """
        Used to create a new Stream using a set of pre-validated data

        Args:
            validated_data: A pre-validated set of data that can be used to create
                            a new instance of a Stream within the model

        Returns: The object that was just created

        """
        return Stream.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Takes an instance of a Stream within the model and updates data within the instance using a set of
        pre-validated data.

        Args:
            instance: The model instance of the stream to be updated
            validated_data: A set of pre-validated data that can be used to update the data within the instance

        Returns: The instance that was just updated with the new data applied

        """
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.live = validated_data.get('live', instance.live)
        instance.save()
        return instance
