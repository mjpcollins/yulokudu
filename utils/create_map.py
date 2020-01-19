from utils.map_algos import UserMap
from utils.t import load_json, format_mapping_dicts
import matplotlib.pyplot as plt


def init_map(user_id, init_articles, show_graph=True):
    u = UserMap(user_id)

    u.update_map(init_articles)

    url = "https://www.msn.com/en-us/autos/news/tesla-selling-broken-glass-cybertruck-t-shirts-because-of-course-it-is/ar-BBYWJBI"
    a = "article2"

    if show_graph:
        u.draw()
        plt.show()

    d = u.recommend_article(current_article_url=url)

    print(d)


if __name__ == '__main__':
    nodes = load_json("./training_info/info.json")
    init_map(user_id="jeff5000",
             init_articles=format_mapping_dicts(nodes=nodes))

