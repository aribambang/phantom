from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")

from app.modules.auth.controllers import post_register_controller