from app.modules.auth import auth_bp
from flask import Flask

def register_blueprints(app: Flask):
    app.register_blueprint(auth_bp)