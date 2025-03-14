from rest_framework import viewsets

from ..models.maxdom import MaxDom
from ..serializers.maxdom_serializer import MaxDomSerializer


class MaxDomViewSet(viewsets.ModelViewSet):
    """
    RaceViewSet is a ViewSet for handling race-related operations such as listing, creating, retrieving, updating, and deleting races.
    Attributes:
        queryset (QuerySet): A Django QuerySet containing all Race objects, ordered by the 'name' field in descending order.
        serializer_class (Serializer): The serializer class used to validate and serialize Race objects.
    """

    queryset = MaxDom.objects.all().order_by('-name')
    serializer_class = MaxDomSerializer

    def list(self, request):
        """
        Handles the GET request to list all races.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the list of races.
        """

        return super().list(request)

    def create(self, request):
        """
        Handles the HTTP POST request to create a new race.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the created race.
        """

        return super().create(request)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP GET request to retrieve a single race.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the race to retrieve.
        Returns:
            Response: The HTTP response object containing the race.
        """

        return super().retrieve(request, pk, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP PUT request to update a race.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the race to update.
        Returns:
            Response: The HTTP response object containing the updated race.
        """

        return super().update(request, pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP PATCH request to partially update a race.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the race to update.
        Returns:
            Response: The HTTP response object containing the updated race.
        """

        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP DELETE request to delete a race.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the race to delete.
        Returns:
            Response: The HTTP response object containing a success message.
        """

        return super().destroy(request, pk, *args, **kwargs)
