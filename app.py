import os
from flask import Flask, render_template, request, redirect, session, abort, flash
from flask_sqlalchemy import SQLAlchemy
from forms import FormConsulta, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = os.urandom(12)
db = SQLAlchemy(app)

class Pedido(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	cliente = db.Column(db.String)
	desc = db.Column(db.String)
	status = db.Column(db.Integer)

@app.route('/', methods=['GET','POST'])
def index():
	form = FormConsulta()
	pedidos = Pedido.query.all()
	id = form.id.data
	resultado = Pedido.query.filter_by(id=id).first()
	return render_template('index.html', resultado=resultado, form=form)

@app.route('/admin')
def admin():
	pedidos = Pedido.query.all()
	form = LoginForm()
	if not session.get('logged_in'):
		return render_template('login.html', form=form)
	else:
		return render_template('admin.html', pedidos=pedidos)

@app.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True
	else:
		flash('Verifique o usuário e senha')
	return admin()

@app.route('/logout', methods=['POST'])
def logout():
	session['logged_in'] = False
	return redirect('admin')