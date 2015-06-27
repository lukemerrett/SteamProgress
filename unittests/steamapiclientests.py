__author__ = 'Luke Merrett'

import settings
import unittest
from clients.steamapi import SteamApiClient

class SteamAPIClientTests(unittest.TestCase):
    def setUp(self):
        self.client = SteamApiClient()

    def test_get_player_summary_returns_json_dictionary(self):
        json = self.client.get_player_summary()

        self.assertTrue(isinstance(json, dict))

        player = json['response']['players'][0]

        self.assertEqual(settings.steam_user_id, player['steamid'])

    def test_get_player_owned_games_returns_json_dictionary(self):
        games =  self.client.get_player_owned_games()
        self.assertTrue(isinstance(games, list))
        self.assertTrue(isinstance(games[0], dict))
