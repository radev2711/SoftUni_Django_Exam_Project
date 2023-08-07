from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TournamentCreateForm
from GameLounge.tournaments.models import TournamentModel


class TournamentCreateView(UserPassesTestMixin, CreateView):
    form_class = TournamentCreateForm
    template_name = 'tournaments/tournament_create.html'
    success_url = reverse_lazy('tourney-all')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('tourney-all')


class TournamentDetailsView(DetailView):
    model = TournamentModel
    template_name = 'tournaments/tournament_details.html'


class TournamentEditView(UserPassesTestMixin, UpdateView):
    model = TournamentModel
    form_class = TournamentCreateForm
    template_name = 'tournaments/tournament_edit.html'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('tourney-all')

    def get_success_url(self):
        return reverse_lazy('tourney-details', kwargs={'pk':self.object.pk})


class TournamentDeleteView(UserPassesTestMixin, DeleteView):
    model = TournamentModel
    template_name = 'tournaments/tournament_delete.html'
    success_url = reverse_lazy('tourney-all')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('tourney-all')


def show_tournaments_view(request):
    tourneys = TournamentModel.objects.all()
    context = {
        "tourneys": tourneys,
    }
    return render(request, 'tournaments/tournaments.html', context)


def join_tournaments_view(request, pk):
    tournament = TournamentModel.objects.get(pk=pk)
    tournament.participants.add(request.user)
    return redirect('tourney-details', pk=tournament.pk)