from rest_framework import serializers
from .models import Company


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',  'description', 'is_mvp')


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'