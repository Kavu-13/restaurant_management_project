from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemByCategoryView(APIView):
    def get(self, request):
        category_name = request.query_params.get("category", None)
        if category_name:
            items = MenuItem.objects.filter(category_name_iexact=category_name)
        else:
            items = MenuItem.objects.all()

        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)