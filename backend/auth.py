from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import User, LogActividad
from database import db
from datetime import datetime
import re



auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email    = request.form['email']
        role     = request.form['role']
        password = request.form['password']
        password1 = request.form['password1']

        # Validación: comprobar que coinciden las contraseñas
        if password != password1:
            flash('❌ Las contraseñas no coinciden.', 'danger')
            return redirect(url_for('auth.register'))

        # Validación: longitud, mayúscula, símbolo especial
        if (
            len(password) < 12 or
            not re.search(r'[A-Z]', password) or
            not re.search(r'[.,_*\+\-\^¨!¿?¡;:]', password)
        ):
            flash('⚠️ La contraseña debe tener al menos 12 caracteres, una letra mayúscula y un símbolo especial (. , _ * + - ^ ¨ ! ¿ ? ¡ ; :)', 'danger')
            return redirect(url_for('auth.register'))
        
        # Validar si el nombre de usuario ya existe
        existente = User.query.filter_by(username=username).first()
        if existente:
            flash('⚠️ El nombre de usuario ya está registrado. Por favor elige otro.', 'danger')
            return redirect(url_for('auth.register'))
        
        existente_email = User.query.filter_by(email=email).first()
        if existente_email:
            flash('⚠️ El correo electrónico ya está registrado. Usa otro.', 'danger')
            return redirect(url_for('auth.register'))
        # Crear usuario si todo es correcto
        u = User(
            username=username,
            email=email,
            role=role,
            activo=False  # Usuario pendiente de aprobación
        )
        u.set_password(password)


        db.session.add(u)
        db.session.commit()

        flash('Registro enviado. Pendiente de aprobación por el administrador.', 'info')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')




@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = User.query.filter_by(username=request.form['username']).first()
        if u and u.check_password(request.form['password']):

            if not u.confirmado:
                flash('Tu cuenta está pendiente de aprobación por el administrador.', 'warning')
                return redirect(url_for('auth.login'))

            if not u.activo:
                flash('Tu cuenta está desactivada. Contacta con el administrador.', 'danger')
                return redirect(url_for('auth.login'))

            login_user(u)
            u.ultimo_acceso = datetime.utcnow()

            log = LogActividad(usuario_id=u.id, accion="Inicio de sesión")
            db.session.add(log)
            flash('Sesión abierta con éxito', 'success')
            db.session.commit()

            return redirect(url_for('volantes.menu'))

        flash('Credenciales inválidas', 'danger')

    return render_template('auth/login.html')




@auth_bp.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        log = LogActividad(
            usuario_id=current_user.id,
            accion=f"Cerró sesión"
        )
        db.session.add(log)
        db.session.commit()

    logout_user()
    flash("Sesión cerrada correctamente", "info")
    return redirect(url_for('auth.login'))

