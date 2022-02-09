import flask
from tmdb import movieInfo

app = flask.Flask(__name__)

@app.route("/")
def index():
    title, tagline, genres = movieInfo(),
    return flask.render_template(
        "index.html",
        movieInfo = movieInfo,
        title = title,
        tagline = tagline,
        #genres = genres,
    )

app.run(debug=True)