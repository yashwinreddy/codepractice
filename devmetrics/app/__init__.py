from flask_dance.contrib.github import make_github_blueprint, github
import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("FLASK_SECRET_KEY")

    github_bp = make_github_blueprint(
        client_id=os.getenv('Ov23liXZ4qDunIrxjL2V'),
        client_secret=os.getenv('16feb4d17754f8ecbbbc062bb8bc6fd0d22a9587'),
    )
    app.register_blueprint(github_bp, url_prefix="/github_login")

    from .routes import main
    app.register_blueprint(main)
    return app
