import os
from flask import render_template
from flask_classful import FlaskView

class ApproverView(FlaskView): 
    def __init__(self): 
        self.__TEMPLATE_DIR__ = "approver"

    def index(self):
        return render_template(f"{self.__TEMPLATE_DIR__}/index.html")