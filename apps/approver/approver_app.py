from flask import Blueprint, render_template

app = Blueprint('approver', __name__, template_folder='templates')

@app.route("/")
def index():
    # return "Hello from Approver"
    return render_template("index.html")