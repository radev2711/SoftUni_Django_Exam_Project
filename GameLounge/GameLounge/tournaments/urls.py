from django.urls import path
from .views import TournamentCreateView, show_tournaments_view, TournamentDetailsView, TournamentEditView,\
    TournamentDeleteView, join_tournaments_view

urlpatterns = [
    path('all/', show_tournaments_view, name='tourney-all'),
    path('join/<int:pk>/',join_tournaments_view, name='tourney-join'),
    path('create/', TournamentCreateView.as_view(), name='tourney-create'),
    path('details/<int:pk>/', TournamentDetailsView.as_view(), name='tourney-details'),
    path('edit/<int:pk>/', TournamentEditView.as_view(), name='tourney-edit'),
    path('delete/<int:pk>/',TournamentDeleteView.as_view(), name='tourney-delete')
]