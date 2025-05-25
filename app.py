import os
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from database import db
from models import User
from auth import auth_bp
from volantes import volantes_bp

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(basedir, '..', 'frotend', 'templates'),
    static_folder  =os.path.join(basedir, '..', 'frotend', 'static')
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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    # si no estás logueado, te lleva al login
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    # si ya iniciaste sesión, al menú de volantes
    return redirect(url_for('volantes.menu'))




# Registramos blueprints
app.register_blueprint(auth_bp,    url_prefix='/auth')
app.register_blueprint(volantes_bp, url_prefix='/volante')

if __name__ == '__main__':
    app.run(debug=True)





