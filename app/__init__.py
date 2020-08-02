import os 
import logging.config

from flask import Flask, Blueprint
from flask_restx import Api, apidoc
from werkzeug.contrib.fixers import ProxyFix

from .api import (    
    API,
    register_swagger,
    register_todos,
    register_default
)

from .config import AppConfig
from .__version__ import __version__

logger = logging.getLogger(__name__)    
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)    

def create_app():
    
    app = Flask(__name__)
    AppConfig.register_flask(app)
    
    logger.info("Initialising TODO API Server v %s ..." % __version__)
    blueprint = Blueprint('api', __name__, url_prefix='{}/api/v1'.format(AppConfig.get('SERVER_BASE')))    
    
    register_todos()
    register_default()
    API.init_app(blueprint)
    app.register_blueprint(blueprint)
    
    register_swagger(app, AppConfig.get('SERVER_BASE'))
    app.wsgi_app = ProxyFix(app.wsgi_app)            
    
    return app