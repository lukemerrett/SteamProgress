__author__ = 'Luke Merrett'

from database.playtime_operations import PlaytimeOperations

if __name__ == '__main__':
    s = PlaytimeOperations()

    s.get_and_store_playtime()
    s.print_all_stored_playtime()
