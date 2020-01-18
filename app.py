from flask import Flask
app = Flask(__name__)


@app.route('/<path:urlpath>')
def entry(urlpath):
    print(urlpath)
    return str(urlpath)


if __name__ == '__main__':
    app.run()

