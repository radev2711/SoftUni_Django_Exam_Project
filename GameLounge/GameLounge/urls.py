
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('GameLounge.common.urls')),
    path("accounts/", include('GameLounge.accounts.urls')),
    path("games/", include('GameLounge.games.urls')),
    path("reviews/", include('GameLounge.game_reviews.urls')),
    path("tourneys/", include('GameLounge.tournaments.urls')),
]
