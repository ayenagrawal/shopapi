from flask_restful import Resource
from sqlalchemy import delete
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        data = StoreModel.find_by_name(name)
        if data:
            return data.json()
        return {'message': 'Store not found.'}, 404

    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A Store with name '{}' already exists.".format(name)}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store.'}, 500
        
        return store.json(), 201
    
    def delete(self, name):
        data = StoreModel.find_by_name(name)
        if data:
            data.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
