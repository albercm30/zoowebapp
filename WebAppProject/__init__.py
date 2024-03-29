from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy() 
bcrypt = Bcrypt()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqldb://23_webapp_11:0c0C6tnk@mysql.lab.it.uc3m.es/23_webapp_11c"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Inside create_app:
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from . import model
    @login_manager.user_loader
    def load_user(user_id):
        return model.User.query.get(int(user_id))

    # Register blueprints:
    from . import main,auth

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    return app