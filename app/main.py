from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    print(request.headers)
    return {
        "status": "success",
    }
