from flask import Flask, Response, make_response, jsonify
from typing import Type
from config.config import Config
import logging
from logging.config import dictConfig
from config.logging import LOGGING_CONFIG
from app.container import register_dependencies
from app.modules import register_blueprints
from app.extensions import db, migrate, bcrypt, jwt
from app.utils.error_handlers import (handle_validation_error, handle_value_error)
from pydantic import ValidationError
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

def create_app(config_class: Type[Config] = Config) -> Flask:
    dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    app: Flask = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register dependencies
    register_dependencies(app)

    # Register blueprints here
    register_blueprints(app)

    # Register error handlers
    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(ValueError, handle_value_error)

    @app.errorhandler(401)
    def unauthorized(error):
        response = Response(
            jsonify({'error': 'Unauthorized access'}), status=401)
        return response

    @app.route('/health')
    def health_check() -> Response:
        try:
            db.session.execute(text('SELECT 1'))
            return make_response(jsonify(statusCode=200, message="Ok" ), 200)
        except SQLAlchemyError as e:
            logger.error(f"Database error: {str(e)}")
            return make_response(jsonify(statusCode=503, message="Service Unavailable" ), 503)
        except Exception as e:
            logger.error(f"Internal server error: {str(e)}")
            return make_response(jsonify(statusCode=500, message="Internal Server Error" ), 500)

    logger.info("Application started")
    for rule in app.url_map.iter_rules():
                methods = ','.join(sorted(rule.methods))
                logger.info(f"{rule.endpoint}: {rule.rule} [{methods}]")

    return app