# Użyj oficjalnego obrazu Python jako bazowego
FROM python:3.8-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj plik requirements.txt do katalogu roboczego
COPY requirements.txt .

# Zainstaluj zależności
RUN pip install -r requirements.txt

# Skopiuj resztę plików aplikacji do katalogu roboczego
COPY . .

# Eksponuj port, na którym aplikacja będzie działać
EXPOSE 5000

# Komenda do uruchomienia aplikacji
CMD ["python", "app.py"]
