from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, DateField
from wtforms.fields.html5 import EmailField
from wtforms import validators 

class LoginForm(FlaskForm):
    username = StringField("username", validators=[validators.DataRequired()])
    password = PasswordField("passeord", validators=[validators.DataRequired()])
    remember_me = BooleanField("remember_me")


class CadastroPacienteForm(FlaskForm):
    name = StringField("name", validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.length(min=3, message="O nome esta muito curto"),
        ])
    email = EmailField("email", validators=[
        validators.DataRequired(message="Este campo é obrigatorio"),
        validators.Email(message="Digite um email valido")
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

         