from django.urls import  path
from . import views, get_streets


urlpatterns = [
        path('city/create/', views.CityCreateView.as_view()),
        path('city/', views.CityListView.as_view()),
        path('city/<int:pk>/street/', views.CityDetailView.as_view()),

        path('street/create/', views.StreetCreateView.as_view()),
        path('street/', views.StreetListView.as_view()),
        path('street/<int:pk>/', views.StreetDetailView.as_view()),

        path('shop/', views.ShopCreateView.as_view()),
        path('shop/list/', views.ShopListView.as_view()),
        path('shop/<int:pk>/', views.ShopDetailView.as_view()),

        path('import/streets/<city_name>/', get_streets.get_all_streets),#импорт города и его улиц

]