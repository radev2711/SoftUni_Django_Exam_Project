from django.contrib import admin
from .models import ReviewModel, RateGameModel


@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('to_game', 'from_user', 'text')


@admin.register(RateGameModel)
class RateGameAdmin(admin.ModelAdmin):
    list_display = ('to_game', 'rating', 'from_user')
    ordering = ('to_game',)