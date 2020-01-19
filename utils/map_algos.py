
from utils.t import load_json

import networkx as nx


class UserMap:

    def __init__(self, user_id):
        self.user_id = user_id
        self.G = nx.Graph()
        self.current_node = None
        self.ns = load_json("./training_info/nodes.json")['content']
        self.urls = load_json("./training_info/urls.json")['content']

        # self.user_map_reference = # TODO: Redis key?

    def __str__(self):
        return "An article map for {uid} with {n} node(s)".format(uid=self.user_id, n=self.nodes)

    def get_nodes(self):
        return self.G.nodes

    def update_map(self, article_information):
        # Receive a new node
        # Not an ideal way to do this...

        # Add nodes to the graph
        for n1 in article_information:
            if n1 not in self.G.nodes:
                self.G.add_node(node_for_adding=n1, **article_information[n1])

                # Loop through added node and increase the weight of the links added
                for k in self.G.nodes[n1]['keywords']:
                    for n2 in self.G.nodes:
                        if n1 != n2:
                            if k in self.G.nodes[n2]['keywords']:
                                if self.G.has_edge(n1, n2):
                                    w = self.G[n1][n2]['weight']
                                    self.G.remove_edge(n1, n2)
                                    self.G.add_edge(n1, n2, weight=w+1)
                                else:
                                    self.G.add_edge(n1, n2, weight=1)

    def discover_neighbourhood(self):
        """
        Take a node and discover articles that are nearby, and the weights to them

        :param node:
        :return:
        """

        return {e[1]: self.G[e[0]][e[1]]['weight'] for e in self.G.edges(self.current_node)}

    def explore_neighbourhood(self):
        nodes_weights = self.discover_neighbourhood()

    def recommend_article(self, current_article_url=None, current_article_name=None, jump_distance=0.5):

        # Find node from input
        if current_article_name:
            try:
                self.current_node = self.ns.index(current_article_name)
            except IndexError:
                raise IndexError("Article not in the Graph!")
        elif current_article_url:
            url_idx = self.urls.index(current_article_url)
            for n in self.G.nodes:
                if int(self.G.nodes[n]['url']) == int(url_idx):
                    self.current_node = int(n)
            if not self.current_node:
                raise IndexError("URL not in the Graph!")
        else:
            raise ValueError("No information on the current article given!")

        # Find next closest node
        neighs = self.discover_neighbourhood()
        closest = max(neighs, key=neighs.get)
        n = self.G.nodes[closest]

        return self.urls[n['url']]


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

