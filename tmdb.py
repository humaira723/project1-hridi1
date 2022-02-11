import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/movie/"
IMG_URL = "https://api.themoviedb.org/3/configuration"

#for id in movies_id:
#    BASE_URL = "https://api.themoviedb.org/3/movie/"+str(id)

def movie_info(id):
    """
    function yada yada
    """
    query_params = {
        "api_key": os.getenv("API_KEY"),
        "movie_id": id,
    }

    response = requests.get(
        BASE_URL+str(id),
        params=query_params
    )
   
    data = response.json()
    try:
        title = data["title"]
        tagline = data["tagline"]
        genres = ", ".join([sub["name"] for sub in data["genres"]])
        image = "https://image.tmdb.org/t/p/w500"+data["poster_path"]
        return (title,tagline,genres,image)
    except KeyError:
        title = "Hereditary"
        tagline = "Every family tree hides a secret."
        genres = "Horror, Mystery, Thriller"
        image = "https://image.tmdb.org/t/p/w500/lHV8HHlhwNup2VbpiACtlKzaGIQ.jpg"
        return (title,tagline,genres,image)
