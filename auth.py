from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required
from models import User, LogActividad
from database import db
from datetime import datetime


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        u = User(
            username=request.form['username'],
            email   =request.form['email'],
            role    =request.form['role'],
            activo  =False  # ← Usuario queda pendiente de activación
        )
        u.set_password(request.form['password'])
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
            db.session.commit()

            return redirect(url_for('volantes.menu'))

        flash('Credenciales inválidas', 'danger')

    return render_template('auth/login.html')




@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión abierta con éxito', 'info')
    return redirect(url_for('auth.login'))
