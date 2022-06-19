from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenicate, identity
from resources.user import UserRegistration
from resources.store import Store, StoreList
from resources.item import Item, Items
from db import db

app = Flask(__name__)
api = Api(app)
app.secret_key = r'abcdefgh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
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

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, port=5000)