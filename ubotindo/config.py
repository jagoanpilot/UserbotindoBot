if not __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    sys.exit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1431311619:AAGjF3q4VEy1ZjgRvy13afk2b4qfcCIFA8s"
    OWNER_ID = (
        "1123523488"  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = ""
    TELETHON_HASH = None  # for purge stuffs
    TELETHON_ID = None

    # RECOMMENDED
    # needed for any database modules
    SQLALCHEMY_DATABASE_URI = "postgres://fnkgdyhncytxki:ff57ae77890b4b3bafe9b02a122c7230a5b4f7ade7c18cf38aae2b0ebec08b28@ec2-34-196-34-158.compute-1.amazonaws.com:5432/df9m916pkqq5pf"
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    GBAN_LOGS = @logbannespublic
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    # List of id's (not usernames) for users which have access to dev's
    # command.
    DEV_USERS = ([820833737 1053257628 1067860255 1388215352 1374967983 1332799713])
    # List of id's (not usernames) for users which have sudo access to the bot.
    SUDO_USERS = ([820833737 1053257628 1067860255 1388215352 1374967983 1332799713])
    # List of id's (not usernames) for users which are allowed to gban, but
    # can also be banned.
    SUPPORT_USERS = ([820833737 1053257628 1067860255 1388215352 1374967983 1332799713])
    # List of id's (not usernames) for users which WONT be banned/kicked by
    # the bot.
    WHITELIST_USERS = ([])
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with
    # more custom handler!
    CUSTOM_CMD = False
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = None  # Your SpamWatch token
    WALL_API = None
    LASTFM_API_KEY = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
