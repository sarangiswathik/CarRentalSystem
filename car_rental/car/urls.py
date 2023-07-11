from django.urls import path

from .views import HomeView, ListCars, CarDetailView, SearchView, SearchResultView, rent_car, checkout, complete_order

app_name = 'car'

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('list/',ListCars.as_view(), name='list'),
    path('details/<int:pk>',CarDetailView.as_view(), name='detail'),
    path('search/',SearchView.as_view(), name='search'),
    path('search_results/',SearchResultView.as_view(), name='search_result'),
    path('rent/<int:pk>/',rent_car, name='rent'),
    path('checkout/<int:rental_id>/',checkout, name='checkout'),
    path('complete_order/',complete_order, name='complete'),
]