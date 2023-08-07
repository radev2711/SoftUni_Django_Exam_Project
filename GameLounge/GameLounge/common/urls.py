from django.urls import path
from .views import home_page, lounge_page #show_404

urlpatterns = [
    path('', home_page, name='home-page'),
    path('lounge/', lounge_page, name='lounge')
    # path('err/', show_404 ,name='page404')
]