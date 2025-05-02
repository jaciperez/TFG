
from flask import Flask, render_template, request, redirect
from database import db
from models import Volante
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

# donde se guardan los datos del formulario en la base de datos
@app.route('/guardar_volante', methods=['POST'])
def guardar_volante():
    datos = request.form

    nuevo_volante = Volante(
        citado=datos.get('citado'),
        fecha=datos.get('fecha'),
        hora=datos.get('hora'),
        hab=datos.get('hab'),
        ext=datos.get('ext'),
        enfermera=datos.get('enfermera'),
        numero=datos.get('numero'),
        box=datos.get('box'),

        diabetes='diabetes' in datos,
        renal='renal' in datos,
        alergia_yodo='alergia_yodo' in datos,
        cardiopata='cardiopata' in datos,

        insulina='insulina' in datos,
        ADO='ADO' in datos,
        antibioticos='antibioticos' in datos,
        corticoides='corticoides' in datos,

        estadificacion='estadificacion' in datos,
        respuesta_a_tto='respuesta_a_tto' in datos,
        control_evolutivo='control_evolutivo' in datos,
        TOD='TOD' in datos,

        planificacion_rt='planificacion_rt' in datos,
        re_estadistificacion='re_estadistificacion' in datos,
        sospecha_recidiva='sospecha_recidiva' in datos,
        sospecha_infeccion='sospecha_infeccion' in datos
    )

    db.session.add(nuevo_volante)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)



