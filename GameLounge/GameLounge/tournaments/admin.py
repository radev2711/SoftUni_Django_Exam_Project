from django.contrib import admin
from .models import TournamentModel


@admin.register(TournamentModel)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_game', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')