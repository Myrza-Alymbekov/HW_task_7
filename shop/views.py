from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Order, Item
from .permissions import IsSenderPermission, IsSenderAndOwnerPermission, IsBuyerAndOwnerPermission
from .serializers import ItemSerializer, OrderSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSenderPermission, ]


class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsSenderAndOwnerPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(category_id=self.kwargs.get('category_id'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            category_id=self.kwargs.get('category_id')
        )


class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsSenderAndOwnerPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(category_id=self.kwargs.get('category_id'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            category_id=self.kwargs.get('category_id')
        )


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsBuyerAndOwnerPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(item_id=self.kwargs.get('item_id'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            item_id=self.kwargs.get('item_id')
        )


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsBuyerAndOwnerPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(item_id=self.kwargs.get('item_id'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            item_id=self.kwargs.get('item_id')
        )
