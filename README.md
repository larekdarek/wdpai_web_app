# Wdpai Web App

## Opis projektu

Wdpai Web App to aplikacja webowa stworzona w ramach zajęć **Wstępu do Projektowania Aplikacji Internetowych**. Aplikacja umożliwia zarządzanie członkami zespołu poprzez interfejs webowy. Technologia backendowa opiera się na Flasku i bazie danych PostgreSQL, a całość jest uruchamiana w kontenerach Docker przy użyciu Docker Compose.

## Funkcjonalności

- **Wyświetlanie listy członków zespołu**: Pobieranie danych z bazy danych PostgreSQL i wyświetlanie ich na stronie.
- **Dodawanie nowych członków zespołu**: Możliwość dodania nowej osoby poprzez formularz.
- **Usuwanie członków zespołu**: Usuwanie wybranej osoby z bazy danych.
- **Interfejs użytkownika**: Przyjazny i responsywny interfejs stworzony przy użyciu HTML, CSS i JavaScript.
- **API REST**: Backend udostępnia API do komunikacji z frontendem.

## Technologia

- **Backend**: Python 3.9, Flask, psycopg2
- **Baza danych**: PostgreSQL 13
- **Frontend**: HTML5, CSS3, JavaScript
- **Serwer webowy**: Nginx
- **Konteneryzacja**: Docker, Docker Compose

## Wymagania

- Docker (wersja 20.x lub nowsza)
- Docker Compose (wersja 1.27 lub nowsza)

## Instalacja i uruchomienie

1. **Sklonuj repozytorium:**

   ```bash
   git clone https://github.com/larekdarek/wdpai_web_app.git
   cd wdpai_web_app
   ```

2. **Uruchomienie aplikacji:**

   W katalogu głównym projektu wykonaj:

   ```bash
   docker-compose up --build
   ```

   Polecenie to zbuduje obrazy Dockerowe i uruchomi kontenery dla wszystkich usług.

3. **Dostęp do aplikacji:**

   - **Frontend**: Otwórz przeglądarkę i przejdź do [http://localhost:8080](http://localhost:8080)
   - **pgAdmin**: Dostępny pod adresem [http://localhost:5050](http://localhost:5050)
     - **Email**: `admin@admin.com`
     - **Hasło**: `admin`

## Struktura projektu

- `nginx/` - konfiguracja i pliki dla serwera Nginx
  - `default.conf` - plik konfiguracyjny Nginx
- `python_server/` - kod aplikacji backendowej
  - `app.py` - główny plik aplikacji Flask
  - `requirements.txt` - zależności Pythona
  - `Dockerfile` - plik do budowy obrazu Dockera dla aplikacji Python
- `postgres_init/` - skrypty inicjalizacyjne dla bazy danych PostgreSQL
  - `init.sql` - skrypt SQL tworzący tabelę i wstawiający dane początkowe
- `docker-compose.yml` - definicja usług Docker Compose
- `README.md` - ten plik

## Użycie

### Dodawanie nowego członka zespołu

1. Otwórz aplikację w przeglądarce pod adresem [http://localhost:8080](http://localhost:8080).
2. Wypełnij formularz dodawania członka zespołu.
3. Kliknij przycisk **SUBMIT**.
4. Nowy członek pojawi się na liście poniżej formularza.

### Usuwanie członka zespołu

- Kliknij ikonę usuwania obok wybranego członka zespołu na liście.

### API

- **GET `/api/team`** - pobiera listę członków zespołu.
- **POST `/api/team`** - dodaje nowego członka zespołu.
- **DELETE `/api/team/<id>`** - usuwa członka zespołu o podanym `id`.

## Testowanie API za pomocą cURL

- **Pobranie listy członków:**

  ```bash
  curl http://localhost:8080/api/team
  ```

- **Dodanie nowego członka:**

  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"firstName":"Jan","lastName":"Kowalski","role":"Developer"}' \
  http://localhost:8080/api/team
  ```

- **Usunięcie członka o `id` równym 1:**

  ```bash
  curl -X DELETE http://localhost:8080/api/team/1
  ```

## Konfiguracja pgAdmin

1. Otwórz pgAdmin pod adresem [http://localhost:5050](http://localhost:5050).
2. Zaloguj się używając podanych wyżej danych.
3. Dodaj nowy serwer:
   - **Name**: Dowolna nazwa, np. `Postgres`
   - **Connection**:
     - **Host name/address**: `postgres`
     - **Port**: `5432`
     - **Maintenance database**: `mydatabase`
     - **Username**: `myuser`
     - **Password**: `mypassword`
4. Połącz się i przeglądaj bazę danych.

## Zmienne środowiskowe

Zmienne środowiskowe są zdefiniowane w pliku `docker-compose.yml` dla usług:

- **postgres**:
  - `POSTGRES_USER`
  - `POSTGRES_PASSWORD`
  - `POSTGRES_DB`
- **pgadmin**:
  - `PGADMIN_DEFAULT_EMAIL`
  - `PGADMIN_DEFAULT_PASSWORD`

## Przydatne komendy

- **Zatrzymanie wszystkich kontenerów:**

  ```bash
  docker-compose down
  ```

- **Ponowne uruchomienie z budowaniem obrazów:**

  ```bash
  docker-compose up --build
  ```

- **Wyświetlenie logów:**

  ```bash
  docker-compose logs
  ```

