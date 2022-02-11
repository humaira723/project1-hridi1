import requests

def wiki_link(movie):
    """
    fdj
    """

    WIKI_URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "opensearch",
        "search": movie,
        "namespace": "0",
        "limit": "5",
        "format": "json",
    }
    response = requests.get(
        WIKI_URL,
        PARAMS
    )

    data = response.json()
    first_url = data[3][0]
    return first_url

#print(wikiLink("Hereditary"))
