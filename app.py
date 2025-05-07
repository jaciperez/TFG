
from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request, redirect, flash, get_flashed_messages

from database import db
from models import Volante
import os
from datetime import datetime

# Creamos la app primero
app = Flask(__name__)
app.secret_key = 'mi_clave_super_secreta_12345'

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

@app.route('/bandeja')
def bandeja():
    volantes = Volante.query.all()
    return render_template('bandeja.html', volantes=volantes)


# donde se guardan los datos del formulario en la base de datos
@app.route('/guardar_volante', methods=['POST'])
def guardar_volante():
    datos = request.form

    def convertir_fecha(campo):
        valor = datos.get(campo)
        return datetime.strptime(valor, "%Y-%m-%d").date() if valor else None
    
    nuevo_volante = Volante(
        Citado_por=datos.get('Citado_por'),
        Fecha = convertir_fecha('Fecha'),
        Hora=datos.get('Hora'),
        Habitacion=datos.get('Habitacion'),
        Extension=datos.get('Extension'),
        Enfermera=datos.get('Enfermera'),
        Numero=datos.get('Numero'),
        BOX=datos.get('BOX'),

        Diabetes='Diabetes' in datos,
        Renal='Renal' in datos,
        Alergia_yodo='Alergia_yodo' in datos,
        Cardiopata='Cardiopata' in datos,

        Insulina='Insulina' in datos,
        ADO='ADO' in datos,
        Antibioticos='Antibioticos' in datos,
        Corticoides='Corticoides' in datos,

        Estadificacion='Estadificacion' in datos,
        Respuesta_a_tto='Respuesta_a_tto' in datos,
        Control_evolutivo='Control_evolutivo' in datos,
        TOD='TOD' in datos,

        Planificacion_RT='Planificacion_RT' in datos,
        Re_Estadistificacion='Re_Estadistificacion' in datos,
        Sospecha_Recidiva='Sospecha_Recidiva' in datos,
        Sospecha_Infeccion='Sospecha_Infeccion' in datos,

        PET=convertir_fecha('PET'),
        TC=convertir_fecha('TC'),
        RMN=convertir_fecha('RMN'),
        Otro4=convertir_fecha('Otro4'),

        Cirugia=convertir_fecha('Cirugia'),
        RadioT=convertir_fecha('RadioT'),
        QuimioT=convertir_fecha('QuimioT'),
        InmunoT=convertir_fecha('InmunoT'),
        Otro=convertir_fecha('Otro'),

        F_FDG='F_FDG' in datos,
        F_Colina='F_Colina' in datos,
        F_FDOPA='F_FDOPA' in datos,
        F_PSMA='F_PSMA' in datos,
        Amiloide='Amiloide' in datos,
        Ga_DOTATOC='Ga_DOTATOC' in datos 


    )

    db.session.add(nuevo_volante)
    db.session.commit()

    flash('Volante guardado en la base de datos correctamente ✅')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)



