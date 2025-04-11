from rest_framework import viewsets

from ..models.item import Item
from ..serializers.item_serializer import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all().order_by('-name')
    serializer_class = ItemSerializer
