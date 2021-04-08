import urllib.parse

import requests
from quart import request

from oauth.base import DISCORD_API_BASE_URL


class DiscordOauth2Client(object):
    def __init__(self, app):
        self.client_id = app.config['CLIENT_ID']
        self.client_secret = app.config['CLIENT_SECRET']
        self.scopes = app.config['SCOPES']
        self.redirect_url = app.config['REDIRECT_URI']

    """Forming authentication URL and returning it"""
    def authentication_url(self):
        return f"https://discord.com/api/oauth2/authorize?response_type=code&redirect_uri={urllib.parse.quote_plus(self.redirect_url)}&client_id={self.client_id}&scope={'%20'.join(self.scopes)}"

    """This is the main authentication function that uses response code and request client's details"""
    def authenticate(self):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': request.args.get("code"),
            'redirect_uri': self.redirect_url,
            'scope': self.scopes or ["identify", "guilds"]
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post('https://discord.com/api/v6/oauth2/token',
                          data=data, headers=headers)
        r.raise_for_status()
        json_ = r.json()
        return json_

    # @staticmethod
    # async def get_access_token(code):
    #     data = {
    #         'client_id': CLIENT_ID,
    #         'client_secret': CLIENT_SECRET,
    #         'grant_type': 'authorization_code',
    #         'code': code,
    #         'redirect_uri': REDIRECT_URI,
    #         'scope': 'identify guilds guilds.join email'
    #     }
    #     headers = {
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     r = requests.post('https://discord.com/api/v6/oauth2/token',
    #                       data=data, headers=headers)
    #     r.raise_for_status()
    #     json_ = r.json()
    #     return json_.get("access_token")

    @staticmethod
    async def fetch_guilds(token):
        url = DISCORD_API_BASE_URL + "/users/@me/guilds"
        headers = {
            "Authorization": "Bearer {}".format(token)
        }
        data = requests.get(url, headers=headers).json()
        return data

