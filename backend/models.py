from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship




class Volante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creado_por = db.Column(db.Integer, db.ForeignKey('user.id'))
    fecha_creacion = db.Column(db.DateTime, default=datetime.now)

    editado_por = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    fecha_edicion = db.Column(db.DateTime, nullable=True)
    

    # Evaluación
    num_historia = db.Column(db.String(50), db.ForeignKey('paciente.num_historia'))
    Citado_por = db.Column(db.String(100))
    Fecha = db.Column(db.Date, nullable=True)
    Hora = db.Column(db.String(20))
    Historia_Clinica = db.Column(db.String(500))
    Dieta_ENDOCARDITIS = db.Column(db.Boolean, default=False)
    Adelantar_si_se_puede = db.Column(db.Boolean, default=False)
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
    Re_Estadificacion = db.Column(db.Boolean)
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

    # Técnicos
    Respiratorio = db.Column(db.Boolean)
    Cardiaco = db.Column(db.Boolean)
    Planificacion = db.Column(db.Boolean)
    EARL = db.Column(db.Boolean)

    # Contraste
    Intravenoso = db.Column(db.Boolean)
    CyC = db.Column(db.Boolean)
    Torax = db.Column(db.Boolean)
    Portal = db.Column(db.Boolean)
    Vasvular = db.Column(db.Boolean)
    Otro2 = db.Column(db.String(50))
    Oral = db.Column(db.Boolean)

    # Protocolo
    Rutina = db.Column(db.Boolean)
    RutinaCraneo = db.Column(db.Boolean)
    Entero = db.Column(db.Boolean)
    cyc1 = db.Column(db.Boolean)
    Neuro = db.Column(db.Boolean)
    Endocarditis = db.Column(db.Boolean)
    ColinaPrecoz = db.Column(db.Boolean)
    ColinaTardia = db.Column(db.Boolean)
    Paratiroides = db.Column(db.Boolean)
    y90 = db.Column(db.Boolean)
    lu177 = db.Column(db.Boolean)
    eess = db.Column(db.Boolean)

    # Hora de adquisición
    adquisicionInicio = db.Column(db.String(10))
    adquisicionFinal = db.Column(db.String(10))

    # Tardía
    tardiaInicio = db.Column(db.String(10))
    tardiaFinal = db.Column(db.String(10))

    # Enfermería
    Peso = db.Column(db.Float)
    Altura = db.Column(db.Float)
    embarazo_positivo = db.Column(db.Boolean)
    embarazo_negativo = db.Column(db.Boolean)
    informado_Contraste = db.Column(db.String(200))
    FUR = db.Column(db.Date)
    Glucemia_pre_inyeccion = db.Column(db.String(200))
    hora1 = db.Column(db.String(10))
    Actrapid = db.Column(db.Boolean)
    Lorazepan_Diazepan = db.Column(db.Boolean)
    Suero = db.Column(db.Boolean)
    otro_texto = db.Column(db.String(200))
    DOSIS = db.Column(db.String(100))

    inyeccion_izq = db.Column(db.Boolean)
    inyeccion_dcha = db.Column(db.Boolean)
    Antecubital = db.Column(db.Boolean)
    Antebrazo = db.Column(db.Boolean)
    Mano = db.Column(db.Boolean)
    Pie = db.Column(db.Boolean)
    otro3_texto = db.Column(db.String(200))

    # Incidencias
    Radiofarmaco = db.Column(db.Boolean)
    contraste1 = db.Column(db.Boolean)
    No_administrado_motivo = db.Column(db.String(200))
    Extravasacion = db.Column(db.Boolean)
    Reaccion_Alergica = db.Column(db.Boolean)
    Intrarterial = db.Column(db.Boolean)
    Malestar_general = db.Column(db.Boolean)
    Sincope = db.Column(db.Boolean)
    otro1_texto = db.Column(db.String(200))

    paciente = db.relationship('Paciente', backref='volantes', lazy=True)


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
    __tablename__ = 'paciente'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(150), nullable=False)
    num_historia = db.Column(db.String(50), unique=True, nullable=False)

