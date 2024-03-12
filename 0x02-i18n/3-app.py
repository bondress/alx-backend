#!/usr/bin/env python3
"""3-app.py"""
from typing import Union
from flask import Flask, request
from flask_babel import Babel
from routes.routes_3 import app_routes
from config import Config

a
app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
app.register_blueprint(app_routes)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Get locale"""
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
