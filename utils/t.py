
import json


def format_mapping_dicts(nodes):
    """
    Convert text nodes to integer mappings

    :param nodes:
    :return:
    """

    json_key = 'content'
    output_nodes = load_json("./training_info/nodes.json")[json_key]
    output_keywords = load_json("./training_info/keywords.json")[json_key]
    output_urls = load_json("./training_info/urls.json")[json_key]
    output_full_node_info = dict()

    for node in nodes:
        url = nodes[node]['url'].replace(" ", "")

        if node not in output_nodes:
            output_nodes.append(node)

        for keyword in nodes[node]['keywords']:
            k = keyword.lower().replace(" ", "")
            if k not in output_keywords:
                output_keywords.append(k)

        if url not in output_urls:
            output_urls.append(url)

        node_information_dict = {
            output_nodes.index(node): {
                    "url": output_urls.index(url),
                    "keywords": [output_keywords.index(keyword.lower().replace(" ", ""))
                                 for keyword in nodes[node]['keywords']]}
        }

        output_full_node_info.update(node_information_dict)

    save_json(path="./training_info/nodes.json", j={json_key: output_nodes})
    save_json(path="./training_info/keywords.json", j={json_key: output_keywords})
    save_json(path="./training_info/urls.json", j={json_key: output_urls})

    return output_full_node_info


def load_json(path):
    """


    :param path:
    :return:
    """

    with open(path, 'r') as F:
        j = json.load(F)
    return j


def save_json(path, j):
    with open(path, 'w') as F:
        F.write(json.dumps(j))


def run():
    nodes = load_json("./training_info/info.json")
    short_nodes = format_mapping_dicts(nodes=nodes)
    print(short_nodes)


if __name__ == '__main__':
    run()
