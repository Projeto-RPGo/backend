from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.character import Character
from ..models.sale import Sale
from ..serializers import PurchaseSerializer, SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('-id')
    serializer_class = SaleSerializer

    @action(detail=True, methods=['post'], serializer_class=PurchaseSerializer)
    def purchase(self, request, pk=None):
        sale = get_object_or_404(Sale, pk=pk)

        if sale.status != 'pending':
            return Response({'error': 'This item is no longer available for sale'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            buyer_id = serializer.validated_data['buyer_id']
            buyer = get_object_or_404(Character, pk=buyer_id)

            if buyer.euros < sale.price:
                return Response({'error': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)

            buyer.euros -= sale.price
            sale.seller.euros += sale.price
            buyer.save()
            sale.seller.save()

            sale.item.character_id = buyer
            sale.item.save()

            sale.status = 'completed'
            sale.save()

            return Response({'message': 'Purchase successful!'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
