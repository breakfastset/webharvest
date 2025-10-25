from flask import Flask
app = Flask(__name__)

@app.route("/")
def index_page():
    return "Hello World!"

@app.route("/second")
def next_page():
    return "<b>Next</b> Page!!"

if __name__ == "__main__":
    app.run(port=5555)