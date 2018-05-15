from core.models.tables import Paciente

def consultarPaciente(username):
    r = []
    pacientes = Paciente.query.all()
    for p in pacientes:
        if p.user.username == username:
            break
    r.append({
        'username': p.user.username
        ,'name':p.user.name
        ,'email':p.user.email
        ,'celular':p.user.celular
        ,'dataNascimento':p.dataNascimento
        ,'sexo':p.sexo
        ,'cidade':p.cidade
        ,'profissao':p.profissao
        ,'objetivo':p.objetivo
    })
    return r