from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from routes.auth import auth_bp
from routes.board import board_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(board_bp, url_prefix='/board')

if __name__ == '__main__':
    app.run(debug=True)