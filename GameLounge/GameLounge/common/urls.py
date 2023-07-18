from django.urls import path
from .views import home_page, lounge_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('lounge/', lounge_page, name='lounge')
]