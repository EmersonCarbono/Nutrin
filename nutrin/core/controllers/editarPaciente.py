from core.models.tables import Paciente
from core import db

def editar(paciente_username, dados):
    pacientes = Paciente.query.all()
    for p in pacientes:
        if p.user.username == paciente_username:
            break
    print(dados)
    p.user.username = dados[0]['username']
    p.user.senha = dados[0]['senha']
    p.user.name = dados[0]['name']
    p.user.email = dados[0]['email']
    p.user.celular = dados[0]['celular']
    p.dataNascimento = dados[0]['dataNascimento']
    p.sexo = dados[0]['sexo']
    p.cidade = dados[0]['cidade']
    p.profissao = dados[0]['profissao']
    p.objetivo = dados[0]['objetivo']

    db.session.commit()
