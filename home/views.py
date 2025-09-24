from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory, MenuItem
from .serializers import MenuCategorySerializer, MenuItemSerializer
from rest_framework import viewset, status
from rest_framework.response import response
from rest_framework.pagination import PageNumberPagination

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuItemSearchPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class MenuItemSearchViewSet(viewset.Viewset):
    pagination_class = MenuItemSearchPagination

    def list(self, request):
        query = request.query_params.get('q', None)
        if not query:
            return Response({"error": "Please provide a search query (?q=)"}, status=status.HTTP_400_BAD_REQUEST)

        items = MenuItem.objects.filter(name_icontains=query)

        paginator = self.pagination_class()
        paginated_items = paginator.paginate_queryset(items, request)

        serializer = MenuItemSerializer(paginated_items, many=True)
        return paginator.get_paginated_response(serializer.data)