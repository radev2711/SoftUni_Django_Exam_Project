from django.test import TestCase, Client
from django.urls import reverse
from .models import ProfileModel
from .forms import CreateProfileForm


class ProfileModelTests(TestCase):
    VALID_CREDENTIALS = {
        'email': 'test@test.com',
        'password': 'somePass42'
        }

    INVALID_MAIL_DATA = {
        'email': 'test@test',
        'password': 'somePass42'
        }

    def test_all_valid_expect_create(self):
        user = ProfileModel.objects.create(**self.VALID_CREDENTIALS)
        self.assertIsNotNone(user.pk)

    def test_invalid_mail_expect_raise(self):
        form = CreateProfileForm(data=self.INVALID_MAIL_DATA)
        form_is_valid = form.is_valid()

        self.assertFalse(form_is_valid)

        with self.assertRaises(ValueError):
            form.save()


class UserEditViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = ProfileModel.objects.create_user(
            email='test@example.com',
            nickname='testuser',
            age=25,
            password='testpassword123'
        )
        self.edit_url = reverse('user-edit', kwargs={'pk': self.user.pk})
        self.user_data = {
            'email': 'test@example.com',
            'nickname': 'a' * 51,
            'age': 25,
        }

    def test_user_edit_with_long_nickname(self):
        self.client.login(email=self.user.email, password='testpassword123')

        user = ProfileModel.objects.get(pk=self.user.pk)
        response = self.client.post(self.edit_url, self.user_data)

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'nickname', 'Ensure this value has at most 50 characters (it has 51).')
        self.assertEqual(user.nickname, 'testuser')

    def test_user_edit_with_negative_age(self):
        self.client.login(email=self.user.email, password='testpassword123')
        self.user_data['age'] = -10

        user = ProfileModel.objects.get(pk=self.user.pk)
        response = self.client.post(self.edit_url, self.user_data)

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'age', 'Ensure this value is greater than or equal to 0.')
        self.assertEqual(user.age, 25)

    def test_user_edit_with_correct_age_and_nickname(self):
        self.client.login(email=self.user.email, password='testpassword123')
        self.user_data['nickname'] = 'newnickname'
        self.user_data['age'] = 30

        user = ProfileModel.objects.get(pk=self.user.pk)
        response = self.client.post(self.edit_url, self.user_data)

        self.assertRedirects(response, reverse('user-details', kwargs={'pk': self.user.pk}))
        self.assertEqual(user.nickname, 'testuser')
        self.assertEqual(user.age, 25)

