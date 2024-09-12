from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db: SQLAlchemy = SQLAlchemy(engine_options={ 'connect_args': { 'connect_timeout': 5 }})
migrate: Migrate = Migrate()
bcrypt: Bcrypt = Bcrypt()
jwt: JWTManager = JWTManager()