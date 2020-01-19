from flask import Flask, request, jsonify

from utils.map_algos import UserMap
from utils.t import load_json, format_mapping_dicts

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def parse_request():

    # TODO: Place inside a function
    print("Request received: {r}".format(r=request))
    current_article = dict(request.args)
    print("Pre process current_article: {c}".format(c=current_article))
    if "jumpdist" not in current_article:
        current_article["jumpdist"] = [0.5]
    # Standardise format
    for k in current_article:
        if isinstance(current_article[k], str):
            current_article[k] = [current_article[k]]

    print("Post process current_article: {c}".format(c=current_article))

    # TODO: Include user ID in final product
    user_id = "jeff100"

    # TODO: Place inside function
    u = UserMap(user_id)
    u.update_map(format_mapping_dicts(nodes=load_json("./training_info/info.json")))
    next_article = u.recommend_article(current_article_url=current_article['start_url'][0],
                                       jump_distance=float(current_article['jumpdist'][0]))
    return_article = {'next_url': next_article}

    response = jsonify(return_article)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

