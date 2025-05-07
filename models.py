from database import db

class Volante(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Evaluación
    # Aquí debería poner algún campo relacionado con el paciente(nº historia, nombre y apellidos, etc) info mas concreta
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
    
