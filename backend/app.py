import os
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from database import db
from models import User
from auth import auth_bp
from volantes import volantes_bp
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(basedir, '..', 'frontend', 'templates'),
    static_folder  =os.path.join(basedir, '..', 'frontend', 'static')
)

app.secret_key = 'mi_clave_super_secreta_12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volantes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Login manager
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# Base de datos
db.init_app(app)
with app.app_context():
    db.create_all()
    # Verificar si existe un administrador
    existente = User.query.filter_by(email='admin@example.com').first()
    if not existente:
        admin = User(
            username='admin',
            email='admin@example.com',
            role='administrador',
            activo=True,
            confirmado=True
        )
        admin.set_password('Admin123456.')
        db.session.add(admin)
        db.session.commit()
        print("Usuario administrador creado automáticamente.")
    else:
        print("El administrador ya existe. No se crea de nuevo.")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return redirect(url_for('volantes.menu'))

@app.context_processor
def inject_now():
    return {'now': datetime.now}

# Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(volantes_bp, url_prefix='/volante')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


