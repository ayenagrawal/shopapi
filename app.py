from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenicate, identity
from resources.user import UserRegistration
from resources.store import Store, StoreList
from resources.item import Item, Items
from db import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.secret_key = os.getenv('secret_key').encode('UTF-8')
db_URI = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
if db_URI.split()[0].startswith('postgres://'): db_URI = db_URI.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
jwt = JWT(app, authenicate, identity)

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores/')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items/')
api.add_resource(UserRegistration, '/register')

@app.route('/',methods=["GET"])
def mn():
    return '<h1>Hi There !</h1>'

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)