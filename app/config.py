import os
import json
import logging

class AppConfig():

    __conf = {
            "SERVER_BASE": os.getenv("SERVER_BASE", "/todoapp"),
            "ENV": os.getenv("FLASK_ENV", "production"),
            "DEBUG": False if os.getenv('FLASK_DEBUG', None) is None else os.getenv('FLASK_DEBUG', None).lower() == 'True'.lower(),
            "RESTPLUS_SWAGGER_UI_DOC_EXPANSION": 'full',
            "RESTPLUS_VALIDATE": True,
            "RESTPLUS_MASK_SWAGGER": False,
            "ERROR_404_HELP": False,
            "GUNICORN_WORKERS": os.getenv('GUNICORN_WORKERS', 1)            
        }

    __flask_params = ["SERVER_BASE", "ENV", "DEBUG", "RESTPLUS_SWAGGER_UI_DOC_EXPANSION", "RESTPLUS_VALIDATE", 
                      "RESTPLUS_MASK_SWAGGER", "ERROR_404_HELP", "RESTPLUS_MASK_SWAGGER"]

    @staticmethod
    def register_flask(flask_app):
        for param_name in AppConfig.__flask_params:
            flask_app.config[param_name] = AppConfig.__conf[param_name]

    @staticmethod
    def get(name):
        return AppConfig.__conf[name]

    @staticmethod
    def set(name, value):
        if name in AppConfig.__conf:
            AppConfig.__conf[name] = value
        else:
            raise NameError("Attribute name not found in AppConfig")