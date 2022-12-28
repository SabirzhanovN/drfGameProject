from rest_framework import generics
from django.shortcuts import render
from .serializers import CategoryDeleteSerializer, CategoryListSerializer, CategoryCreateSerializer,\
                         CategoryDetailSerializer, CategoryUpdateSerializer
from .serializers import GameCreateSerializer, GameDeleteSerializer, GameDetailSerializer,\
                         GameListSerializer, GameUpdateSerializer

from .models import Category, Game, Company

# Category model api


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

# Game model api


class GameListAPIView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer


class GameDetailAPIView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer
    lookup_field = 'id'


class GameCreateAPIView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateSerializer


class GameUpdateAPIView(generics.UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameUpdateSerializer
    lookup_field = 'id'


class GameDeleteAPIView(generics.DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDeleteSerializer
    lookup_field = 'id'
