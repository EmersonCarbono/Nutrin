from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("passeord", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class CadastroPacienteForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    dataNascimento = StringField("dataNascimento", validators=[DataRequired()])
    sexo = RadioField("sexo", choices=[("M","Masculino"),("F","Feminino")], validators=[DataRequired()])
    cidade = StringField("cidade", validators=[DataRequired()])
    profissao = StringField("profissao", validators=[DataRequired()])
    celular = StringField('celular', validators=[DataRequired()])
    objetivo = StringField('objetivo', validators=[DataRequired()])