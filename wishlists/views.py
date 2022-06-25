from rest_framework import viewsets
from rest_framework.response import Response
from .models import Wishlist
from .serializers import WishlistSerializer
from .services import create_wishlist, get_wishlists

class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def create(self, request):
        buyer = self.request.data.get('buyer')
        items = self.request.data.get('items')
        store = int(self.request.data.get('store'))

        wishlist = create_wishlist(buyer, items, store)
        wishlist_data = WishlistSerializer(wishlist, many=False)

        return Response(wishlist_data.data)

def list(self, request):
    latitude = self.request.query_params.get('lat')
    longitude = self.request.query_params.get('lng')
    options = {}
    for key in ('buyer', 'whishmaster'):
        value = self.request.query_params.get(key)
        if value:
            options[key] = value
    
    whishlist = get_wishlists(
        float(latitude),
        float(longitude),
        options
    )

    wishlist_data = WhishlistSerializer(wishlist, many=True)
    return Response(whishlist_data.data)