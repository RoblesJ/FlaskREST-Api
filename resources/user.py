import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    # Take the data with flask's reqparse by the arguments we need to authenticate
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True,
                        help="This field can't be blank")
    parser.add_argument("password", type=str, required=True,
                        help="This field can't be blank")

    def post(self):
        # Obtain data.
        data = UserRegister.parser.parse_args()

        # Verify if the username already exists.
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()
        # Code 201, User created successfully
        return {"message": "User created successfully"}, 201
