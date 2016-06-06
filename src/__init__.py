# -*- coding: UTF-8 -*- 

from flask import Flask
from src.controllers import *
# from src.controllers.order import fitnessorder

def create_guirenagent_app():
    app = Flask(__name__)
    app.jinja_env.variable_start_string = '(('
    app.jinja_env.variable_end_string = '))'
    app.config.from_pyfile('agentconfig.py')
    app.register_module(home)

    return app