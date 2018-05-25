from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, DateField
from wtforms.fields.html5 import EmailField
from wtforms import validators 

class LoginForm(FlaskForm):
    username = StringField("username", validators=[validators.DataRequired()])
    password = PasswordField("password", validators=[validators.DataRequired()])
    remember_me = BooleanField("remember_me")

def username_unique(form, field):
    from core.controllers.listarPaciente import listarPaciente
    pacientes = listarPaciente()
    print(pacientes)
    for p in pacientes:
        if p["username"] == field.data:
            raise validators.ValidationError("Este username já esta sendo usado")

def email_unique(form, field):
    from core.controllers.listarPaciente import listarPaciente
    for p in listarPaciente():
        if p["email"] == field.data:
            raise validators.ValidationError("Este email já esta sendo usado")

def tamanho_senha(form, field):
    if len(field.data) not in range(6,9):
        raise validators.ValidationError('A senha deve conter no minimo 6 caracteres e nomáximo 8')

def min_mai_number(form, field):
    s = field.data
    if not(any(x.islower() for x in s)) or not(any(x.isupper() for x in s)) or not(any(x.isdigit() for x in s)):
        raise validators.ValidationError("A senha deve conter letras minusculas, maiusculas e numeros")

class CadastroPacienteForm(FlaskForm):
    name = StringField("name", validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.length(min=3, message="O nome esta muito curto"),
        ])
    email = EmailField("email", validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.Email(message="Digite um email valido"),
        email_unique,
        ])
    dataNascimento = DateField("dataNascimento", validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        ])
    sexo = RadioField("sexo", choices=[("M","Masculino"),("F","Feminino")], validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        ])
    cidade = StringField("cidade", validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.length(min=3, message="O nome da cidade esta muito curto")
        ])
    profissao = StringField("profissao", validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.length(min=3, message="O nome da profissão esta muito curto")
        ])
    celular = StringField('celular', validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.length(min=11, max=11, message="Digite um celular valido exemplo:11912345678")
        ])
    objetivo = StringField('objetivo',validators=[
        validators.DataRequired(message="Este campo é obrigatorio")
        ])
    username = StringField('username', validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.length(min=5, max=30, message="Digite um username de 5 a 30 caracteres"),
        username_unique,
    ])
    password = PasswordField("password", validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.EqualTo('c_password', message="As senhas estão diferentes"),
        min_mai_number,
        tamanho_senha,
    ])
    c_password = PasswordField('confirmar pasword', validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
    ])


class AlterarSenhaForm(FlaskForm):
    password = PasswordField("password", validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.EqualTo('c_password', message="As senhas estão diferentes"),
        min_mai_number,
        tamanho_senha,
    ])
    c_password = PasswordField('confirmar pasword', validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
    ])
         