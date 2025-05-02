from database import db

class Volante(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Evaluación
    citado = db.Column(db.String(100))
    fecha = db.Column(db.String(20))
    hora = db.Column(db.String(20))
    hab = db.Column(db.String(50))
    ext = db.Column(db.String(50))
    enfermera = db.Column(db.String(100))
    numero = db.Column(db.String(50))
    box = db.Column(db.String(50))

    # Antecedentes personales
    diabetes = db.Column(db.Boolean)
    renal = db.Column(db.Boolean)
    alergia_yodo = db.Column(db.Boolean)
    cardiopata = db.Column(db.Boolean)

    # Medicación actual
    insulina = db.Column(db.Boolean)
    ADO = db.Column(db.Boolean)
    antibioticos = db.Column(db.Boolean)
    corticoides = db.Column(db.Boolean)

    # Motivo de exploración
    estadificacion = db.Column(db.Boolean)
    respuesta_a_tto = db.Column(db.Boolean)
    control_evolutivo = db.Column(db.Boolean)
    TOD = db.Column(db.Boolean)

    # Motivo de exploración pt2
    planificacion_rt = db.Column(db.Boolean)
    re_estadistificacion = db.Column(db.Boolean)
    sospecha_recidiva = db.Column(db.Boolean)
    sospecha_infeccion = db.Column(db.Boolean)

