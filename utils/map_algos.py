
from utils.wiki_api import get_random_article


class UserMap:

    def __init__(self, user_id):
        self.user_id = user_id
        self.nodes = 0
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
