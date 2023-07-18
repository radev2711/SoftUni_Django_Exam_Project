from django.urls import path
from .views import GameCreateView, GameDetailsView, GameEditView, GameDeleteView

urlpatterns = [
    path('create/', GameCreateView.as_view(), name='game-create'),
    path('details/<int:pk>/', GameDetailsView.as_view(), name='game-details'),
    path('edit/<int:pk>/', GameEditView.as_view() , name='game-edit'),
    path('delete/<int:pk>/', GameDeleteView.as_view(), name='game-delete')
]