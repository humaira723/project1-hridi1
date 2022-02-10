import requests

from tmdb import movieInfo


WIKI_URL = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=info&inprop=url%7Ctalkid"


def wikiLink(): #set movie title arg

    PARAMS = {
        "action": "query",
        "titles": "Albert Einstein",
        "format": "json",
        "prop": "info",
        "inprop": "url|talkid",
    }
    response = requests.get(
        WIKI_URL= WIKI_URL, 
        params=PARAMS
    )

    data = response.json()

    pages = data["query"]["pages"][0]["fullurl"]
    print(pages)
   # for k, v in pages.items():
    #    for l in v["links"]:
     #       print(l["title"])

    #link = data["links"]

wikiLink()
