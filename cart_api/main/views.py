from rest_framework import generics
from .models import Cart
from .serializer import CartSerializer


class CartApiView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
