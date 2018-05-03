from core import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    tipo = db.Column(db.String(1))

    #tipo: N - nutricionista, P - paciente, A - admin  

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email, tipo):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.tipo = tipo
    
    def __repr__(self):
        return "<User {0}>".format(self.username)
    
class Paciente(User):
    __tablename__ = "pacientes"

    dataNascimento = db.Column(db.DateTime)
    sexo = db.Column(db.String)
    cidade = db.Column(db.String)
    profissao = db.Column(db.String)
    celular = db.Column(db.String)
    objetivo = db.Column(db.String)

    def __init__(self, username, password, name, email, dataNascimento, sexo, cidade, profissao, celular, objetivo):
        super().__init__(username, password, name, email, "P")
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.cidade = cidade
        self.profissao = profissao
        self.celular = celular
        self.objetivo = objetivo
    
    def __repr__(self):
        return "<Paciente {0}>".format(self.username)
