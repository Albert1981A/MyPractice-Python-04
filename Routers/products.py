from flask import jsonify, request, Blueprint

from BL.product_bl import ProductBL

products = Blueprint("products", __name__)

product_bl = ProductBL()

# This router will sed all cars
@products.route('/', methods=['GET'])
def get_all_products():
    return jsonify(product_bl.get_all_products())

# This router will sed one car by his ID
@products.route('/<string:productId>', methods=['GET'])
def get_product(productId):
    return jsonify(product_bl.get_product(productId))

# This router receive and create new car
@products.route('/', methods=['POST'])
def create_product():
    data = request.json
    return jsonify(product_bl.add_product(data))

# This router receive and update an existing car
@products.route('/<string:productId>', methods=['PUT'])
def update_products(productId):
    data = request.json
    return jsonify(product_bl.update_product(productId, data))

# This router delete car by his ID
@products.route('/<string:productId>', methods=['DELETE'])
def delete_product(productId):
    return jsonify(product_bl.delete_product(productId))

# 3:22
