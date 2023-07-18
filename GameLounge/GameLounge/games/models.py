from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from GameLounge.accounts.models import ProfileModel


class GameModel(models.Model):
    title = models.CharField(max_length=177)
    image = models.URLField()
    genre = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    rating = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class GameCommentModel(models.Model):
    text = models.TextField()
    from_user = models.OneToOneField(ProfileModel, on_delete=models.CASCADE)
    to_game = models.OneToOneField(GameModel, on_delete=models.CASCADE)


class GameRatingModel(models.Model):
    rate = models.PositiveIntegerField(validators=[MaxValueValidator(10.0)])
    from_user = models.OneToOneField(ProfileModel, on_delete=models.CASCADE)
    to_game = models.OneToOneField(GameModel, on_delete=models.CASCADE)
