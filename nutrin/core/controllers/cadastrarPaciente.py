from core.models.tables import Paciente
from core import db
def cadastrar(username, password, name, email, celular, dataNascimento, sexo, cidade, profissao, objetivo):
    p = Paciente(username,password, name, email, celular, dataNascimento, sexo, cidade, profissao, objetivo)
    db.session.add(p)
    db.session.commit()