from quart import Quart, redirect

from config import *
from oauth.client import DiscordOauth2Client

app = Quart(__name__)
app.secret_key = ""
app.config['CLIENT_ID'] = CLIENT_ID
app.config['CLIENT_SECRET'] = CLIENT_SECRET
app.config['SCOPES'] = ["identify", "guilds"]
app.config['REDIRECT_URI'] = REDIRECT_URI

client = DiscordOauth2Client(app)


@app.route("/")
async def index():
    return redirect("/login")  # redirect to login for ease


@app.route('/login/', methods=['GET'])
async def login():
    return redirect(client.authentication_url())  # redirect to authentication url formed by given client details


@app.route('/api')
async def api():
    return {"Hello": "World"}


@app.route('/callback', methods=['GET'])
async def callback():
    """Get client's details in accordance of provided scopes"""
    data = client.authenticate()
    return data


# async def create_db_pool():
#     conn = await asyncpg.connect(database="QuotientDB", user="postgres", password="588y5vwa")
#     print("--DB Connection Complete --")
#
# asyncio.get_event_loop().run_until_complete(create_db_pool())

app.run(debug=True, port=5000, host='localhost')
