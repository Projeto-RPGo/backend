from rest_framework import serializers

from api.models.character import Character
from api.models.sale import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class PurchaseSerializer(serializers.Serializer):
    buyer_id = serializers.IntegerField()
