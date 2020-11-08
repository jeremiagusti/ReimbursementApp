import os
from constants import REQUESTOR
from flask import render_template
from flask_classful import FlaskView

class RequestorIndexView(FlaskView): 
    route_base = REQUESTOR["BASEPATH"]

    def __init__(self): 
        self.__TEMPLATE_DIR__ = REQUESTOR["TEMPLATE_DIR"]
    
    def index(self):
        return render_template(f"{self.__TEMPLATE_DIR__}/index.html")