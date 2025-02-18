from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import User
from ..models.user import User
from ..serializers.user_serializer import UserSerializer


class IsSuperuserOrOwnProfile(permissions.BasePermission):
    """
    Custom permission that allows superusers to perform any action.
    Regular users can only update or delete their own profile.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == obj:
            return True

        return False


class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet is a viewset for handling user-related operations.
    Attributes:
        queryset (QuerySet): A queryset of all User objects ordered by first name in descending order.
        serializer_class (Serializer): The serializer class used for serializing and deserializing User objects.
        permission_classes (list): A list of permission classes that determine access control for this viewset.
    """
    queryset = User.objects.all().order_by('-name')
    serializer_class = UserSerializer
    # permission_classes = [IsSuperuserOrOwnProfile]

    def list(self, request):
        """
        Handles the GET request to list all users.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the list of users.
        """

        return super().list(request)

    def create(self, request):
        """
        Handles the HTTP POST request to create a new user.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the created user.
        """

        return super().create(request)

    def retrieve(self, request, pk=None):
        """
        Handles the HTTP GET request to retrieve a single user.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user to retrieve.
        Returns:
            Response: The HTTP response object containing the user.
        """

        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        """
        Handles the HTTP PUT request to update a user.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user to update.
        Returns:
            Response: The HTTP response object containing the updated user.
        """

        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        """
        Handles the HTTP PATCH request to partially update a user.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user to update.
        Returns:
            Response: The HTTP response object containing the updated user.
        """

        return super().partial_update(request, pk)

    def destroy(self, request, pk=None):
        """
        Handles the HTTP DELETE request to delete a user.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user to delete.
        Returns:
            Response: The HTTP response object containing a success message.
        """

        return super().destroy(request, pk)
