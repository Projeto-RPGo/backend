from rest_framework import viewsets

from ..models.user import User
from ..serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet is a ViewSet for handling user-related operations such as listing, creating, retrieving, updating, and deleting users.
    Attributes:
        queryset (QuerySet): A Django QuerySet containing all User objects, ordered by the 'first_name' field in descending order.
        serializer_class (Serializer): The serializer class used to validate and serialize User objects.
    """

    queryset = User.objects.all().order_by('-first_name')
    serializer_class = UserSerializer
