from rest_framework import generics
from django.shortcuts import render
from .serializers import CategoryDeleteSerializer, CategoryListSerializer, CategoryCreateSerializer,\
                         CategoryDetailSerializer, CategoryUpdateSerializer
from .serializers import GameCreateSerializer, GameDeleteSerializer, GameDetailSerializer,\
                         GameListSerializer, GameUpdateSerializer

from .models import Category, Game, Company


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'


class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_field = 'id'


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field = 'id'
