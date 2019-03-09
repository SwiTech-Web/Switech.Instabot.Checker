import sqlite3

from plugins.config import CONFIGURATION


class SqliteConnection:
    def __init__(self, filename):
        sqlite_connection = sqlite3.connect(CONFIGURATION.config['Target'] + filename)
        self.connection = sqlite_connection

    def commit_change(self):
        self.connection.commit()
        return

    def get_all_rows(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM following WHERE archived != 1")
        result = cursor.fetchall()
        cursor.close()
        return result

    def update_row_by_id(self, username):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE following SET archived = 1 WHERE username = \"{}\" ".format(username))
        self.commit_change()
        return

    def close_connection(self):
        self.connection.close()
        return
