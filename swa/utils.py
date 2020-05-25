from os import getenv

import bottle
import redis

cookie_secret = str(getenv("SPOTIPY_CLIENT_SECRET"))


def redis_client() -> redis.Redis:
    c = redis.Redis(
        password='yetsle97',
        decode_responses=True
    )
    # Test connection
    c.ping()
    return c


def redis_session_data_key(sid: str) -> str:
    return 'swa-session-data-{}'.format(sid)


def http_server_info() -> tuple:
    return getenv("SERVER_HOST", '127.0.1.1'), getenv("SERVER_PORT", '8080')


# def cookie_get_username() -> str or None:
#     cookie = bottle.request.get_cookie('swa_data', secret=cookie_secret)
#     if cookie and 'user' in cookie:
#         return cookie['user']
#
#     return None