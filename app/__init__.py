from flask import Flask, app 
from flask_bootstrap import Bootstrap
from .config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db=SQLAlchemy()

def create_app(config_name):
    app= Flask(__name__)

   # Creating the app configs
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting configuration
    from .request import configure_request
    configure_request(app)

    #registering auth blueprint 
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    from .main import views
    from .main import error

    return app