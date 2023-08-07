from django.shortcuts import render
from GameLounge.games.models import GameModel
from GameLounge.games.forms import SearchForGameForm


# def show_404(request):
#     return render(request, '404.html')


def home_page(request):
    return render(request, 'common/home_page.html')


def lounge_page(request):
    all_games = GameModel.objects.all()
    search_form = SearchForGameForm()

    if request.method == 'POST':
        search_form = SearchForGameForm(request.POST)
        if search_form.is_valid():
            all_games = GameModel.objects.filter(title__icontains=search_form.cleaned_data['title_string'])

    context = {
        "games": all_games,
        "search_form": search_form
    }

    return render(request, 'common/lounge.html', context)
