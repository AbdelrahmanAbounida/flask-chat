from .config import config_dict
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask import Flask
from typing import Literal

# instantiate the extensions
db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_name: Literal["default","testing","production","development"]="default"):
    # basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__,static_url_path="/static")

    # App Configuration
    app.config.from_object(config_dict[config_name])

    # initalize extensions 
    db.init_app(app)
    bcrypt.init_app(app)

    # Allow cors
    # CORS(app)
    # CORS(app, resources={
    #     r"/*":{
    #     "origins":"*"
    #     }
    # })

    # register blueprints
    # from routes.chat import chat_router_pb,chat_router_pb_api
    from app.main.routes.chat import chat_router_pb, message_router_pb
    app.register_blueprint(chat_router_pb)
    app.register_blueprint(message_router_pb)


    return app





