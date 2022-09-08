from flask import jsonify, request, Blueprint

from BL.car_bl import CarBL

cars = Blueprint("cars", __name__)

car_bl = CarBL()

# This router will sed all cars
@cars.route('/', methods=['GET'])
def get_all_cars():
    return jsonify(car_bl.get_all_cars())

# This router will sed one car by his ID
@cars.route('/<string:carId>', methods=['GET'])
def get_car(carId):
    return jsonify(car_bl.get_car(carId))

# This router receive and create new car
@cars.route('/', methods=['POST'])
def create_car():
    data = request.json
    return jsonify(car_bl.add_car(data))

# This router receive and update an existing car
@cars.route('/<string:carId>', methods=['PUT'])
def update_car(carId):
    data = request.json
    return jsonify(car_bl.update_car(carId, data))

# This router delete car by his ID
@cars.route('/<string:carId>', methods=['DELETE'])
def delete_car(carId):
    return jsonify(car_bl.delete_car(carId))
