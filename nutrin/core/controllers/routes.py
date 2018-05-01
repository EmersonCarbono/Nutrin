#from index import index
from core import app, db, lm
from flask import render_template, redirect, url_for, flash

#login
from flask_login import login_user, logout_user
from core.models.tables import User
from core.models.forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/login")
def loginRoute():
    form = LoginForm() 
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))
            flash("Login in")
        else:
            flash("Invalid Login")
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route("/")
def indexRoute():
    return render_template('index.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('indexRoute'))