from rest_framework import serializers

from ..models.domain import Domain


class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = '__all__'
