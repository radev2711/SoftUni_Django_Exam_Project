from django.db import models
from GameLounge.accounts.models import ProfileModel
from GameLounge.games.models import GameModel


class TournamentModel(models.Model):
    title = models.CharField(max_length=50)
    to_game = models.ForeignKey(to=GameModel, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    host = models.CharField(max_length=50)
    prise = models.PositiveIntegerField()
    participants = models.ManyToManyField(ProfileModel, default=None, null=True, blank=True)
