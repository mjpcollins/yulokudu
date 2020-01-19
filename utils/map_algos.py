
from utils.t import load_json

import networkx as nx


class UserMap:

    def __init__(self, user_id):
        self.user_id = user_id
        self.G = nx.Graph()
        # self.user_map_reference = # TODO: Redis key?

    def __str__(self):
        return f"An article map for {self.user_id} with {self.nodes} node(s)"

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

    def discover_neighbourhood(self, node):
        """
        Take a node and discover articles that art < 3 links away

        Calculate the weighted distance to those articles

        Penalty for being further away.
        :param node:
        :return:
        """

        print(node)
        first_neighbours = [nod for nod in self.G.neighbors(node)]
        for neighbour in first_neighbours:

            print("----", neighbour, self.G[node][neighbour])
            for n in self.G.neighbors(neighbour):
                if (n != node) and (n not in first_neighbours):
                    print("----", "----", n, self.G[neighbour][n])

        # c = nx.algorithms.resistance_distance(self.G, node, 4)
        # for ch in c:
        #     print(ch)

        closest = {ns: self.G[node][ns]['weight'] for ns in self.G.neighbors(node)}

        return closest

    def recommend_article(self, current_article_url=None, current_article_name=None, jump_distance=0.5):

        # Load infomation from file
        ns = load_json("./training_info/nodes.json")['content']
        urls = load_json("./training_info/urls.json")['content']

        # Find node from input
        node_idx = False
        if current_article_name:
            try:
                node_idx = ns.index(current_article_name)
            except IndexError:
                raise IndexError("Article not in the Graph!")
        elif current_article_url:
            url_idx = urls.index(current_article_url)
            for n in self.G.nodes:
                if int(self.G.nodes[n]['url']) == int(url_idx):
                    node_idx = int(n)
            if not node_idx:
                raise IndexError("URL not in the Graph!")
        else:
            raise ValueError("No information on the current article given!")

        # Find next node

        neighs = self.discover_neighbourhood(node_idx)

        closest = max(neighs, key=neighs.get)

        n = self.G.nodes[closest]

        return urls[n['url']]


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

