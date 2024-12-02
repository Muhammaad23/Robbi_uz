from django.urls import path
from .views import Hotel_informationView, Hotel_informationDetailView, HotelsViewSet

urlpatterns = [
    path('hotels/', HotelsViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotels'),
    path('hotel_information/', Hotel_informationView.as_view(), name='hotel-list'),  # List and create hotel
    path('hotel_information/<int:pk>/', Hotel_informationDetailView.as_view(), name='hotel-detail'),

]
