from django.urls import path

from . import views


urlpatterns = [
    path('categories-list/', views.CategoryListAPIView.as_view(), name='category_list'),
    path('category-create/', views.CategoryCreateAPIView.as_view(), name='category_create'),
    path('category-detail/<int:id>/', views.CategoryDetailAPIView.as_view(), name='category_detail'),
    path('category-update/<int:id>/', views.CategoryUpdateAPIView.as_view(), name='category_detail'),
    path('category-delete/<int:id>/', views.CategoryDeleteAPIView.as_view(), name='category_delete'),

    path('games-list/', views.GameListAPIView.as_view(), name='game_list'),
    path('game-create/', views.GameCreateAPIView.as_view(), name='game_create'),
    path('game-detail/<int:id>/', views.GameDetailAPIView.as_view(), name='game_detail'),
    path('game-update/<int:id>/', views.GameUpdateAPIView.as_view(), name='game_update'),
    path('game-delete/<int:id>/', views.GameDeleteAPIView.as_view(), name='game_delete'),
]
