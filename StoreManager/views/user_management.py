from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from ..models.users import User
import json

bp = Blueprint('users', __name__, url_prefix='/auth')


@bp.route('/api/v1/register', methods=('POST'))
def register():
    user=User()
    user_data = request.get_json
    first_name =  user_data.get('first_name')
    last_name = user_data.get('last_name')
    username = user_data.get('username')
    password = user_data.get('password')        
    
    #confirm that required fields are not empty
    if not (first_name and last_name and username and password):
        error = "Required fields must be filled and non-zero!"
        return jsonify({"response": error}), 400

    if user.get_a_user(username) != None:
        message = "username already taken"
        return jsonify({"response": message}), 400

    #Assign admin or user previledge
    if user.get_users() == None:
        user_role = "admin"
    else:
        user_role = "user"  
    try:
        user.addUser(first_name, last_name, username, password, user_role) 
        message = 'User {} has been created!'. format(username)
    except Exception as e:
        message = e + " " + "User account not created!"

    return jsonify({"Response": message})

@bp.route('/api/v1/login', methods=('POST'))
def login():
    user=User()
    user_data = request.get_json
    username = user_data.get('username')
    password = user_data.get('password') 
      
    response = user.login(username, password)
    if response == "incorrect username":
        message = "incorrect username entered!"
    elif response == "incorrect password!":
        message = "incorrect password entered!"
    elif response == "admin":
        message = "Welcome! successfully logged in as admin" 
    elif response == "user":  
        message = 'Welcome! Successfully logged in!'
    return jsonify({"Response": message})


        
        