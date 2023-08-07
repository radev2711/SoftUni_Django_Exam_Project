from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import AddReviewForm, RateGameForm
from .forms import ReviewModel, RateGameModel
from GameLounge.games.models import GameModel
from GameLounge.accounts.models import ProfileModel


class AddReviewView(LoginRequiredMixin, CreateView):
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


class ReviewEditView(LoginRequiredMixin, UpdateView):
    form_class = AddReviewForm
    template_name = 'game_reviews/review_edit.html'
    success_url = reverse_lazy('lounge')

    def get_queryset(self):
        return ReviewModel.objects.filter(from_user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.object.to_game.pk})


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = ReviewModel
    template_name = 'game_reviews/review_delete.html'
    success_url = reverse_lazy('lounge')

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.object.to_game.pk})


class RateGameView(LoginRequiredMixin,  FormView):
    template_name = 'game_reviews/rate_game.html'
    form_class = RateGameForm
    success_url = reverse_lazy('lounge')

    def get_initial(self):
        game_id = self.kwargs['game_id']
        user = self.request.user
        initial_data = {}

        existing_rating = RateGameModel.objects.filter(to_game_id=game_id, from_user=user).first()

        if existing_rating:
            initial_data['rating'] = existing_rating.rating

        initial_data['to_game'] = game_id
        initial_data['from_user'] = user.id
        return initial_data

    def form_valid(self, form):
        game_id = self.kwargs['game_id']
        user = self.request.user
        rating_value = form.cleaned_data['rating']

        existing_rating = RateGameModel.objects.filter(to_game_id=game_id, from_user=user).first()

        if existing_rating:
            existing_rating.rating = rating_value
            existing_rating.save()
        else:
            game = get_object_or_404(GameModel, pk=game_id)
            RateGameModel.objects.create(to_game=game, from_user=user, rating=rating_value)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.kwargs['game_id']})
