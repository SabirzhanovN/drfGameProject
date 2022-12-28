from rest_framework import generics
from .models import Company
from .serializers import CompanyListSerializer, CompanyDetailSerializer, CompanyCreateSerializer, \
                         CompanyUpdateSerializer, CompanyDeleteSerializer


class CompaniesListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer


class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    lookup_field = 'id'


class CompanyCreateAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer


class CompanyUpdateAPIView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer
    lookup_field = 'id'


class CompanyDeleteAPIView(generics.DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDeleteSerializer
    lookup_field = 'id'