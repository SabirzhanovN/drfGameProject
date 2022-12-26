from django.urls import path

from . import views

urlpatterns = [
    path('companies-list/', views.CompaniesListAPIView.as_view(), name='companies_list'),
    path('company-detail/<int:id>/', views.CompanyDetailAPIView.as_view(), name='company_detail'),
    path('company-create/', views.CompanyCreateAPIView.as_view(), name='company_create'),
    path('company-update/<int:id>/', views.CompanyUpdateAPIView.as_view(), name='company_update')
]