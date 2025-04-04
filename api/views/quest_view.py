from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models.character import Character

from ..models.quest import Quest, QuestMember
from ..serializers.quest_serializer import QuestSerializer


class QuestViewSet(viewsets.ModelViewSet):
    """
    RaceViewSet is a ViewSet for handling race-related operations such as listing, creating, retrieving, updating, and deleting races.
    Attributes:
        queryset (QuerySet): A Django QuerySet containing all Race objects, ordered by the 'name' field in descending order.
        serializer_class (Serializer): The serializer class used to validate and serialize Race objects.
    """

    queryset = Quest.objects.all().order_by('-quest_id')
    serializer_class = QuestSerializer

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

    def retrieve(self, request, pk=None):
        """
        Handles the HTTP GET request to retrieve a single race.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the race to retrieve.
        Returns:
            Response: The HTTP response object containing the race.
        """

        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        """
        Handles the HTTP PUT request to update a race.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the race to update.
        Returns:
            Response: The HTTP response object containing the updated race.
        """

        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        """
        Handles the HTTP PATCH request to partially update a race.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the race to update.
        Returns:
            Response: The HTTP response object containing the updated race.
        """

        return super().partial_update(request, pk)

    def destroy(self, request, pk=None):
        """
        Handles the HTTP DELETE request to delete a race.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the race to delete.
        Returns:
            Response: The HTTP response object containing a success message.
        """

        return super().destroy(request, pk)

    @extend_schema(parameters=[{"name": "character_id", "in": "path", "required": True, "type": "integer"}])
    @action(detail=True, methods=['post'], url_path='add-character/(?P<character_id>[^/.]+)')
    def add_character_to_quest(self, _, pk=None, character_id=None):
        """
        Adiciona um personagem a uma quest.
        """
        quest = get_object_or_404(Quest, pk=pk)
        character = get_object_or_404(Character, pk=character_id)

        if QuestMember.objects.filter(quest=quest, character=character).exists():
            return Response({'detail': 'Character already in this quest.'}, status=status.HTTP_400_BAD_REQUEST)

        QuestMember.objects.create(
            quest=quest, character=character, xp=0, euros=0)

        return Response({'detail': 'Character added successfully to quest.'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='character/(?P<character_id>[^/.]+)')
    def quests_by_character(self, request, character_id):
        """
        Retorna uma lista de quests associadas a um determinado personagem.
        """
        character = get_object_or_404(Character, pk=character_id)
        quests = Quest.objects.filter(participants=character)

        serializer = self.get_serializer(quests, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)/quests')
    def quests_by_user(self, _, user_id):
        """
        Retorna uma lista de personagens de um usuário, e para cada personagem, uma lista de quests associadas.
        """
        characters = Character.objects.filter(user_id=user_id)

        result = []
        for character in characters:
            quests = Quest.objects.filter(participants=character)
            quest_data = QuestSerializer(quests, many=True).data

            result.append({
                'character_id': character.character_id,
                'character_name': character.name,
                'quests': quest_data
            })

        return Response(result, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='giver/(?P<giver_id>[^/.]+)')
    def quests_by_giver(self, _, giver_id):
        """
        Retorna todas as quests associadas a um determinado giver (usuário).
        """
        quests = Quest.objects.filter(giver_id=giver_id)

        serializer = self.get_serializer(quests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='status/(?P<status_value>[^/.]+)')
    def quests_by_status(self, _, status_value):
        """
        Retorna todas as quests com um determinado status.
        """
        quests = Quest.objects.filter(status=status_value)

        serializer = self.get_serializer(quests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
