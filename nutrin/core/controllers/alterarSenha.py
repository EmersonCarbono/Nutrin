from core.models.tables import User
from core import db

def alterarSenha(username, senha):
    users = User.query.all()
    for u in users:
        if u.username == username:
            break
    
    u.password = senha
    db.session.commit()
    
