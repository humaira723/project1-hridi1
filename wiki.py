# pylint: disable=line-too-long
import requests

def wiki_link(movie):
    """
    Function uses MediaWiki API to search for the first url in a list of lists regarding the movie title that is passed as an argument.
    """

    wiki_url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "opensearch",
        "search": movie,
        "namespace": "0",
        "limit": "5",
        "format": "json",
    }
    response = requests.get(
        wiki_url,
        params
    )

    data = response.json()
    first_url = data[3][0]
    return first_url
