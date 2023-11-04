from flask import *
from Elements.Clients.routes import clientsBP
from Elements.Products.routes import productsBP

app = Flask(__name__)

app.register_blueprint(clientsBP, url_prefix="/clients")
app.register_blueprint(productsBP, url_prefix="/products")

@app.route("/")
def index():
    return "<h1 style=\"font-family: 'Arial', 'Verdana', sans-serif;\">Welcome!</h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)