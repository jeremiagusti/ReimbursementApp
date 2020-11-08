import os
from flask import Flask, render_template
from views.requestor_view import RequestorView
from views.approver_view import ApproverView
from libs.shared import db

app = Flask(__name__, template_folder="views/templates") 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reimbursement.db"

db.init_app(app)

@app.route("/")
def index():
    return "Hello World"

# Requestor related applications
RequestorView.register(app)
ApproverView.register(app)

if __name__ == "__main__":
    app.run(debug=True)