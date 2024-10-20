# Usa una imagen base de Python
FROM python:3.9-slim

# Crea el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos al contenedor
COPY . /app

# Instala las dependencias
RUN pip install -r requirements.txt

# Ejecuta el script principal
CMD ["python", "src/model.py"]