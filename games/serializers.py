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
        fields = '__all__'


class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description')


class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('category', 'author', 'title', 'description', 'country',
                  'price', 'price_free', 'RAM', 'support_on_windows', 'support_on_mac',
                  'support_on_linux', 'is_published', 'list_date', 'photo_main',
                  'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6')


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GameDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
