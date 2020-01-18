
from utils.wiki_api import get_random_article
import networkx as nx


class UserMap:

    def __init__(self, user_id):
        self.user_id = user_id
        self.nodes = 0
        self.G = nx.Graph()
        # self.user_map_reference = # TODO: Redis key?

    def __str__(self):
        return f"An article map for {self.user_id} with {self.nodes} node(s)"

    def update_map(self, article_information):
        # Receive a new node

        # Identify links to other nodes

        # add to node map
        pass

    def recommend_article(self, current_article):

        return get_random_article()


class GlobalMap:

    pass


def network_investigation():

    G = nx.Graph()

    n = {"united_kingdom": {"topic": "united_kingdom",
         "url": "http://wikipedia.org/united_kingdom",
         "categories": ["countries"]},
        "united_states_of_america": {"topic": "united_states_of_america",
         "url": "http://wikipedia.org/united_states_of_america",
         "categories": ["countries"]}}

    for node in n:
        G.add_node(node, **n[node])

    print(G.nodes['united_kingdom'])


if __name__ == '__main__':
    network_investigation()

