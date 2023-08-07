from django.contrib import admin
from .models import GameModel


@admin.register(GameModel)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'genre',)
    list_filter = ('genre', 'price')
    search_fields = ('title', 'genre')
    ordering = ('pk',)

