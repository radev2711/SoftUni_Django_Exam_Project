from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AddReviewForm, RateGameForm
from .forms import ReviewModel, RateGameModel
from GameLounge.games.models import GameModel
from GameLounge.accounts.models import ProfileModel


class AddReviewView(CreateView):
    form_class = AddReviewForm
    template_name = 'game_reviews/review_create.html'
    success_url = reverse_lazy('lounge')

    def form_valid(self, form):
        game_id = self.kwargs['game_id']
        user_id = self.kwargs['user_id']

        game = get_object_or_404(GameModel, id=game_id)
        user = get_object_or_404(ProfileModel, id=user_id)

        form.instance.to_game = game
        form.instance.from_user = user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.object.to_game.pk})


class ReviewEditView(UpdateView):
    form_class = AddReviewForm
    template_name = 'game_reviews/review_edit.html'
    success_url = reverse_lazy('lounge')

    def get_queryset(self):
        return ReviewModel.objects.filter(from_user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.object.to_game.pk})


class ReviewDeleteView(DeleteView):
    model = ReviewModel
    template_name = 'game_reviews/review_delete.html'
    success_url = reverse_lazy('lounge')

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.object.to_game.pk})


class RateGameView(CreateView):
    form_class = RateGameForm
    template_name = 'game_reviews/rate_game.html'
    success_url = reverse_lazy('lounge')

    def form_valid(self, form):
        game_id = self.kwargs['game_id']
        user_id = self.request.user.id

        game = get_object_or_404(GameModel, id=game_id)
        user = get_object_or_404(ProfileModel, id=user_id)

        form.instance.to_game = game
        form.instance.from_user = user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.object.to_game.pk})
