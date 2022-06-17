from rest_framework import viewsets
from rest_framework.response import Response
from .models import Wishlist
from .serializers import WishlistSerializer

class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
