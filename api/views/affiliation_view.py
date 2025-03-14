from rest_framework import viewsets

from ..models.affiliation import Affiliation
from ..serializers.affiliation_serializer import AffiliationSerializer


class AffiliationViewSet(viewsets.ModelViewSet):

    queryset = Affiliation.objects.all().order_by('-name')
    serializer_class = AffiliationSerializer

    def list(self, request):
        """
        Handles the GET request to list all affiliantions.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the list of affiliantions.
        """

        return super().list(request)

    def create(self, request):
        """
        Handles the HTTP POST request to create a new affiliantion.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the created affiliantion.
        """

        return super().create(request)

    def retrieve(self, request, pk=None):
        """
        Handles the HTTP GET request to retrieve a single affiliantion.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the affiliantion to retrieve.
        Returns:
            Response: The HTTP response object containing the affiliantion.
        """

        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        """
        Handles the HTTP PUT request to update a affiliantion.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the affiliantion to update.
        Returns:
            Response: The HTTP response object containing the updated affiliantion.
        """

        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        """
        Handles the HTTP PATCH request to partially update a affiliantion.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the affiliantion to update.
        Returns:
            Response: The HTTP response object containing the updated affiliantion.
        """

        return super().partial_update(request, pk)

    def destroy(self, request, pk=None):
        """
        Handles the HTTP DELETE request to delete a affiliantion.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the affiliantion to delete.
        Returns:
            Response: The HTTP response object containing a success message.
        """

        return super().destroy(request, pk)
