import os
from flask import Flask, render_template
from apps.requestor.requestor_index import RequestorIndexView
from apps.approver.approver_index import ApproverIndexView

app = Flask(__name__, template_folder="templates") 

@app.route("/")
def index():
    return "Hello World"

# Requestor related applications
RequestorIndexView.register(app)

if __name__ == "__main__":
    app.run(debug=True)