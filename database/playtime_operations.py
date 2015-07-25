__author__ = 'Luke Merrett'

import settings
import datetime
import pygal
import webbrowser
from peewee import *
from clients.steamapi import SteamApiClient
from collections import defaultdict, OrderedDict

db = SqliteDatabase(settings.sqlite_database_name, threadlocals=True)

class BaseModel(Model):
    class Meta:
        database = db

class PlaytimeInLast2Weeks(BaseModel):
    """
    Table holding details on games and their playtime over the last 2 weeks
    """
    game_name = TextField()
    playtime_in_minutes = IntegerField()
    date_captured = DateField(default=datetime.date.today())

class PlaytimeOperations:
    """
    Gets all the playtime for the last 2 weeks and stores it in Sqlite
    """
    def __init__(self):
        db.connect()
        db.create_table(PlaytimeInLast2Weeks, True)

    def get_and_store_playtime(self):
        records_for_today = PlaytimeInLast2Weeks.select().where(
            PlaytimeInLast2Weeks.date_captured == datetime.date.today()
        )

        if records_for_today.count() > 0:
            print('Playtime already captured for today, cancelling save operation')
            return

        games = SteamApiClient().get_player_owned_games()
        games_played = []

        for game in games:
            if 'playtime_2weeks' in game:
                games_played.append(game)

        for game in games_played:
            print('Saving playtime for ' + game['name'])
            record = PlaytimeInLast2Weeks.create(game_name=game['name'], playtime_in_minutes=game['playtime_2weeks'])
            record.save()

    def print_all_stored_playtime(self):
        playtime = PlaytimeInLast2Weeks.select().order_by(PlaytimeInLast2Weeks.date_captured.desc())

        print('\nGame, Date Captured, Playtime in minutes')
        print('----------------------------------------')
        for time in playtime:
            output = ', '.join([time.game_name, str(time.date_captured), str(time.playtime_in_minutes)])
            print(output)

    def chart_stored_playtime(self):
        playtime = PlaytimeInLast2Weeks.select().order_by(PlaytimeInLast2Weeks.date_captured.desc())

        bar_chart = pygal.Bar(title="Playtime over the last 2 weeks by date captured")

        # Group by date captured
        time_by_date_captured = defaultdict(list)
        for time in playtime:
            if not str(time.date_captured) in time_by_date_captured.keys():
                time_by_date_captured[str(time.date_captured)] = time.playtime_in_minutes
            else:
                time_by_date_captured[str(time.date_captured)] += time.playtime_in_minutes

        time_by_date_captured = OrderedDict(sorted(time_by_date_captured.items(), key=lambda t: t[0]))

        bar_chart.x_labels = time_by_date_captured.keys()

        bar_chart.add("Playtime", time_by_date_captured.values())

        bar_chart.render_to_file(settings.target_chart_export_filename)

        webbrowser.open_new(settings.target_chart_export_filename)
