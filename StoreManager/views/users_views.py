from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..models.users import User
import json

bp = Blueprint('users', __name__, url_prefix='/auth')


@bp.route('/api/v1/signup', methods=['POST'])
def register():
    user=User()
    user_data = request.get_json()
    first_name =  user_data.get('first_name')
    last_name = user_data.get('last_name')
    username = user_data.get('username')
    password = generate_password_hash(user_data.get('password'))        
    
    #confirm that required fields are not empty
    if not (first_name and last_name and username and password):
        error = "Required fields must be filled and non-zero!"
        return jsonify({"response": error}), 400

    if user.get_a_user(username) != None:
        message = "username already taken"
        return jsonify({"response": message}), 400

    #Assign admin or user previledge
    if user.get_users() == []:
        user_role = "admin"
    else:
        user_role = "user"  
    try:
        user.addUser(first_name, last_name, username, password, user_role) 
        access_token = create_access_token(identity=username)
        message = 'User {} has been created!'. format(username)
        return jsonify({"Response": message, "access_token": access_token}),200
    except Exception as e:
        return jsonify({"Response": e})

@bp.route('/api/v1/login', methods=['POST'])
def login():
    user=User()
    user_data = request.get_json()
    username = user_data.get('username')
    password = user_data.get('password')       
    new_user = user.get_a_user(username)
    if not new_user:
        response = "incorrect username!"
    elif not check_password_hash(new_user['password'], password):
        response = "incorrect password!"      
    elif new_user["role"] == "admin":
        response = "Welcome! successfully logged in as admin" 
        access_token = create_access_token(identity=username)
    elif new_user["role"] == "user":  
        response = 'Welcome! Successfully logged in!'
        access_token = create_access_token(identity=username)
    return jsonify({"Response": response, "access_token": access_token}),200

@bp.route('/api/v1/users')
@jwt_required
def get_all_users():
    user = User()
    current_user = get_jwt_identity()
    if user.get_a_user(current_user)['role'] == 'user':
        response = "You are not authorised to perform this operation!"
        return jsonify(response), 401
    response = user.get_users()
    if len(response) == 0:    
        message = "There are no users registered!"
        return jsonify({"response":message}), 200
    
    message = "available_users" 
    return jsonify({message:response}), 200

@bp.route('/api/v1/users/upgrade/<username>', methods = ['PUT'])
@jwt_required
def upgrade_a_user(username):
    user = User()
    current_user = get_jwt_identity()
    if user.get_a_user(current_user)['role'] == 'user':
        response = "You are not authorised to perform this operation!"
        return jsonify(response), 401
    user.upgradeUser(username)
    response = "User %s has been upgraded to admin status" %username
    return jsonify({"response": response}), 200

@bp.route('/api/v1/users/downgrade/<username>', methods = ['PUT'])
@jwt_required
def downgrade_a_user(username):
    user = User()
    current_user = get_jwt_identity()
    if user.get_a_user(current_user)['role'] == 'user':
        response = "You are not authorised to perform this operation!"
        return jsonify(response), 401
    user.downgradeUser(username)
    response = "User %s has been downgraded to user status" %username
    return jsonify({"response": response}), 200
    
        