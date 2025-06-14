from flask import Blueprint, render_template, request, redirect, flash, url_for, abort
from flask_login import login_required, current_user
from datetime import datetime
from database import db
from models import Volante, User, LogActividad, Paciente
import io
from flask import send_file, jsonify
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

    historia = datos.get('num_historia')

    paciente = Paciente.query.filter_by(num_historia=historia).first()
    if not paciente:
        flash('⚠️ El número de historia ingresado no está registrado.', 'danger')
        return render_template('index.html', modo='nuevo')
    

    v = Volante(
        num_historia=datos.get('num_historia'),
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
        Ga_DOTATOC='Ga_DOTATOC' in datos,
        Respiratorio = 'Respiratorio' in datos,
        Cardiaco = 'Cardiaco' in datos,
        Planificacion = 'Planificacion' in datos,
        EARL = 'EARL' in datos,
        Intravenoso = 'Intravenoso' in datos,
        CyC = 'CyC' in datos,
        Torax = 'Torax' in datos,
        Portal = 'Portal' in datos,
        Vasvular = 'Vasvular' in datos,
        Otro2 = datos.get('Otro2'),
        Oral = 'Oral' in datos,
        Rutina = 'Rutina' in datos,
        RutinaCraneo = 'RutinaCraneo' in datos,
        Entero = 'Entero' in datos,
        cyc1 = 'cyc1' in datos,
        Neuro = 'Neuro' in datos,
        Endocarditis = 'Endocarditis' in datos,
        ColinaPrecoz = 'ColinaPrecoz' in datos,
        ColinaTardia = 'ColinaTardia' in datos,
        Paratiroides = 'Paratiroides' in datos,
        y90 = 'y90' in datos,
        lu177 = 'lu177' in datos,
        eess = 'eess' in datos,
        adquisicionInicio = datos.get('adquisicionInicio'),
        adquisicionFinal = datos.get('adquisicionFinal'),
        tardiaInicio = datos.get('tardiaInicio'),
        tardiaFinal = datos.get('tardiaFinal'),
        Peso = datos.get('Peso'),
        Altura = datos.get('Altura'),
        embarazo_positivo = 'embarazo_positivo' in datos,
        embarazo_negativo = 'embarazo_negativo' in datos,
        informado_Contraste = 'embarazo_negativo' in datos,
        FUR = convertir_fecha(datos.get('FUR')),
        Glucemia_pre_inyeccion = datos.get('Glucemia_pre_inyeccion'),
        hora1 = datos.get('hora1'),
        Actrapid = 'Actrapid' in datos,
        Lorazepan_Diazepan = 'Lorazepan/Diazepan' in datos,
        Suero = 'Suero' in datos,
        otro_texto = datos.get('otro_texto'),
        DOSIS = datos.get('DOSIS'),
        inyeccion_izq = 'inyeccion_izq' in datos,
        inyeccion_dcha = 'inyeccion_dcha' in datos,
        Antecubital = 'Antecubital' in datos,
        Antebrazo = 'Antebrazo' in datos,
        Mano = 'Mano' in datos,
        Pie = 'Pie' in datos,
        otro3_texto = datos.get('otro3_texto'),
        Radiofarmaco = 'Radiofarmaco' in datos,
        contraste1 = 'contraste1' in datos,
        No_administrado_motivo = datos.get('No_administrado_motivo'),
        Extravasacion = 'Extravasacion' in datos,
        Reaccion_Alergica = 'Reaccion_Alergica' in datos,
        Intrarterial = 'Intrarterial' in datos,
        Malestar_general = 'Malestar_general' in datos,
        Sincope = 'Sincope' in datos,
        otro1_texto = datos.get('otro1_texto')


    )
    v.creado_por = current_user.id
    

    db.session.add(v)
    
    db.session.commit()
    # Registro en LogActividad
    log = LogActividad(
        usuario_id=current_user.id,
        accion=f"Creó volante con Nº Historia: {v.num_historia}"
    )
    db.session.add(log)
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
        historia = datos.get('num_historia')

        paciente = Paciente.query.filter_by(num_historia=historia).first()
        if not paciente:
            flash('⚠️ El número de historia ingresado no está registrado en pacientes.', 'danger')
            return render_template('index.html', volante=volante, modo='editar')
        
        volante.Citado_por       = datos.get('Citado_por')
        volante.num_historia     = historia
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
        volante.Respiratorio = 'Respiratorio' in datos
        volante.Cardiaco = 'Cardiaco' in datos
        volante.Planificacion = 'Planificacion' in datos
        volante.EARL = 'EARL' in datos
        volante.Intravenoso = 'Intravenoso' in datos
        volante.CyC = 'CyC' in datos
        volante.Torax = 'Torax' in datos
        volante.Portal = 'Portal' in datos
        volante.Vasvular = 'Vasvular' in datos
        volante.Otro2 = datos.get('Otro2')
        volante.Oral = 'Oral' in datos
        volante.Rutina = 'Rutina' in datos
        volante.RutinaCraneo = 'RutinaCraneo' in datos
        volante.Entero = 'Entero' in datos
        volante.cyc1 = 'cyc1' in datos
        volante.Neuro = 'Neuro' in datos
        volante.Endocarditis = 'Endocarditis' in datos
        volante.ColinaPrecoz = 'ColinaPrecoz' in datos
        volante.ColinaTardia = 'ColinaTardia' in datos
        volante.Paratiroides = 'Paratiroides' in datos
        volante.y90 = 'y90' in datos
        volante.lu177 = 'lu177' in datos
        volante.eess = 'eess' in datos
        volante.adquisicionInicio = datos.get('adquisicionInicio')
        volante.adquisicionFinal = datos.get('adquisicionFinal')
        volante.tardiaInicio = datos.get('tardiaInicio')
        volante.tardiaFinal = datos.get('tardiaFinal')
        volante.Peso = datos.get('Peso')
        volante.Altura = datos.get('Altura')
        volante.embarazo_positivo = 'embarazo_positivo' in datos
        volante.embarazo_negativo = 'embarazo_negativo' in datos
        volante.informado_Contraste = datos.get('informado_Contraste')
        volante.FUR = convertir_fecha(datos.get('FUR'))
        volante.Glucemia_pre_inyeccion = datos.get('Glucemia_pre_inyeccion')
        volante.hora1 = datos.get('hora1')
        volante.Actrapid = 'Actrapid' in datos
        volante.Lorazepan_Diazepan = 'Lorazepan_Diazepan' in datos
        volante.Suero = 'Suero' in datos
        volante.otro_texto = datos.get('otro_texto')
        volante.DOSIS = datos.get('DOSIS')
        volante.inyeccion_izq = 'inyeccion_izq' in datos
        volante.inyeccion_dcha = 'inyeccion_dcha' in datos
        volante.Antecubital = 'Antecubital' in datos
        volante.Antebrazo = 'Antebrazo' in datos
        volante.Mano = 'Mano' in datos
        volante.Pie = 'Pie' in datos
        volante.otro3_texto = datos.get('otro3_texto')
        volante.Radiofarmaco = 'Radiofarmaco' in datos
        volante.contraste1 = 'contraste1' in datos
        volante.No_administrado_motivo = datos.get('No_administrado_motivo')
        volante.Extravasacion = 'Extravasacion' in datos
        volante.Reaccion_Alergica = 'Reaccion_Alergica' in datos
        volante.Intrarterial = 'Intrarterial' in datos
        volante.Malestar_general = 'Malestar_general' in datos
        volante.Sincope = 'Sincope' in datos
        volante.otro1_texto = datos.get('otro1_texto')


        volante.editado_por = current_user.id
        volante.fecha_edicion = datetime.now()
        


        db.session.commit()
        # registrar edición
        log = LogActividad(usuario_id=current_user.id, accion=f"Editó volante con Nº Historia: {volante.num_historia}")
        db.session.add(log)
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
            'Ga_DOTATOC': v.Ga_DOTATOC,
            'Respiratorio': v.Respiratorio,
            'Cardiaco': v.Cardiaco,
            'Planificacion': v.Planificacion,
            'EARL': v.EARL,
            'Intravenoso': v.Intravenoso,
            'CyC': v.CyC,
            'Torax': v.Torax,
            'Portal': v.Portal,
            'Vasvular': v.Vasvular,
            'Otro2': v.Otro2,
            'Oral': v.Oral,
            'Rutina': v.Rutina,
            'RutinaCraneo': v.RutinaCraneo,
            'Entero': v.Entero,
            'cyc1': v.cyc1,
            'Neuro': v.Neuro,
            'Endocarditis': v.Endocarditis,
            'ColinaPrecoz': v.ColinaPrecoz,
            'ColinaTardia': v.ColinaTardia,
            'Paratiroides': v.Paratiroides,
            'y90': v.y90,
            'lu177': v.lu177,
            'eess': v.eess,
            'adquisicionInicio': v.adquisicionInicio,
            'adquisicionFinal': v.adquisicionFinal,
            'tardiaInicio': v.tardiaInicio,
            'tardiaFinal': v.tardiaFinal,
            'Peso': v.Peso,
            'Altura': v.Altura,
            'embarazo_positivo': v.embarazo_positivo,
            'embarazo_negativo': v.embarazo_negativo,
            'informado_Contraste': v.informado_Contraste,
            'FUR': v.FUR,
            'Glucemia_pre_inyeccion': v.Glucemia_pre_inyeccion,
            'hora1': v.hora1,
            'Actrapid': v.Actrapid,
            'Lorazepan/Diazepan': v.Lorazepan/Diazepan,
            'Suero': v.Suero,
            'otro_texto': v.otro_texto,
            'DOSIS': v.DOSIS,
            'inyeccion_izq': v.inyeccion_izq,
            'inyeccion_dcha': v.inyeccion_dcha,
            'Antecubital': v.Antecubital,
            'Antebrazo': v.Antebrazo,
            'Mano': v.Mano,
            'Pie': v.Pie,
            'otro3_texto': v.otro3_texto,
            'Radiofarmaco': v.Radiofarmaco,
            'contraste1': v.contraste1,
            'No_administrado_motivo': v.No_administrado_motivo,
            'Extravasacion': v.Extravasacion,
            'Reaccion_Alergica': v.Reaccion_Alergica,
            'Intrarterial': v.Intrarterial,
            'Malestar_general': v.Malestar_general,
            'Sincope': v.Sincope,
            'otro1_texto': v.otro1_texto
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
    if current_user.role not in ['facultativo', 'administrador']:
        abort(403)
    users = User.query.all()
    return render_template('gestion_users.html', users=users)

@volantes_bp.route('/users/<int:id>/delete', methods=['POST'])
@login_required
def delete_user(id):
    if current_user.role not in ['facultativo', 'administrador']:
        abort(403)
    
    u = User.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()

    # Registrar eliminación
    log = LogActividad(
        usuario_id=current_user.id,
        accion=f"Eliminó al usuario con ID {u.id} y nombre '{u.username}'"
    )
    db.session.add(log)
    db.session.commit()

    flash('Usuario eliminado 🗑️', 'warning')
    return redirect(url_for('volantes.gestion_usuarios'))





@volantes_bp.route('/users/pendientes')
@login_required
def ver_pendientes():
    if current_user.role != 'administrador':
        abort(403)
    pendientes = User.query.filter_by(confirmado=False).all()
    return render_template('pendientes.html', users=pendientes)

@volantes_bp.route('/users/<int:id>/aprobar', methods=['POST'])
@login_required
def aprobar_usuario(id):
    if current_user.role != 'administrador':
        abort(403)
    u = User.query.get_or_404(id)
    u.confirmado = True
    u.activo = True
    db.session.commit()
    flash(f'Usuario {u.username} confirmado ✅', 'success')
    return redirect(url_for('volantes.ver_pendientes'))

@volantes_bp.route('/users/<int:id>/cancelar', methods=['POST'])
@login_required
def cancelar_usuario(id):
    if current_user.role != 'administrador':
        abort(403)
    u = User.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    flash(f'Registro de {u.username} cancelado ❌', 'danger')
    return redirect(url_for('volantes.ver_pendientes'))


@volantes_bp.route('/logs')
@login_required
def ver_logs():
    if current_user.role != 'administrador':
        abort(403)
    logs = LogActividad.query.order_by(LogActividad.fecha.desc()).all()
    return render_template('logs.html', logs=logs)


@volantes_bp.route('/users/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def editar_usuario(id):
    if current_user.role != 'administrador':
        abort(403)

    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.role = request.form['role']

        nueva_pw = request.form.get('password')
        if nueva_pw:
            user.set_password(nueva_pw)

        db.session.commit()
        flash(f'Usuario {user.username} actualizado ✅', 'success')
        return redirect(url_for('volantes.gestion_usuarios'))

    return render_template('editar_usuario.html', user=user)


@volantes_bp.route('/paciente/nuevo', methods=['GET', 'POST'])
@login_required
def alta_paciente():
    if current_user.role not in ['administrador', 'facultativo']:
        abort(403)

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        historia = request.form['num_historia']

        existente = Paciente.query.filter_by(num_historia=historia).first()
        if existente:
            flash('⚠️ Ya existe un paciente con ese número de historia.', 'danger')
            return redirect(url_for('volantes.alta_paciente'))

        p = Paciente(nombre=nombre, apellidos=apellidos, num_historia=historia)
        db.session.add(p)
        db.session.commit()
        flash('Paciente registrado ✅', 'success')
        return redirect(url_for('volantes.menu'))

    return render_template('alta_paciente.html')

@volantes_bp.route('/verificar_historia')
def verificar_historia():
    num = request.args.get('valor', '').strip()

    if not num:
        return jsonify({'existe': False})

    paciente = db.session.query(Paciente).filter(Paciente.num_historia == num).first()

    if paciente:
        return jsonify({
            'existe': True,
            'nombre': paciente.nombre,
            'apellidos': paciente.apellidos
        })
    else:
        return jsonify({'existe': False})



@volantes_bp.route('/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_volante(id):
    volante = Volante.query.get_or_404(id)
    db.session.delete(volante)
    db.session.commit()

    # Log de actividad
    log = LogActividad(usuario_id=current_user.id, accion=f"Eliminó volante con Nº Historia {volante.num_historia}")
    db.session.add(log)
    db.session.commit()

    flash('Volante eliminado con éxito', 'warning')
    return redirect(url_for('volantes.bandeja'))

@volantes_bp.route('/users/<int:id>/toggle_estado', methods=['POST'])
@login_required
def toggle_estado_usuario(id):
    if current_user.role != 'administrador':
        abort(403)

    user = User.query.get_or_404(id)
    user.activo = not user.activo
    db.session.commit()

    estado = "activado" if user.activo else "desactivado"
    flash(f"Usuario {user.username} ha sido {estado}.", "info")
    return redirect(url_for('volantes.gestion_usuarios'))

