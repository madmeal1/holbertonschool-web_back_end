#!/usr/bin/env python3
"""Infer appropriate time zone"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale() -> str:
    """Determine locale by priority: URL, user settings, header, default"""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone() -> str:
    """Determine timezone by priority: URL, user settings, default UTC"""
    timezone = request.args.get("timezone")
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and g.user.get("timezone"):
        try:
            pytz.timezone(g.user["timezone"])
            return g.user["timezone"]
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return "UTC"


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


def get_user() -> dict:
    """Return a user dictionary or None if not found"""
    login_as = request.args.get("login_as")
    if login_as is None:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request() -> None:
    """Execute before all other functions and set global user"""
    g.user = get_user()


@app.route("/", methods=['GET'], strict_slashes=False)
def index() -> str:
    """Render the index page"""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
