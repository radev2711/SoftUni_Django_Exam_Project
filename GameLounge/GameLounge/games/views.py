from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import GameCreateForm
from .models import GameModel
from GameLounge.game_reviews.models import ReviewModel, RateGameModel

User = get_user_model()


class GameCreateView(UserPassesTestMixin, CreateView):
    form_class = GameCreateForm
    template_name = 'games/game_create.html'
    success_url = reverse_lazy('lounge')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('lounge')


class GameDetailsView(DetailView):
    model = GameModel
    template_name = 'games/game_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        game = self.get_object()
        reviews = ReviewModel.objects.filter(to_game=game)

        game_ratings = RateGameModel.objects.filter(to_game=game)
        n_ratings = [r.rating for r in game_ratings]
        average_rating = 5
        if n_ratings:
            average_rating = sum(n_ratings) / len(n_ratings)

        context['reviews'] = reviews
        context['rating'] = average_rating
        context['num_ratings'] = len(n_ratings)

        return context


class GameEditView(UserPassesTestMixin, UpdateView):
    model = GameModel
    form_class = GameCreateForm
    template_name = 'games/game_edit.html'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('lounge')

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk':self.object.pk})


class GameDeleteView(UserPassesTestMixin, DeleteView):
    model = GameModel
    template_name = 'games/game_delete.html'
    success_url = reverse_lazy('lounge')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('lounge')