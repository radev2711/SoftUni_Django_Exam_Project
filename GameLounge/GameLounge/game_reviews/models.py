from django.db import models
from GameLounge.accounts.models import ProfileModel
from GameLounge.games.models import GameModel


class ReviewModel(models.Model):
    text = models.TextField()
    date_of_publication = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    to_game = models.ForeignKey(GameModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_of_publication"]


class ReviewCommentModel(models.Model):
    text = models.TextField()
    from_user = models.OneToOneField(ProfileModel, on_delete=models.CASCADE)
    to_review = models.OneToOneField(ReviewModel, on_delete=models.CASCADE)


class RateGameModel(models.Model):
    GAME_RATINGS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    rating = models.PositiveIntegerField(choices=GAME_RATINGS, default=5)

    from_user = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    to_game = models.ForeignKey(GameModel, on_delete=models.CASCADE)
