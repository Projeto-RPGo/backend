from rest_framework import serializers

from ..models.world import World


class WorldSerializer(serializers.ModelSerializer):

    class Meta:
        model = World
        fields = '__all__'
        read_only_fields = ['users']
