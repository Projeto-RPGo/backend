from rest_framework import serializers

from ..models.affiliation import Affiliation


class AffiliationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Affiliation
        fields = '__all__'