from rest_framework import serializers
from .models import Category, Game


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'category', 'author', 'title', 'price', 'list_date')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__',)


class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__',)


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__',)


class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        files = ('__all__',)


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__',)


class GameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__',)


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__',)


class GameDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__',)
