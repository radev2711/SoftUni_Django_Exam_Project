from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TournamentCreateForm
from GameLounge.tournaments.models import TournamentModel


class TournamentCreateView(CreateView):
    form_class = TournamentCreateForm
    template_name = 'tournaments/tournament_create.html'
    success_url = reverse_lazy('tourney-all')


class TournamentDetailsView(DetailView):
    model = TournamentModel
    template_name = 'tournaments/tournament_details.html'


class TournamentEditView(UpdateView):
    model = TournamentModel
    form_class = TournamentCreateForm
    template_name = 'tournaments/tournament_edit.html'

    def get_success_url(self):
        return reverse_lazy('tourney-details', kwargs={'pk':self.object.pk})


class TournamentDeleteView(DeleteView):
    model = TournamentModel
    template_name = 'tournaments/tournament_delete.html'
    success_url = reverse_lazy('tourney-all')


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