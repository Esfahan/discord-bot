from flask import Flask
from amongus.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object('amongus.config.Config')

    init_db(app)

    return app

app = create_app()
app.app_context().push()
