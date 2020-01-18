from flask import Flask, request

from utils.map_algos import UserMap

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def parse_request():

    current_article = request.args['start_url']

    # TODO: Include user ID in final product
    user_id = "jeff100"

    u = UserMap(user_id)
    u.update_map(current_article)
    next_article = u.recommend_article(current_article)

    return_article = {'next_url': next_article}

    return return_article


if __name__ == '__main__':
    app.run()

