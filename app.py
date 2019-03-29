from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import FormConsulta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'dev'
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

