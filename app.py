# pylint: disable=line-too-long
import random
import flask
from tmdb import movie_info
from wiki import wiki_link

app = flask.Flask(__name__)
movies_id = [493922,76341,7326,4348,10315,22538,9428,502033,152601,16869,270303,254320,8363,19913,68718,242224,84892,49020,44214,773,1443,694,274,11545,565310,24,546554,371645,4538,116745,313369,210577,37165]


@app.route("/")
def index():
    """
    idk
    """
    title, tagline, genres, image = movie_info(random.choice(movies_id))

    wiki_link(title)

    return flask.render_template(
        "index.html",
        movie_info = movie_info,
        title = title,
        tagline = tagline,
        genres = genres,
        image = image,

        wiki_link = wiki_link,
    )
app.run(debug=True)
