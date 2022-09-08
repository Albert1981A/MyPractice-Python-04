from flask import jsonify, request, Blueprint

from BL.user_bl import UserBL

users = Blueprint("users", __name__)

user_bl = UserBL()
#headers: {"Access-Control-Allow-Origin": "*"}
# This router will sed all cars
@users.route('/', methods=['GET'])
def get_all_users():
    return jsonify(user_bl.get_all_users())

# This router will sed one car by his ID
@users.route('/<string:userId>', methods=['GET'])
def get_user(userId):
    return jsonify(user_bl.get_user(userId))

# This router receive and create new car
@users.route('/', methods=['POST'])
def create_user():
    data = request.json
    return jsonify(user_bl.add_user(data))

# This router receive and update an existing car
@users.route('/<string:userId>', methods=['PUT'])
def update_user(userId):
    data = request.json
    return jsonify(user_bl.update_user(userId, data))

# This router delete car by his ID
@users.route('/<string:userId>', methods=['DELETE'])
def delete_user(userId):
    return jsonify(user_bl.delete_user(userId))
