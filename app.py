from flask import Flask

app = Flask(__name__)

@app.route("up/")
def hello_world():
    return "<p>Up</p>"
