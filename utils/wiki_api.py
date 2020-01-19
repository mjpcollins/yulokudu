
import wikipedia


def get_random_article():
    return wikipedia.random()


def information_from_article(article):
    """
    Extract useful information from the article and dump it in a dict

    :param article:
    :return:
    """

    try:
        c = wikipedia.page(article).categories
        # l = wikipedia.page(article).links
        u = wikipedia.page(article).url
        return {article: {'topic': article,
                          'categories': c,
                          # 'links': l,
                          'url': u}}
    except wikipedia.exceptions.PageError:
        return False


def article_url(article):
    base_url_text = "https://en.wikipedia.org/wiki/{article}"
    return base_url_text.format(article=article.replace(" ", "_"))


if __name__ == '__main__':
    r = get_random_article()
    print(r)



