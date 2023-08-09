from flask import Flask, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/no_content')
def no_content():
    return ({"message":"No content found"}, 204)

@app.route('/exp')
def index_explicit():
    """
    give response "Hello World!" when status 200
    """
    resp = make_response({"message": "Hello World!"})
    resp.status_code = 200
    return resp