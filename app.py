import flask
import random
from tmdb import movieInfo

app = flask.Flask(__name__)
movies_id = [493922,76341,7326,4348,10315,22538,9428,502033,152601,16869,270303,254320,8363,19913,68718,242224,84892,49020,44214,773,1443,694,274,11545,565310,24,546554,371645,4538,116745,313369,210577,37165]


@app.route("/")
def index():
    #wikiLink(title)
    title, tagline, genres, image = movieInfo(random.choice(movies_id))
    return flask.render_template(
        "index.html",
        movieInfo = movieInfo,
        title = title,
        tagline = tagline,
        genres = genres,
        image = image,

    )

app.run(debug=True)