from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime




class Volante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creado_por = db.Column(db.Integer, db.ForeignKey('user.id'))
    fecha_creacion = db.Column(db.DateTime, default=datetime.now)

    editado_por = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    fecha_edicion = db.Column(db.DateTime, nullable=True)
    

    # Evaluación
    # Aquí debería poner algún campo relacionado con el paciente(nº historia, nombre y apellidos, etc) info mas concreta
    num_historia = db.Column(db.String(50), db.ForeignKey('paciente.num_historia'))
    Citado_por = db.Column(db.String(100))
    Fecha = db.Column(db.Date, nullable=True)
    Hora = db.Column(db.String(20))
    Habitacion = db.Column(db.String(50))
    Extension = db.Column(db.String(50))
    Enfermera = db.Column(db.String(100))
    Numero = db.Column(db.String(50))
    BOX = db.Column(db.String(50))

    # Antecedentes personales
    Diabetes = db.Column(db.Boolean)
    Renal = db.Column(db.Boolean)
    Alergia_yodo = db.Column(db.Boolean)
    Cardiopata = db.Column(db.Boolean)

    # Medicación actual
    Insulina = db.Column(db.Boolean)
    ADO = db.Column(db.Boolean)
    Antibioticos = db.Column(db.Boolean)
    Corticoides = db.Column(db.Boolean)

    # Motivo de exploración
    Estadificacion = db.Column(db.Boolean)
    Respuesta_a_tto = db.Column(db.Boolean)
    Control_evolutivo = db.Column(db.Boolean)
    TOD = db.Column(db.Boolean)

    # Motivo de exploración pt2
    Planificacion_RT = db.Column(db.Boolean)
    Re_Estadistificacion = db.Column(db.Boolean)
    Sospecha_Recidiva = db.Column(db.Boolean)
    Sospecha_Infeccion = db.Column(db.Boolean)

    # Estudios previos
    PET = db.Column(db.Date, nullable=True)
    TC = db.Column(db.Date, nullable=True)
    RMN = db.Column(db.Date, nullable=True)
    Otro4 = db.Column(db.Date, nullable=True)

    # Final del tratamiento previo
    Cirugia = db.Column(db.Date, nullable=True)
    RadioT = db.Column(db.Date, nullable=True)
    QuimioT = db.Column(db.Date, nullable=True)
    InmunoT = db.Column(db.Date, nullable=True)
    Otro = db.Column(db.Date, nullable=True)

    #Radiofarmaco
    F_FDG = db.Column(db.Boolean)
    F_Colina = db.Column(db.Boolean)
    F_FDOPA = db.Column(db.Boolean)
    F_PSMA = db.Column(db.Boolean)
    Amiloide = db.Column(db.Boolean)
    Ga_DOTATOC = db.Column(db.Boolean)
    

class User(UserMixin, db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email    = db.Column(db.String(120), unique=True, nullable=False)
    pwd_hash = db.Column(db.String(128), nullable=False)
    role     = db.Column(db.String(20), nullable=False)  # 'facultativo', 'enfermero', 'tecnico', 'administrador'
    activo   = db.Column(db.Boolean, default=False)  
    confirmado = db.Column(db.Boolean, default=False)
    ultimo_acceso = db.Column(db.DateTime, nullable=True)

    def set_password(self, pw):
        self.pwd_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.pwd_hash, pw)
    

class LogActividad(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    accion    = db.Column(db.String(255))
    fecha     = db.Column(db.DateTime, default=datetime.now)

    usuario   = db.relationship('User', backref='logs')


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(150), nullable=False)
    num_historia = db.Column(db.String(50), unique=True, nullable=False)

