__author__ = 'Luke Merrett'

import settings
import unittest
from builders import urlbuilder

class TestUrlBuilder(unittest.TestCase):
    def test_get_player_summary_returns_url(self):
        url = urlbuilder.get_player_summary()

        self.assertTrue(settings.steam_api_url in url)
        self.assertTrue('ISteamUser' in url)
        self.assertTrue('GetPlayerSummaries' in url)
        self.assertTrue('v0002' in url)
        self.assertTrue('key' in url)
        self.assertTrue(settings.steam_webapi_key in url)
        self.assertTrue('steamids' in url)
        self.assertTrue(settings.steam_user_id in url)

    def test_get_player_owned_games_returns_url(self):
        url = urlbuilder.get_player_owned_games()

        self.assertTrue(settings.steam_api_url in url)
        self.assertTrue('IPlayerService' in url)
        self.assertTrue('GetOwnedGames' in url)
        self.assertTrue('v0001' in url)
        self.assertTrue('key' in url)
        self.assertTrue(settings.steam_webapi_key in url)
        self.assertTrue('steamid' in url)
        self.assertTrue(settings.steam_user_id in url)
        self.assertTrue('include_appinfo' in url)
        self.assertTrue('include_played_free_games' in url)
