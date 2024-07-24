import os


class Config(object):
    API_HASH = os.environ.get("0b691c3e86603a7e34aae0b5927d725a")
    BOT_TOKEN = os.environ.get("7206189591:AAErETpVJ3qe5APSRzPbhyTouG9qer0fCYc")
    TELEGRAM_API = os.environ.get("25695562")
    OWNER = os.environ.get("1895952308")
    OWNER_USERNAME = os.environ.get("StupidBoi69")
    PASSWORD = os.environ.get("1qaz")
    DATABASE_URL = os.environ.get("mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")
    LOGCHANNEL = os.environ.get("-1001875723856")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]

    UPSTREAM_REPO = "https://github.com/nero-bc/MERGE-BOTi"
    UPSTREAM_BRANCH = "master"
