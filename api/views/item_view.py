from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.item import Item
from ..serializers.item_serializer import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all().order_by('-name')
    serializer_class = ItemSerializer

    @action(detail=False, methods=['get'], url_path='by-character/(?P<character_id>[^/.]+)')
    def get_items_by_character(self, request, character_id=None):
        """
        Custom endpoint to retrieve all items for a given character ID.
        """
        items = self.queryset.filter(character_id=character_id)
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)
