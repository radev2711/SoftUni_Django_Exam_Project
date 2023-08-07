from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import GameModel


class GameCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('game-create')
        self.lounge_url = reverse('lounge')
        self.staff_user = get_user_model().objects.create_user(
            email='staff@example.com',
            password='testpassword123',
            is_staff=True,
        )
        self.non_staff_user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpassword123',
        )
        self.valid_game_data = {
            'title': 'Test Game',
            'image': 'http://example.com/image.jpg',
            'genre': 'Action',
            'developer': 'Test Developer',
            'price': 19.99,
        }

        self.invalid_game_data = {
            'title': '',
            'price': -10,
        }

    def test_create_game_as_staff_user(self):

        self.client.login(email=self.staff_user.email, password='testpassword123')

        response = self.client.post(self.create_url, self.valid_game_data, follow=True)

        game_count = GameModel.objects.filter(title=self.valid_game_data['title']).count()
        self.assertEqual(game_count, 1)

        self.assertRedirects(response, self.lounge_url)

    def test_create_game_as_non_staff_user(self):

        self.client.login(email=self.non_staff_user.email, password='testpassword123')

        response = self.client.post(self.create_url, self.valid_game_data, follow=True)

        game_count = GameModel.objects.filter(title=self.valid_game_data['title']).count()
        self.assertEqual(game_count, 0)

        self.assertRedirects(response, self.lounge_url)

    def test_game_create_with_invalid_data(self):
        self.client.login(email=self.staff_user.email, password='testpassword123')
        response = self.client.post(self.create_url, self.invalid_game_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(GameModel.objects.exists())
