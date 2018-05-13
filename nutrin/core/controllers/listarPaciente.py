from core.models.tables import Paciente

def listarPaciente():
    r = []
    pacientes = Paciente.query.all()
    for p in pacientes:
        r.append({"nome":p.user.name,"username":p.user.username,"email":p.user.email,"celular":p.user.celular})
    return r