from rest_framework import serializers
from .models import City, Street, Shop
from rest_framework.validators import UniqueTogetherValidator


#список городов
class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

#информация о городе
class CityDetailSerializer(serializers.ModelSerializer):
    def get_streets(self):
        streets = Street.objects.filter(city=self)  
        return [street.name for street in streets]
    City.streets = get_streets
    class Meta:
        model = City
        fields = ('name', 'streets')

#список улиц
class StreetListSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = Street
        fields = '__all__'

#информация о улице
class StreetDetailSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = Street
        fields = '__all__'

#создание улицы
class StreetCreateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Street
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Street.objects.all(),
                fields=['city', 'name'],
                message='В этом городе уже есть улица с таким названием'
            )
        ]

#список магазинов
class ShopListSerializer(serializers.ModelSerializer):
    street = serializers.SlugRelatedField(slug_field='name',read_only=True)
    city = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = Shop
        fields = ('id', 'street', 'city', 'name', 'house', 'opening_time', 'closing_time', 'status')

#информация о магазине
class ShopDetailSerializer(serializers.ModelSerializer):
    street = serializers.SlugRelatedField(slug_field='name',read_only=True)
    city = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = Shop
        fields = ('street', 'city', 'name', 'house', 'opening_time', 'closing_time', 'status')

#создание магазина
class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id','street', 'city', 'name', 'house', 'opening_time', 'closing_time', 'status')

