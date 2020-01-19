from flask import Flask, request, jsonify
import json

from utils.map_algos import UserMap
from utils.t import load_json, format_mapping_dicts

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def parse_request():

    print(request)

    current_article = dict(request.form)
    print("form", current_article)

    current_article = dict(request.args)
    print("args", current_article)

    current_article = dict(request.values)
    print("values", current_article)

    current_article = dict(request.data)
    print("data", current_article)

    if "jumpdist" not in current_article:
        current_article["jumpdist"] = 0.5

    # TODO: Include user ID in final product
    user_id = "jeff100"

    u = UserMap(user_id)

    u.update_map(format_mapping_dicts(nodes=load_json("./training_info/info.json")))

    next_article = u.recommend_article(current_article_url=current_article['start_url'],
                                       jump_distance=current_article['jumpdist'])

    return_article = {'next_url': next_article}

    return return_article


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

