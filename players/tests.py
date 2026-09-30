from django.test import Client, TestCase
from django.urls import reverse

from .models import Player


class PlayerOperationsTests(TestCase):
    def setUp(self):
        self.player = Player.objects.create(
            name='Player', steam_id='123', games_played=10, wins=4,
        )
        self.data = {
            'name': 'Renamed', 'steam_id': '456', 'games_played': '12', 'wins': '5',
        }
        self.edit_url = reverse('players:edit', args=[self.player.pk])
        self.delete_url = reverse('players:delete', args=[self.player.pk])

    def test_edit_displays_current_values_and_saves_same_player(self):
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].initial['games_played'], 10)
        self.assertContains(response, 'csrfmiddlewaretoken')
        response = self.client.post(self.edit_url, self.data)
        self.assertRedirects(response, reverse('players:list'))
        self.player.refresh_from_db()
        self.assertEqual(
            (self.player.name, self.player.steam_id, self.player.games_played, self.player.wins),
            ('Renamed', '456', 12, 5),
        )
        self.assertEqual(Player.objects.count(), 1)

    def test_invalid_numbers_do_not_change_player(self):
        for field in ('games_played', 'wins'):
            for value in ('abc', '1.5', '-1', '', '2147483648', '9' * 100):
                with self.subTest(field=field, value=value):
                    response = self.client.post(self.edit_url, {**self.data, field: value})
                    self.assertEqual(response.status_code, 200)
                    self.assertIn(field, response.context['form'].errors)
                    self.assertEqual(response.context['form'].data[field], value)
        for data in ({}, {**self.data, 'wins': '13'}):
            response = self.client.post(self.edit_url, data)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.context['form'].errors)
        self.player.refresh_from_db()
        self.assertEqual(
            (self.player.name, self.player.steam_id, self.player.games_played, self.player.wins),
            ('Player', '123', 10, 4),
        )

    def test_zero_and_equal_counters_are_valid(self):
        for value in ('0', '12', '2147483647'):
            with self.subTest(value=value):
                response = self.client.post(
                    self.edit_url, {**self.data, 'games_played': value, 'wins': value},
                )
                self.assertRedirects(response, reverse('players:list'))
                self.player.refresh_from_db()
                self.assertEqual(self.player.games_played, int(value))
                self.assertEqual(self.player.wins, int(value))

    def test_duplicate_steam_id_is_an_error_but_unchanged_id_is_valid(self):
        other = Player.objects.create(name='Player', steam_id='789')
        response = self.client.post(self.edit_url, {**self.data, 'steam_id': other.steam_id})
        self.assertIn('steam_id', response.context['form'].errors)
        self.player.refresh_from_db()
        self.assertEqual(self.player.steam_id, '123')
        response = self.client.post(self.edit_url, {**self.data, 'steam_id': '123'})
        self.assertRedirects(response, reverse('players:list'))
        other.refresh_from_db()
        self.assertEqual(other.name, 'Player')

    def test_delete_only_accepts_post_and_removes_target(self):
        other = Player.objects.create(name='Player', steam_id='789')
        for method in ('get', 'head', 'put', 'patch', 'delete', 'options'):
            with self.subTest(method=method):
                self.assertEqual(getattr(self.client, method)(self.delete_url).status_code, 405)
                self.assertTrue(Player.objects.filter(pk=self.player.pk).exists())
        response = self.client.post(self.delete_url)
        self.assertRedirects(response, reverse('players:list'))
        self.assertFalse(Player.objects.filter(pk=self.player.pk).exists())
        self.assertTrue(Player.objects.filter(pk=other.pk).exists())

    def test_missing_players_return_404(self):
        missing_pk = self.player.pk + 100
        edit_url = reverse('players:edit', args=[missing_pk])
        self.assertEqual(self.client.get(edit_url).status_code, 404)
        self.assertEqual(self.client.post(edit_url, self.data).status_code, 404)
        self.assertEqual(
            self.client.post(reverse('players:delete', args=[missing_pk])).status_code, 404,
        )

    def test_csrf_required_for_edit_and_delete(self):
        client = Client(enforce_csrf_checks=True)
        for url in (self.edit_url, self.delete_url):
            self.assertEqual(client.post(url, self.data).status_code, 403)
        self.player.refresh_from_db()
        self.assertEqual(self.player.name, 'Player')
        client.get(self.edit_url)
        token = client.cookies['csrftoken'].value
        self.assertRedirects(
            client.post(self.edit_url, {**self.data, 'csrfmiddlewaretoken': token}),
            reverse('players:list'),
        )
        self.assertRedirects(
            client.post(self.delete_url, {'csrfmiddlewaretoken': token}),
            reverse('players:list'),
        )
        self.assertFalse(Player.objects.filter(pk=self.player.pk).exists())

    def test_existing_pages_and_add_form_still_work(self):
        for name in ('players:list', 'players:list_alt'):
            response = self.client.get(reverse(name))
            self.assertContains(response, self.edit_url)
            self.assertContains(response, self.delete_url)
            self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertEqual(
            self.client.get(reverse('players:profile', args=[self.player.name])).status_code, 200,
        )
        client = Client(enforce_csrf_checks=True)
        add_url = reverse('stats:add_player')
        response = client.get(add_url)
        self.assertEqual(set(response.context['form'].fields), {'name', 'age'})
        self.assertEqual(client.post(add_url, {'name': 'New', 'age': '20'}).status_code, 403)
        token = client.cookies['csrftoken'].value
        response = client.post(add_url, {
            'name': 'New', 'age': '20', 'csrfmiddlewaretoken': token,
        })
        self.assertContains(response, 'Игрок New (20 лет) успешно добавлен.')
        self.assertEqual(Player.objects.count(), 1)
