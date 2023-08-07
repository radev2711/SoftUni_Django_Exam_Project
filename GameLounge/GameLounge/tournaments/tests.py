from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import TournamentModel, GameModel


class TournamentCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('tourney-create')
        self.tourney_all_url = reverse('tourney-all')

        self.staff_user = get_user_model().objects.create_user(
            email='staff@example.com',
            password='testpassword123',
            is_staff=True,
        )

        self.game = GameModel.objects.create(
            title='Test Game',
            image='http://example.com/image.jpg',
            genre='Action',
            developer='Test Developer',
            price=19.99,
        )

        self.valid_tournament_data = {
            'title': 'Test Tournament',
            'to_game': self.game.pk,
            'start_date': '2023-07-15 14:00',
            'end_date': '2023-07-16 18:00',
            'host': 'Test Host',
            'prise': 100,
        }

        self.invalid_tournament_data = {
            'title': '',
            'to_game': self.game.pk,
            'start_date': '2023-07-15 14:00',
            'end_date': '2023-07-16 18:00',
            'host': 'Test Host',
            'prise': -100,
        }

    def test_create_tournament_as_staff_user(self):
        self.client.login(email=self.staff_user.email, password='testpassword123')

        response = self.client.post(self.create_url, self.valid_tournament_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, self.tourney_all_url)
        self.assertTrue(TournamentModel.objects.exists())

    def test_create_tournament_as_non_staff_user(self):
        non_staff_user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpassword123',
        )

        self.client.login(email=non_staff_user.email, password='testpassword123')
        response = self.client.post(self.create_url, self.valid_tournament_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, self.tourney_all_url)
        self.assertFalse(TournamentModel.objects.exists())

    def test_tournament_create_with_invalid_data(self):
        self.client.login(email=self.staff_user.email, password='testpassword123')
        response = self.client.post(self.create_url, self.invalid_tournament_data)

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'This field is required.')
        self.assertFormError(response, 'form', 'prise', 'Ensure this value is greater than or equal to 0.')

        self.assertFalse(TournamentModel.objects.exists())

