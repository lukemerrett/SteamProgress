__author__ = 'Luke Merrett'

import unittest
from analytics import playtime

class PlaytimeTests(unittest.TestCase):
    def test_get_total_playtime_for_last_two_weeks_returns_playtime(self):
        playtime_in_minutes = playtime.get_total_playtime_for_last_two_weeks()
        self.assertTrue(playtime_in_minutes > 0)

    def test_get_total_playtime_ever_returns_playtime(self):
        playtime_in_minutes = playtime.get_total_playtime_ever()
        self.assertTrue(playtime_in_minutes > 0)

    def test_choose_a_random_game_to_play_returns_a_game(self):
        game_to_play = playtime.choose_a_random_game_to_play(False, False)
        self.assertTrue(isinstance(game_to_play, str))
