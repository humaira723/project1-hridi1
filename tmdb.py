import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


BASE_URL = "https://api.themoviedb.org/3/movie/493922"
#BASE_URL = "https://api.themoviedb.org/3/movie/{movie_id}"

movies_id = [493922,76341,7326,4348]
#for id in movies_id:
#    BASE_URL = "https://api.themoviedb.org/3/movie/"+str(id)
def movieInfo():
    query_params = {
        "api_key": os.getenv("API_KEY"),
    }

    response = requests.get(
        BASE_URL,
        params=query_params
    )

    data = response.json()

    title = data["title"]
    tagline = data["tagline"]
    #genres = [sub["name"] for sub in data["genres"]]
    return (title,tagline)
    #print(title,"-",tagline,"\n",genres)

#movies = response.json()
#for movie in movies_id:
    #print(response.json()[movie]["original_title"])
#for id in movies_id:
#print(response.json()["original_title"])

