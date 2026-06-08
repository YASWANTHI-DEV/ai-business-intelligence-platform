import bcrypt
from database import add_user, get_user


def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )


def register_user(username, password):

    hashed_password = hash_password(password)

    return add_user(
        username,
        hashed_password
    )


def login_user(username, password):

    user = get_user(username)

    if user:

        stored_password = user[2]

        if bcrypt.checkpw(
            password.encode(),
            stored_password
        ):
            return True

    return False