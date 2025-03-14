from rest_framework import viewsets

from ..models.npc import NPC
from ..serializers.npc_serializer import NPCSerializer


class NPCViewSet(viewsets.ModelViewSet):

    queryset = NPC.objects.all().order_by('-name')
    serializer_class = NPCSerializer

    def list(self, request):
        """
        Handles the GET request to list all NPCs.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the list of NPCs.
        """

        return super().list(request)

    def create(self, request):
        """
        Handles the HTTP POST request to create a new NPC.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the created NPC.
        """

        return super().create(request)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP GET request to retrieve a single NPC.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the NPC to retrieve.
        Returns:
            Response: The HTTP response object containing the NPC.
        """

        return super().retrieve(request, pk, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP PUT request to update a NPC.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the NPC to update.
        Returns:
            Response: The HTTP response object containing the updated NPC.
        """

        return super().update(request, pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP PATCH request to partially update a NPC.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the NPC to update.
        Returns:
            Response: The HTTP response object containing the updated NPC.
        """

        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP DELETE request to delete a NPC.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the NPC to delete.
        Returns:
            Response: The HTTP response object containing a success message.
        """

        return super().destroy(request, pk, *args, **kwargs)
