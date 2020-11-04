from flask import Blueprint

app = Blueprint('requester', __name__, template_folder='templates')

@app.route("/")
def index():
    return "Hello from requester"