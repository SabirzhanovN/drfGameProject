from django.urls import path

from . import views


urlpatterns = [
    path('category-list/', views.CategoryListAPIView.as_view(), name='category_list'),
    path('category-create/', views.CategoryCreateAPIView.as_view(), name='category_create'),
    path('category-detail/<int:id>/', views.CategoryDetailAPIView.as_view(), name='category_detail'),
    path('category-update/<int:id>/', views.CategoryUpdateAPIView.as_view(), name='category_detail'),
    path('category-delete/<int:id>/', views.CategoryDeleteAPIView.as_view(), name='category_delete'),

]
