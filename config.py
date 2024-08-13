import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 19863702))
API_HASH = getenv("API_HASH", "6d48cb362a97a43cfc944fd5c0f917f9")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7078801887:AAHfjN8PLgYX9OtWAUDvGyX5uFqWe210mT8")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 777777))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1001880981234))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6304277259))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/arindam69x/New-music-bot69",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Sprizen_Bots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Sprizen_Bot_Support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "df4340d7535741cf945b1848c20c2fd8")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "5bec438b8cb4495dac757db614c51494")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFQHkgAudbJQYekYFHA_vsESV2JuVbKx1r9_MNf7R_u3diI8iPoBuTgov0Kxj-3DgGSAZp9guzmd-tlURm64S21sNDExmKVdQxhkLNnTSiDadDBSrikb32d62DENgBcA9yyF53knp6tW_jUq2CoMElbUr42W5GXT2mfVvqVyq8_kxErb1-cpfx1MFjwqBFHaDH2TzovI997EsmBcZlgRgoyG44ah71E_zmVax4v4qKaVj3oRuH1e1FUQFGQFUCWeYhtcpwvZlf4wfXymKkMfwgBzFsYEiS2B-oNkW2dniWKSQqGvXjKVkk7ew_nQBo0UGXK9GT9iFPXAkjR8gIFZbLPgg1EMwAAAAGFwWJtAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph//file/260b71399f061c1f0d9fb.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph//file/2d576fcf982ff294b0d5a.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph//file/77ba78d195c2e26de2d32.jpg"
STATS_IMG_URL = "https://telegra.ph//file/e9abb075cdc98091fd73b.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph//file/a64b601cce0f45a192ce1.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph//file/37f24422832e727ebf478.jpg"
STREAM_IMG_URL = "https://telegra.ph//file/7c896988bd3d0b91b8e46.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph//file/1df85370be3f13663a2d9.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph//file/38124ca6dea236fb7e4ef.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph//file/adf5178b6e62a11b2c402.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph//file/9a258a9e3c9c3b6f61169.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph//file/b3b2e9a46166f3ee1a5cf.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
