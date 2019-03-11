import os
import sys
import plugins.bot as bot
import plugins.db_sqlite as database

from plugins.PyLogger import pylogger


os.chdir(os.path.dirname(os.path.realpath(__file__)))


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    instabot = bot.InstagramBotChecker(username, password)
    instabot.login()
    followers = instabot.check_followers()
    filename = '{}.sqlite'.format(username)
    database.check_if_in_database(filename, followers)


if __name__ == '__main__':
    main()
