from core.models.tables import Paciente, User
from core import db
def excluir(username):
    pacientes = Paciente.query.all()
    for p in pacientes:
        if p.user.username == username:
            break
    db.session.delete(p)
    db.session.commit()

    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()