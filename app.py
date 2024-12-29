# Taken from https://github.com/cabreraalex/svelte-flask-example/blob/master/server.py
# And tweaked/updated for https://www.reddit.com/r/learnpython/comments/17y2r8p/best_frontend_framework_for_an_intermediate/

from flask import Flask, send_from_directory
import random
app = Flask(__name__)

# << CHANGE THIS TO WHATEVER YOUR FRONTEND APP IS CALLED >>
FRONTEND_APP = 'ui'

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory(f'{FRONTEND_APP}/dist', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory(f'{FRONTEND_APP}/dist', path)


@app.route("/hello")
def hello():
    return f"{random.randint(1, 100)} Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
