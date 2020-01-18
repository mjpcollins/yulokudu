
import wikipedia


def get_random_article():
    base_url_text = "https://en.wikipedia.org/wiki/{article}"
    article = wikipedia.random()
    return base_url_text.format(article=article.replace(" ", "_"))


if __name__ == '__main__':
    r = get_random_article()
    print(r)



