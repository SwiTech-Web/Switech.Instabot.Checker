import datetime

from plugins.sqlite_connection import SqliteConnection


def check_if_in_database(filename, followers):
    sqlite_connection = SqliteConnection(filename)
    rows = sqlite_connection.get_all_rows()
    for row in rows:
        print(row[0])
        if row[0] in followers:
            elapsed_time = (datetime.datetime.now() - row[2]).total_seconds()
            if elapsed_time >= 172800:
                sqlite_connection.update_row_by_id(row[0])
    sqlite_connection.close_connection()
    return
