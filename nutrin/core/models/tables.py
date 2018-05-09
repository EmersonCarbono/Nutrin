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

    def __init__(self, name, email, tipo):
        self.username = self.id
        self.password = "nutrin1700"
        self.name = name
        self.email = email
        self.tipo = tipo
    
    def __repr__(self):
        return "<User {0}>".format(self.username)
    
class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    dataNascimento = db.Column(db.String)
    sexo = db.Column(db.String(1))
    cidade = db.Column(db.String(50))
    profissao = db.Column(db.String(50))
    celular = db.Column(db.String(11))
    objetivo = db.Column(db.String(50))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, name, email, dataNascimento, sexo, cidade, profissao, celular, objetivo):
        u = User(name, email, "P")
        db.session.add(u)
        db.session.commit()
        self.user_id = u.id
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.cidade = cidade
        self.profissao = profissao
        self.celular = celular
        self.objetivo = objetivo


class Nutricionista(db.Model):
    __tablename__ = "nutricionistas"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, username, password, name, email):
        u = User(username, password, name, email, "N")
        db.session.add(u)
        db.session.commit()
        self.user_id = u.id
    
    def __repr__(self):
        return "<Nutricionista {0}>".format(self.username)

