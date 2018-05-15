from core.models.tables import User
from flask_login import login_user
def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
        return True
    else:
        return False