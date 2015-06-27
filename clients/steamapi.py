__author__ = 'Luke Merrett'

import json
from urllib import request
from builders import urlbuilder

class SteamApiClient:
    def get_player_summary(self):
        return self.__get_json_from_url(urlbuilder.get_player_summary())

    def get_player_owned_games(self):
        response = self.__get_json_from_url(urlbuilder.get_player_owned_games())
        return response['response']['games']

    @staticmethod
    def __get_json_from_url(url):
        data = request.urlopen(url)
        return json.loads(data.readall().decode('utf-8'))
