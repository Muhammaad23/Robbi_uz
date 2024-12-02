# views.py
from rest_framework import viewsets
from .models import Restaurants, Restaurant_info, Menu
from .serializers import RestaurantSerializer, RestaurantInfoSerializer, MenuSerializer
from django_filters import rest_framework as filters


class RestaurantsFilter(filters.FilterSet):
    address = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Restaurants
        fields = ['address']

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RestaurantsFilter

class RestaurantInfoViewSet(viewsets.ModelViewSet):
    queryset = Restaurant_info.objects.all()
    serializer_class = RestaurantInfoSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
