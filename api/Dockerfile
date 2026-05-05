# 1 image de base
FROM python:3.11-slim

# 2 copie et installation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3 copie code source
COPY app.py .
COPY test_app.py .

# 4 exposition du port
EXPOSE 5000

# 5 commande démarrage de l'application
CMD ["python", "app.py"]

