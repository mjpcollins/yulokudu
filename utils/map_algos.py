
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
                                    w = (1 / self.G[n1][n2]['weight']) + 1
                                    self.G.remove_edge(n1, n2)
                                    self.G.add_edge(n1, n2, weight=1/w)
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
        # Very computationally heavy - replace with better algo when in product
        opts = list()
        for n in self.G.nodes:
            if (self.current_node != n) and (nx.has_path(self.G, self.current_node, n)):
                p = min(path for path in nx.all_simple_paths(self.G, self.current_node, n))
            elif self.current_node != n:
                continue
            else:
                p = []
            d = {"node": int(n),
                 "distance": -1}
            for idx in range(len(p)):
                if idx < (len(p) - 1):
                    d["distance"] = d["distance"] + self.G[p[idx]][p[idx + 1]]["weight"]

            # Arbitrary large number
            if d["distance"] == -1:
                d["distance"] = 200

            opts.append(d)

        opts.sort(key=lambda k: k['distance'])

        return opts

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

        # Think about paths around the network
        neighbourhood = self.explore_neighbourhood()

        jump_to_node = int(len(neighbourhood) * jump_distance)
        if jump_to_node >= len(neighbourhood):
            nd = neighbourhood[jump_to_node - 1]["node"]
        else:
            nd = neighbourhood[jump_to_node]["node"]

        n = self.G.nodes[nd]

        return self.urls[n['url']]

    def draw(self):
        nx.draw_networkx(self.G)


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

