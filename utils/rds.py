

from flask import Flask
app = Flask(__name__)


@app.route('/<path:urlpath>')
def entry(urlpath):
    return urlpath


if __name__ == '__main__':
    app.run()

