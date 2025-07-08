# Imagen base de Python
FROM python:3.10-slim

# Crea un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que corre Flask
EXPOSE 5000

# Indicar el comando de arranque
CMD ["python", "backend/app.py"]
