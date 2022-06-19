from flask_restful import Resource, reqparse
import sqlite3
from models.user import UserModel

class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help='This field can not be left blank!'
        )
    parser.add_argument('password',
            type=str,
            required=True,
            help='This field can not be left blank!'
        )
    
    def post(self):
        data = UserRegistration.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {'message': 'A user with same username already exists'}, 400
        
        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User created successfully'}, 201