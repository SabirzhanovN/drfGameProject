from rest_framework import generics
from .models import Company
from .serializers import CompanyListSerializer, CompanyDetailSerializer, CompanyCreateSerializer, C


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

