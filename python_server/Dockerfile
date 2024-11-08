FROM python:3.9-slim

WORKDIR /usr/src/app

# Instalacja pakietów systemowych
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Kopiowanie pliku requirements.txt i instalacja zależności Pythona
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie skryptu aplikacji
COPY app.py .

EXPOSE 5000

# Uruchomienie aplikacji
CMD ["python", "./app.py"]
