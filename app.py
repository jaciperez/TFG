
from flask import Flask, render_template, request, redirect
from database import db
import os

# Creamos la app primero
app = Flask(__name__)

# Configuramos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volantes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos con la app
db.init_app(app)

# Creamos las tablas si no existen
with app.app_context():
    db.create_all()

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/volante')
def volante():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



