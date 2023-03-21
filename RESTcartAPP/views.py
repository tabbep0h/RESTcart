from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerilizer
from .models import Cart

class CRUDCart(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            serializer = CartSerilizer(Cart.objects.all(), many=True)
        else:
            try:
                serializer = CartSerilizer(Cart.objects.get(pk=pk))
            except Cart.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def put(self, request, pk):
        try:
            product = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerilizer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            product = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_200_OK)
