from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    # Obtain the user data from the User object.
    user = UserModel.find_by_username(username)
    #verify the existance of the user, and do a safe comp. of it's values
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    #i dont understand this part.
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


