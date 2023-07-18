from django.urls import path
from .views import AddReviewView, ReviewEditView, ReviewDeleteView, RateGameView

urlpatterns = [
    path('rate/<int:game_id>/', RateGameView.as_view(), name='rate-game'),
    path('create/<int:game_id>/<int:user_id>/', AddReviewView.as_view(), name='review-create'),
    path('edit/<int:pk>/', ReviewEditView.as_view(), name='review-edit'),
    path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='review-delete')
]