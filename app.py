import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def cat():
    resp = requests.get(url='https://randomfox.ca/floof/')
    return render_template('index.html', url=resp.json()['image'])


if __name__ == '__main__':
    app.run(port=5000)
