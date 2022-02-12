# pylint: disable=line-too-long
import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/movie/"
IMG_URL = "https://api.themoviedb.org/3/configuration"

def movie_info(movie_id):
    """
    Function uses TMDB api and requests library to retrieve title, tagline, genres, and an image for movie according to movie_id. If KeyError occurs default values for movie "Hereditary" is set to all variables.
    """
    query_params = {
        "api_key": os.getenv("API_KEY"),
        "movie_id": movie_id,
    }

    response = requests.get(
        BASE_URL+str(movie_id),
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
