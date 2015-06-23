__author__ = 'Luke Merrett'

import json
from urllib import request
from builders import urlbuilder

class SteamApiClient:
    def get_player_summary(self):
        return self.__get_json_from_url(urlbuilder.get_player_summary())
        pass

    def get_player_owned_games(self):
        return self.__get_json_from_url(urlbuilder.get_player_owned_games())

    @staticmethod
    def __get_json_from_url(url):
        data = request.urlopen(url)
        return json.loads(data.readall().decode('utf-8'))