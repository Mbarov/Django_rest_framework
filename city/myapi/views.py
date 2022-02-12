from rest_framework import generics, filters
from rest_framework.response import Response
from datetime import datetime
from .serializers import *
from .models import City, Street, Shop


class CityCreateView(generics.CreateAPIView):
    """Создание города"""
    serializer_class = CityDetailSerializer


class CityListView(generics.ListAPIView):
    """Список городов"""
    serializer_class = CityListSerializer
    queryset = City.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id','name']


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация о городе"""
    serializer_class = CityDetailSerializer
    queryset = City.objects.all()



class StreetCreateView(generics.CreateAPIView):
    """Создание улицы"""
    serializer_class = StreetCreateSerializer


class StreetListView(generics.ListAPIView):
    """Список улиц"""
    serializer_class = StreetListSerializer
    queryset = Street.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id','name', 'city']


class StreetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация о улице"""
    serializer_class = StreetDetailSerializer
    queryset = Street.objects.all()



class ShopCreateView(generics.CreateAPIView):
    """Создание магазина"""
    serializer_class = ShopCreateSerializer
    def post(self, request):
        serializer = ShopCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'id':serializer.data['id']})



class ShopListView(generics.ListAPIView):
    """Список магазинов"""
    serializer_class = ShopListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'city', 'street', 'opening_time','closing_time']
    def get_queryset(self):
        queryset = Shop.objects.all()
        street = self.request.query_params.get('street')
        city = self.request.query_params.get('city')
        open = self.request.query_params.get('open')
        time_now = datetime.now().time().replace(microsecond=0)         
        try:
            queryset = queryset.filter(city__name__contains=city)
        except: None
        try:
            queryset = queryset.filter(street__name__contains=street)
        except: None
        try:
            if open == '1':
                queryset = queryset.filter(opening_time__lt=time_now,closing_time__gt=time_now)
            elif open == '0':
                queryset = queryset.exclude(opening_time__lt=time_now,closing_time__gt=time_now)
        except: None
        return queryset



class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Информация о магазине"""
    serializer_class = ShopDetailSerializer
    queryset = Shop.objects.all()

