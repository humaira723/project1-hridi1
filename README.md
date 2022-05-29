# project1-hridi1
## Heroku Link
https://polar-plains-32700.herokuapp.com/
## Technologies
Using VSCode as my IDE, I created a directory in the terminal that would hold all my files. In order to install all my libraries, I began with installing pip using the command `sudo apt install python3-pip`.

To make sure my code is readable and free of semantic errors, I installed the linter pylint using the command `pip install pylint`. After analyzing all my code, I had to disable the following pylint errors: `line-too-long` and `invalid-envvar-default`.

Next, I installed flask using `pip install flask`. Flask is a web framework that works with Python to make web development less complicated. My flask app file in this repository is named “app.py”. I used the most libraries in my flask app file. Firstly, I imported the flask library. I imported the libraries `movie_info` and `wiki_link` from my api files in order to display information on the web browser. The function `random` was used to call a random element from a list of movie ids in the `movie_info()` function.

Python-dotenv was installed, as well. To import the main functions I used `from dotenv import find_dotenv, load_dotenv`. This can be seen in the tmdb.py file. Using this library I put information I do not want to be visible in a .env file, then used .gitignore to hide that file. I used the os library to access the environment variable in the .env file.

Requests was installed with `pip install requests`. This is to get parameters needed from my API, which I accomplished by calling `requests.get()` on the base url and parameters.

Heroku was installed with the command `sudo curl https://cli-assets.heroku.com/install.sh | sh` (for WSL users). Heroku is a free deployment service that works well with Git. After creating an app, you can push your code to its repository. In return, you receive a URL that contains your deployed app.
