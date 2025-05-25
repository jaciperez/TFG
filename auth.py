from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required
from models import User
from database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        u = User(
            username=request.form['username'],
            email   =request.form['email'],
            role    =request.form['role']
        )
        u.set_password(request.form['password'])
        db.session.add(u)
        db.session.commit()
        flash('Usuario registrado', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = User.query.filter_by(username=request.form['username']).first()
        if u and u.check_password(request.form['password']):
            login_user(u)
            return redirect(url_for('volantes.menu'))
        flash('Credenciales inválidas', 'danger')
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión abierta con éxito', 'info')
    return redirect(url_for('auth.login'))
