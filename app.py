from flask import Flask 
from flask_restful import Api 
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store,StoreList
from db import db


# Define app settings with flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'razhty'
api = Api(app)
# take the values from authenticate.py to verify identity through flas_JWT
jwt = JWT(app, authenticate, identity)




#HTML redirections, and theyr resources.
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    #TODO remove debug after production// def. port used 5000
    db.init_app(app)
    app.run(port=5000, debug=True)
