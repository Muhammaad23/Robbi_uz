from django.urls import path
from .views import RestaurantViewSet, RestaurantInfoViewSet, MenuViewSet

restaurant_list = RestaurantViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

restaurant_detail = RestaurantViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

restaurant_info_list = RestaurantInfoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

restaurant_info_detail = RestaurantInfoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

menu_list = MenuViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

menu_detail = MenuViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('restaurants/', restaurant_list, name='restaurant-list'),
    path('restaurants/<int:pk>/', restaurant_detail, name='restaurant-detail'),
    path('restaurant-info/', restaurant_info_list, name='restaurant-info-list'),
    path('restaurant-info/<int:pk>/', restaurant_info_detail, name='restaurant-info-detail'),
    path('menu/', menu_list, name='menu-list'),
    path('menu/<int:pk>/', menu_detail, name='menu-detail'),
]
