import requests

from tmdb import movieInfo

S = requests.Session()
WIKI_URL = "https://en.wikipedia.org/w/api.php"


def wikiLink(): #set movie title arg

    PARAMS = {
        "action": "query",
        "titles": title,
        "format": "json",
        "prop": "links"
    }
    R = S.get(
        WIKI_URL= WIKI_URL, 
        params=PARAMS
    )

    data = response.json()

    pages = data["query"]["pages"]

    print(pages)
   # for k, v in pages.items():
    #    for l in v["links"]:
     #       print(l["title"])

    #link = data["links"]

wikiLink()
