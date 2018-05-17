from core import app, db, lm, response
from flask import render_template, redirect, url_for, flash
from core.models.tables import  User

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/login", methods=["POST","GET"])
def loginRoute():
    from core.controllers.login import login
    from core.models.forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        if login(form.username.data,form.password.data):
            return redirect(url_for('indexRoute'))
    return render_template('login.html', form=form)

@app.route("/areaNutricionista", methods=["GET"])
def areaNutricionistaRoute():
    return render_template('areaNutricionista/areaNutricionista.html')

@app.route("/cadastrarPaciente", methods=['POST','GET'])
def cadastrarPacienteRoute():
    from core.controllers.cadastrarPaciente import cadastrar
    from core.models.forms import CadastroPacienteForm
    form = CadastroPacienteForm()
    if form.validate_on_submit():
        cadastrar(form.username.data,
        form.password.data,
        form.name.data,
        form.email.data,
        form.celular.data,
        form.dataNascimento.data,
        form.sexo.data,
        form.cidade.data,
        form.profissao.data,
        form.objetivo.data)
    return render_template('areaNutricionista/cadastroPaciente.html', form=form)

@app.route("/pacientes", methods=["GET"])
def listarPacienteRoute():
    from core.controllers.listarPaciente import listarPaciente
    response['Dados'] = listarPaciente()
    return render_template('areaNutricionista/listarPaciente.html', response=response)

@app.route("/paciente/<paciente_username>", methods=["GET"])
def consultarPacienteRoute(paciente_username):
    from core.controllers.consultarPaciente import consultarPaciente
    response["Dados"] = consultarPaciente(paciente_username)
    return render_template('perfilPaciente.html', response=response)

@app.route("/editar/<paciente_username>", methods=["GET", "POST"])
def alterarCadastroPacienteRoute(paciente_username):
    from core.controllers.consultarPaciente import consultarPaciente
    from core.controllers.editarPaciente import editar
    from core.models.forms import CadastroPacienteForm
    form = CadastroPacienteForm()
    response["Dados"] = consultarPaciente(paciente_username)
    if form.validate_on_submit(): 
        dados = [{
        'username': form.username.data
        ,'senha': form.password.data
        ,'name': form.name.data
        ,'email': form.email.data
        ,'celular': form.celular.data
        ,'dataNascimento': form.dataNascimento.data
        ,'sexo': form.sexo.data
        ,'cidade': form.cidade.data
        ,'profissao': form.profissao.data
        ,'objetivo': form.objetivo.data
        }]
        editar(paciente_username, dados)
    return render_template('editarPaciente.html', response=response, form=form)

@app.route("/excluir/<paciente_username>", methods=["GET"])
def excluirPacienteRoute(paciente_username):
    from core.controllers.excluirPaciente import excluir
    excluir(paciente_username)
    return redirect(url_for('listarPacienteRoute'))

@app.route("/")
def indexRoute():
    from core.controllers.index import index
    return index()

@app.route("/logout")
def logout():
    from flask_login import logout_user
    logout_user()
    return redirect(url_for('indexRoute'))