from core.models.tables import Paciente

def consultarPaciente(username):
    r = []
    p = Paciente.query.filter_by(username=username).first()
    r.append({""})