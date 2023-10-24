from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1><b>Welcome!</b></h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)