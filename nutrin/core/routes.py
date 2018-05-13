from core import app, db, lm, response
from flask import render_template, redirect, url_for, flash
from core.controllers.index import index


#login
from flask_login import login_user, logout_user
from core.models.tables import User, Paciente, Nutricionista

#form
from core.models.forms import LoginForm, CadastroPacienteForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/login", methods=["POST","GET"])
def loginRoute():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('indexRoute'))
            flash("Login in")
        else:
            flash("Invalid Login")
    else:
        print(form.errors)
    return render_template('login.html', form=form)

@app.route("/areaNutricionista", methods=["GET"])
def areaNutricionistaRoute():
    return render_template('areaNutricionista.html')

@app.route("/cadastrarPaciente", methods=['POST','GET'])
def cadastrarPacienteRoute():
    form = CadastroPacienteForm()
    if form.validate_on_submit():
        p = Paciente(
            form.username.data,
            form.password.data,
            form.name.data,
            form.email.data,
            form.celular.data,
            form.dataNascimento.data,
            form.sexo.data,
            form.cidade.data,
            form.profissao.data,
            form.objetivo.data
        )
        db.session.add(p)
        db.session.commit()
    else:
        print(form.errors)
    return render_template('cadastroPaciente.html', form=form)

@app.route("/pacientes", methods=["GET"])
def listarPacienteRoute():
    from core.controllers.listarPaciente import listarPaciente
    response['Dados'] = listarPaciente()
    return render_template('areaNutricionista/listarPaciente.html', response=response)

@app.route("/paciente/<paciente_username>", methods=["GET"])
def consultarPacienteRoute(paciente_username):
    from core.controllers.consultarPaciente import consultarPaciente
    return render_template('perfilPaciente.html')

@app.route("/")
def indexRoute():
    return index()

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('indexRoute'))