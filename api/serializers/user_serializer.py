from rest_framework import serializers

from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer is a ModelSerializer for the User model.
    This serializer automatically generates fields based on the User model and includes all fields in the model.
    Attributes:
        Meta (class): A nested class that defines the metadata options for the serializer.
            model (User): The model that the serializer is based on.
            fields (str): Specifies that all fields in the model should be included in the serializer.
    """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username',
                  'email', 'password', 'date_joined', 'last_login']
        read_only_fields = ['date_joined', 'last_login']
        write_only_fields = ['password']
