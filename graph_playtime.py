__author__ = 'Luke Merrett'

from database.playtime_operations import PlaytimeOperations

if __name__ == '__main__':
    s = PlaytimeOperations()

    s.chart_stored_playtime()
