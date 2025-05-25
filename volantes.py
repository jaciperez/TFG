from flask import Blueprint, render_template, request, redirect, flash, url_for, abort
from flask_login import login_required, current_user
from datetime import datetime
from database import db
from models import Volante, User
import io
from flask import send_file
import pandas as pd
from sqlalchemy.orm import aliased


volantes_bp = Blueprint('volantes', __name__)

def convertir_fecha(str_fecha):
    return datetime.strptime(str_fecha, "%Y-%m-%d").date() if str_fecha else None

@volantes_bp.route('/', methods=['GET'])
@login_required
def menu():
    # aquí le pasamos al template el objeto current_user
    return render_template('menu.html', user=current_user)

@volantes_bp.route('/nuevo', methods=['GET'])
@login_required
def nuevo_volante():
    return render_template('index.html', volante=None, modo='crear')

@volantes_bp.route('/guardar', methods=['POST'])
@login_required
def guardar_volante():
    datos = request.form

    v = Volante(
        Citado_por=datos.get('Citado_por'),
        Fecha=convertir_fecha(datos.get('Fecha')),
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
        PET=convertir_fecha(datos.get('PET')),
        TC=convertir_fecha(datos.get('TC')),
        RMN=convertir_fecha(datos.get('RMN')),
        Otro4=convertir_fecha(datos.get('Otro4')),
        Cirugia=convertir_fecha(datos.get('Cirugia')),
        RadioT=convertir_fecha(datos.get('RadioT')),
        QuimioT=convertir_fecha(datos.get('QuimioT')),
        InmunoT=convertir_fecha(datos.get('InmunoT')),
        Otro=convertir_fecha(datos.get('Otro')),
        F_FDG='F_FDG' in datos,
        F_Colina='F_Colina' in datos,
        F_FDOPA='F_FDOPA' in datos,
        F_PSMA='F_PSMA' in datos,
        Amiloide='Amiloide' in datos,
        Ga_DOTATOC='Ga_DOTATOC' in datos

        

    )
    v.creado_por = current_user.id
    db.session.add(v)
    
    db.session.commit()
    flash('Volante guardado ✅', 'success')
    return redirect(url_for('volantes.bandeja'))

from sqlalchemy.orm import aliased

@volantes_bp.route('/bandeja', methods=['GET'])
@login_required
def bandeja():
    creador = aliased(User)
    editor = aliased(User)

    volantes = db.session.query(Volante, creador, editor)\
        .outerjoin(creador, Volante.creado_por == creador.id)\
        .outerjoin(editor, Volante.editado_por == editor.id)\
        .all()

    # formatear lista con acceso directo a creador/editor
    resultado = []
    for v, creador_obj, editor_obj in volantes:
        v.creador = creador_obj
        v.editor = editor_obj
        resultado.append(v)

    return render_template('bandeja.html', volantes=resultado)


@volantes_bp.route('/calendario')
@login_required
def calendario():
    volantes = Volante.query.filter(Volante.Fecha != None).all()

    eventos = {}
    for v in volantes:
        fecha_str = v.Fecha.strftime("%Y-%m-%d")
        if fecha_str not in eventos:
            eventos[fecha_str] = []
        eventos[fecha_str].append(v.Citado_por or "Sin nombre")

    return render_template('calendario.html', eventos=eventos)


@volantes_bp.route('/<int:id>/edit', methods=['GET','POST'])
@login_required
def editar_volante(id):
    volante = Volante.query.get_or_404(id)
    if request.method == 'POST':
        datos = request.form
        volante.Citado_por       = datos.get('Citado_por')
        volante.Fecha            = convertir_fecha(datos.get('Fecha'))
        volante.Hora             = datos.get('Hora')
        volante.Habitacion       = datos.get('Habitacion')
        volante.Extension        = datos.get('Extension')
        volante.Enfermera        = datos.get('Enfermera')
        volante.Numero           = datos.get('Numero')
        volante.BOX              = datos.get('BOX')
        volante.Diabetes         = 'Diabetes' in datos
        volante.Renal            = 'Renal' in datos
        volante.Alergia_yodo     = 'Alergia_yodo' in datos
        volante.Cardiopata       = 'Cardiopata' in datos
        volante.Insulina         = 'Insulina' in datos
        volante.ADO              = 'ADO' in datos
        volante.Antibioticos     = 'Antibioticos' in datos
        volante.Corticoides      = 'Corticoides' in datos
        volante.Estadificacion   = 'Estadificacion' in datos
        volante.Respuesta_a_tto  = 'Respuesta_a_tto' in datos
        volante.Control_evolutivo= 'Control_evolutivo' in datos
        volante.TOD              = 'TOD' in datos
        volante.Planificacion_RT = 'Planificacion_RT' in datos
        volante.Re_Estadistificacion = 'Re_Estadistificacion' in datos
        volante.Sospecha_Recidiva    = 'Sospecha_Recidiva' in datos
        volante.Sospecha_Infeccion   = 'Sospecha_Infeccion' in datos
        volante.PET              = convertir_fecha(datos.get('PET'))
        volante.TC               = convertir_fecha(datos.get('TC'))
        volante.RMN              = convertir_fecha(datos.get('RMN'))
        volante.Otro4            = convertir_fecha(datos.get('Otro4'))
        volante.Cirugia          = convertir_fecha(datos.get('Cirugia'))
        volante.RadioT           = convertir_fecha(datos.get('RadioT'))
        volante.QuimioT          = convertir_fecha(datos.get('QuimioT'))
        volante.InmunoT          = convertir_fecha(datos.get('InmunoT'))
        volante.Otro             = convertir_fecha(datos.get('Otro'))
        volante.F_FDG            = 'F_FDG' in datos
        volante.F_Colina         = 'F_Colina' in datos
        volante.F_FDOPA          = 'F_FDOPA' in datos
        volante.F_PSMA           = 'F_PSMA' in datos
        volante.Amiloide         = 'Amiloide' in datos
        volante.Ga_DOTATOC       = 'Ga_DOTATOC' in datos

        volante.editado_por = current_user.id
        volante.fecha_edicion = datetime.now()

        db.session.commit()
        flash('Volante actualizado ✅', 'success')
        return redirect(url_for('volantes.bandeja'))

    
    return render_template('index.html', volante=volante, modo='editar')



@volantes_bp.route('/exportar_excel')
@login_required
def exportar_excel():
    volantes = Volante.query.all()

    # Convertir a lista de diccionarios
    data = []
    for v in volantes:
        data.append({
            'ID': v.id,
            'Citado_por': v.Citado_por,
            'Fecha': v.Fecha,
            'Hora': v.Hora,
            'Habitacion': v.Habitacion,
            'Extension': v.Extension,
            'Enfermera': v.Enfermera,
            'Numero': v.Numero,
            'BOX': v.BOX,
            'Diabetes': v.Diabetes,
            'Renal': v.Renal,
            'Alergia_yodo': v.Alergia_yodo,
            'Cardiopata': v.Cardiopata,
            'Insulina': v.Insulina,
            'ADO': v.ADO,
            'Antibioticos': v.Antibioticos,
            'Corticoides': v.Corticoides,
            'Estadificacion': v.Estadificacion,
            'Respuesta_a_tto': v.Respuesta_a_tto,
            'Control_evolutivo': v.Control_evolutivo,
            'TOD': v.TOD,
            'Planificacion_RT': v.Planificacion_RT,
            'Re_Estadistificacion': v.Re_Estadistificacion,
            'Sospecha_Recidiva': v.Sospecha_Recidiva,
            'Sospecha_Infeccion': v.Sospecha_Infeccion,
            'PET': v.PET,
            'TC': v.TC,
            'RMN': v.RMN,
            'Otro4': v.Otro4,
            'Cirugia': v.Cirugia,
            'RadioT': v.RadioT,
            'QuimioT': v.QuimioT,
            'InmunoT': v.InmunoT,
            'Otro': v.Otro,
            'F_FDG': v.F_FDG,
            'F_Colina': v.F_Colina,
            'F_FDOPA': v.F_FDOPA,
            'F_PSMA': v.F_PSMA,
            'Amiloide': v.Amiloide,
            'Ga_DOTATOC': v.Ga_DOTATOC
        })

    df = pd.DataFrame(data)

    for col in df.select_dtypes(include=bool).columns:
        df[col] = df[col].map({True: "Sí", False: "No"})

    # Crear Excel en memoria
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Volantes')

    # Ajustar el ancho de columnas automáticamente
        workbook  = writer.book
        worksheet = writer.sheets['Volantes']
    
        for i, col in enumerate(df.columns):
            max_len = max(
                df[col].astype(str).map(len).max(),
                len(col)
            )
            worksheet.set_column(i, i, max_len + 2)
        

    output.seek(0)

    return send_file(
        output,
        as_attachment=True,
        download_name='volantes.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


# Gestión de usuarios
@volantes_bp.route('/users', methods=['GET'])
@login_required
def gestion_usuarios():
    if current_user.role != 'facultativo':
        abort(403)
    users = User.query.all()
    return render_template('gestion_users.html', users=users)

@volantes_bp.route('/users/<int:id>/delete', methods=['POST'])
@login_required
def delete_user(id):
    if current_user.role != 'facultativo':
        abort(403)
    u = User.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    flash('Usuario eliminado 🗑️', 'warning')
    return redirect(url_for('volantes.gestion_usuarios'))


