import os
import click
from flask.cli import AppGroup
from flask_migrate import Migrate
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


db.init_app(app)
migrate.init_app(app, db)


# group command
@click.group('user')
def user_cli_group():
    pass


@click.group('secure')
def secure_cli_group():
    pass


# add group
app.cli.add_command(user_cli_group)
app.cli.add_command(secure_cli_group)

__import__("entities")
__import__("application")


@app.route("/")
def index():
    return "py-ludo version 1.0"

if __name__ == "__main__":
    if Config.FLASK_ENV != "production":
        app.run(debug=True)
    else:
        app.run(debug=False)
