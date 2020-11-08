import os
from flask import render_template
from flask_classful import FlaskView

class ApproverIndexView(FlaskView): 
    def index(self):
        return render_template("index.html")