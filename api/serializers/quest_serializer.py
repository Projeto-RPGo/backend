from rest_framework import serializers

from ..models.quest import Quest


class QuestSerializer(serializers.ModelSerializer):
    """
    QuestSerializer is a ModelSerializer for the Quest model.
    This serializer automatically generates fields based on the Quest model and includes all fields in the model.
    Attributes:
        Meta (class): A nested class that defines the metadata options for the serializer.
            model (Race): The model that the serializer is based on.
            fields (str): Specifies that all fields in the model should be included in the serializer.
    """

    class Meta:
        model = Quest
        fields = '__all__'
