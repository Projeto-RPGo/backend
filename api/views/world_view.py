from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.world import World
from ..serializers.world_serializer import WorldSerializer


class WorldViewSet(viewsets.ModelViewSet):
    """
    WorldViewSet is a viewset for handling CRUD operations on the World model.
    Attributes:
        queryset (QuerySet): A queryset of all World objects ordered by name in descending order.
        serializer_class (Serializer): The serializer class used for serializing and deserializing World objects.
        permission_classes (list): A list of permission classes that determine access control. Uncomment to enforce authentication.
    Methods:
        perform_create(serializer):
            Saves a new World instance with the current user as one of the users.
    """
    queryset = World.objects.all().order_by('-name')
    serializer_class = WorldSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Handles the GET request to list all worlds.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response containing the list of worlds.
        """

        return super().list(request)

    def create(self, request):
        """
        Handles the HTTP POST request to create a new world.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the created world.
        """

        return super().create(request)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP GET request to retrieve a single world.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the item to retrieve.
        Returns:
            Response: The HTTP response object containing the world.
        """

        return super().retrieve(request, pk, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP PUT request to update an world.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the item to update.
        Returns:
            Response: The HTTP response object containing the updated world.
        """

        return super().update(request, pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Partially update a world.
        This method handles HTTP PATCH requests to partially update a resource
        identified by the primary key (pk). It delegates the actual update
        operation to the parent class's `partial_update` method.
        Args:
            request (Request): The HTTP request object containing the partial
                               update data.
            pk (str, optional): The primary key of the resource to be updated.
        Returns:
            Response: The HTTP response object returned by the parent class's
                      `partial_update` method.
        """

        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Deletes a world instance.
        Args:
            request (Request): The HTTP request object.
            pk (int, optional): The primary key of the world instance to be deleted.
        Returns:
            Response: The HTTP response after the world instance is deleted.
        """

        return super().destroy(request, pk, *args, **kwargs)

    def perform_create(self, serializer):
        """
        Overrides the default perform_create method to save the serializer
        with the current user as part of the users list.
        Args:
            serializer (Serializer): The serializer instance to be saved.
        """

        serializer.save(users=[self.request.user], creator=self.request.user, admins=[
                        self.request.user])
