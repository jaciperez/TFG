from app import app, db
from models import User

with app.app_context():
    # Verificamos si ya existe un usuario admin
    existente = User.query.filter_by(email='admin@example.com').first()

    if existente:
        print("⚠️ Ya existe un administrador con ese email.")
    else:
        admin = User(
            username='admin',
            email='admin@example.com',
            role='administrador',
            activo=True,
            confirmado=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("✅ Usuario administrador creado correctamente.")


