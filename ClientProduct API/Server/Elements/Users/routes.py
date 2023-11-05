from flask import Blueprint, jsonify, request
from flask_jwt_extended import *
from ReadWriteOps import *
import bcrypt

usersBP = Blueprint("users", __name__)

fileName = "ClientProduct API\\JSON\\User.json"

@usersBP.post("/")
def registerUser():
    users = readFile(fileName)
    if request.is_json:
        user = request.get_json()
        password = user["password"].encode("utf-8")
        salt = bcrypt.gensalt() # Random number added to password for increased security.
        hashPassword = bcrypt.hashpw(password, salt).hex() # Final password to assign to new user.
        user["password"] = hashPassword # Password assignment.
        users.append(user)
        writeFile(users, fileName)
        token = create_access_token(identity=user["username"]) # Token generation to give access to the new user.
        return {"token": token}, 201
    else:
        return {"error": "Request must be a JSON file."}, 415

@usersBP.get("/")
def getUser():
    users = readFile(fileName)
    if request.is_json:
        user = request.get_json()
        username = user["username"]
        password = user["password"].encode("utf-8")
        for userFile in users:
            if userFile[username] == username:
                passwordFile = userFile["password"]
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token = create_access_token(identity=username)
                    return {"token": token}, 200
                else:
                    return {"error": "Not authorized!"}, 401
            else:
                return {"error": "User was not found."}, 404
    else:
        return {"error": "Request must be a JSON file."}, 415