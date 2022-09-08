from flask import Flask

from Routers.cars import cars
from Routers.products import products
from Routers.users import users
from flask_cors import CORS

# Creating a web application
app = Flask(__name__)

# Opening the application to receive calls from the web
cors = CORS(app)

app.register_blueprint(cars, url_prefix='/cars')
app.register_blueprint(products, url_prefix='/products')
app.register_blueprint(users, url_prefix='/users')

app.run()