from quart import redirect
from models import exceptions, guild
from config import *
import requests


API_ENDPOINT = "https://discord.com/api/v6"


class DiscordOauth2Client(object):
    def __init__(self, app):
        self.client_id = client_id

    @staticmethod
    async def get_access_token(code):
        data = {
            'client_id': client_id,
            'client_secret': client_Secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'scope': 'identify guilds guilds.join email'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post('https://discord.com/api/v6/oauth2/token',
                          data=data, headers=headers)
        r.raise_for_status()
        json_ = r.json()
        return json_.get("access_token")

    @staticmethod
    async def fetch_guilds(token):
        url = API_ENDPOINT + "/users/@me/guilds"
        headers = {
            "Authorization": "Bearer {}".format(token)
        }
        data = requests.get(url, headers=headers).json()

        return data
