from flask import Flask, render_template
from apps.approver import approver_app
from apps.requester import requester_app

app = Flask(__name__) 
app.register_blueprint(approver_app.app, url_prefix='/approver')
app.register_blueprint(requester_app.app, url_prefix='/requester')

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)