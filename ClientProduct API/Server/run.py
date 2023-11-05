from flask import * # All necessary libraries are imported for later use.
from flask_jwt_extended import *
from Elements.Users.routes import usersBP
from Elements.Clients.routes import clientsBP
from Elements.Products.routes import productsBP
import random

def passwordEncrypter(): # This function is responsible for randomizing characters in the password.
    password = "" # Password declaration.
    for i in range(30): # Character generation goes up to 30.
        index = random.randint(33, 122) # Index used to get ASCII table character.
        password = password + chr(index) # chr(index) is used to get the character from the ASCII table with the index. The inverted function is ord(char).
    return password # Returns the password once the function is done generating.

app = Flask(__name__)
app.config["PASSWORD"] = passwordEncrypter() #A random encrypted password is generated. Example: B'!fo5"0\O/y)Rg!f=kC0F6iH?H`U\.
jwt = JWTManager(app) # JWT Manager is initialized.

#All blueprints are registered along with their following code.
app.register_blueprint(usersBP, url_prefix="/users")
app.register_blueprint(clientsBP, url_prefix="/clients")
app.register_blueprint(productsBP, url_prefix="/products")

# First page showing the index of the server.
@app.route("/")
def index():
    return "<h1 style=\"font-family: 'Arial', 'Verdana', sans-serif;\">Welcome!</h1>"

# Code used to startup the server. Server may be accessed with "http://localhost" along with port number.
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)