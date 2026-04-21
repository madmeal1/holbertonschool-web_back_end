#!/usr/bin/env python3
"""Parametrize templates with Flask-Babel"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
babel = Babel()


def get_locale() -> str:
    """Determine the best match locale from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", methods=['GET'], strict_slashes=False)
def index() -> str:
    """Render the index page

       Return render
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
