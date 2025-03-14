from rest_framework import viewsets

from ..models.domain import Domain
from ..serializers.domain_serializer import DomainSerializer


class DomainViewSet(viewsets.ModelViewSet):

    queryset = Domain.objects.all().order_by('-name')
    serializer_class = DomainSerializer

    def list(self, request):
        """
        Handles the GET request to list all domains.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the list of domains.
        """

        return super().list(request)

    def create(self, request):
        """
        Handles the HTTP POST request to create a new domain.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the created domain.
        """

        return super().create(request)

    def retrieve(self, request, pk=None):
        """
        Handles the HTTP GET request to retrieve a single domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to retrieve.
        Returns:
            Response: The HTTP response object containing the domain.
        """

        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        """
        Handles the HTTP PUT request to update a domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to update.
        Returns:
            Response: The HTTP response object containing the updated domain.
        """

        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        """
        Handles the HTTP PATCH request to partially update a domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to update.
        Returns:
            Response: The HTTP response object containing the updated domain.
        """

        return super().partial_update(request, pk)

    def destroy(self, request, pk=None):
        """
        Handles the HTTP DELETE request to delete a domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to delete.
        Returns:
            Response: The HTTP response object containing a success message.
        """

        return super().destroy(request, pk)
