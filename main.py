import os

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    random_gif_link = get_random_gif_link()
    return render_template('index.html', image_file=random_gif_link)


def get_random_gif_link():
    token = os.environ.get('GIF_TOKEN')
    response = requests.get(
        f"https://api.giphy.com/v1/gifs/random?api_key={token}&rating=g",
        headers={"Content-Type": "text/html"}
    )
    return response.json()['data']['images']['original']['webp']


if __name__ == '__main__':
    app.run()
