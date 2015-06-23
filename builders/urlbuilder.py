__author__ = 'Luke Merrett'

import settings

valid_interfaces = {
    'ISteamUser': [
        'GetPlayerSummaries'
    ],
    'IPlayerService': [
        'GetOwnedGames'
    ]
}

def get_player_summary():
    return __get_url('ISteamUser', 'GetPlayerSummaries', 'v0002', {
        'steamids': settings.steam_user_id
    })

def get_player_owned_games():
    return __get_url('IPlayerService', 'GetOwnedGames', 'v0001', {
        'steamid': settings.steam_user_id,
        'include_appinfo':'1',
        'include_played_free_games':'1'
    })

def __get_url(interfaceName, methodName, version, parameters):
    if interfaceName not in valid_interfaces:
        raise Exception('The interfaceName provided is not supported')

    valid_methods = valid_interfaces[interfaceName]

    if methodName not in valid_methods:
        raise Exception('The methodName provided is not supported for this interfaceName')

    if not isinstance(parameters, dict):
        raise Exception('parameters must be a dictionary')

    url = settings.steam_api_url + interfaceName + '/' + methodName + '/' + version
    url += '?key=' + settings.steam_webapi_key + '&format=' + settings.response_format

    for key, value in parameters.items():
        url += '&' + key + '=' + value

    return url