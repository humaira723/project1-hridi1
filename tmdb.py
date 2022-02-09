import requests
import os
import random
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/movie/" 
IMG_URL = "https://api.themoviedb.org/3/configuration"

#for id in movies_id:
#    BASE_URL = "https://api.themoviedb.org/3/movie/"+str(id)
def movieInfo(id):
    query_params = {
        "api_key": os.getenv("API_KEY"),
        "movie_id": id,
    }

    response = requests.get(
        BASE_URL+str(id),
        params=query_params
    )

    data = response.json()

    title = data["title"]
    tagline = data["tagline"]
    genresList = [sub["name"] for sub in data["genres"]]
    genres = ", ".join(genresList)
    image = "https://image.tmdb.org/t/p/w500"+data["poster_path"]

    return (title,tagline,genres,image)

#print(movieInfo(493922))
#movies = response.json()
#for movie in movies_id:
    #print(response.json()[movie]["original_title"])
#for id in movies_id:
#print(response.json()["original_title"])

