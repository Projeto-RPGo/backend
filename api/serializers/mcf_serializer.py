from rest_framework import serializers

from ..models.mcf import MCF


class MCFSerializer(serializers.ModelSerializer):
    """
    MCFSerializer is a ModelSerializer for the MCF model.
    This serializer automatically generates fields based on the User model and includes all fields in the model.
    Attributes:
        Meta (class): A nested class that defines the metadata options for the serializer.
            model (User): The model that the serializer is based on.
            fields (str): Specifies that all fields in the model should be included in the serializer.
    """

    class Meta:
        model = MCF
        fields = '__all__'
