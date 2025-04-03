from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.character import Character
from ..serializers.character_serializer import CharacterSerializer


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


class CharacterViewSet(viewsets.ModelViewSet):
    """
    CharacterViewSet is a ViewSet for handling character-related operations such as listing, creating, retrieving, updating, and deleting characters.
    Attributes:
        queryset (QuerySet): A Django QuerySet containing all Character objects, ordered by the 'name' field in descending order.
        serializer_class (Serializer): The serializer class used to validate and serialize Character objects.
    """

    queryset = Character.objects.all().order_by('-name')
    serializer_class = CharacterSerializer
    permission_classes = [IsSuperuserOrOwnProfile]

    def list(self, request):
        """
        Handles the GET request to list all characters.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the list of characters.
        """

        return super().list(request)

    def create(self, request):
        """
        Handles the HTTP POST request to create a new character.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the created character.
        """

        return super().create(request)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP GET request to retrieve a single character.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the character to retrieve.
        Returns:
            Response: The HTTP response object containing the character.
        """

        return super().retrieve(request, pk, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP PUT request to update a character.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the character to update.
        Returns:
            Response: The HTTP response object containing the updated character.
        """

        return super().update(request, pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP PATCH request to partially update a character.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the character to update.
        Returns:
            Response: The HTTP response object containing the updated character.
        """

        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP DELETE request to delete a character.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the character to delete.
        Returns:
            Response: The HTTP response object containing a success message.
        """

        return super().destroy(request, pk, *args, **kwargs)

    @action(detail=False, methods=['GET'], url_path='user/(?P<user_id>[^/.]+)')
    def user_characters(self, request, user_id=None):
        """
        Custom endpoint to retrieve characters belonging to a specific user.
        """
        characters = Character.objects.filter(
            user_id=user_id).order_by('-name')
        serializer = self.get_serializer(characters, many=True)
        return Response(serializer.data)
