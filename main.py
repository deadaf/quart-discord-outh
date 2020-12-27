from oauth.client import DiscordOauth2Client
from quart import Quart, redirect, request, render_template
from config import *

app = Quart(__name__)
app.secret_key = quart_secret

client = DiscordOauth2Client(app)


@app.route("/")
async def index():
    return "Hello World"


@app.route('/login/', methods=['GET'])
async def login():
    return redirect(oauth_url)


@app.route('/api')
async def api():
    return ({"Hello": "World"})


@app.route('/callback', methods=['GET'])
async def callback():
    code = request.args.get('code')
    access_token = await client.get_access_token(code)
    guilds = await client.fetch_guilds(access_token)
    # return render_template("guilds.html", glist=guilds)
    return str(guilds)


app.run(debug=True, port=5000, host='localhost')
