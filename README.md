# Aplikacja Webowa z użyciem Django, React i Dockera

Projekt przedstawia prostą aplikację webową do zarządzania członkami zespołu, zbudowaną przy użyciu **Django** (backend), **React** (frontend) oraz **Docker** do konteneryzacji.

## Spis treści

- [Opis projektu](#opis-projektu)
- [Funkcjonalności](#funkcjonalności)
- [Technologie](#technologie)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Uruchamianie aplikacji](#uruchamianie-aplikacji)
- [Dostęp do aplikacji](#dostęp-do-aplikacji)
- [Korzystanie z API](#korzystanie-z-api)
- [Logowanie do panelu administracyjnego Django](#logowanie-do-panelu-administracyjnego-django)
- [Ładowanie danych początkowych](#ładowanie-danych-początkowych)
- [Autor](#autor)

## Opis projektu

Aplikacja umożliwia zarządzanie członkami zespołu poprzez interfejs webowy. Użytkownicy mogą dodawać, wyświetlać i usuwać członków zespołu. Projekt jest podzielony na trzy główne komponenty:

- **Backend**: Aplikacja Django udostępniająca API RESTful.
- **Frontend**: Aplikacja React umożliwiająca interakcję z API.
- **Baza danych**: PostgreSQL przechowujący dane o członkach zespołu.

## Funkcjonalności

- **Wyświetlanie listy członków zespołu**: Imię, nazwisko i rola każdego członka.
- **Dodawanie nowych członków**: Formularz do wprowadzania danych nowego członka.
- **Usuwanie członków**: Możliwość usunięcia istniejącego członka zespołu.
- **API RESTful**: Backend udostępnia API do zarządzania danymi, co umożliwia łatwą integrację z innymi aplikacjami.

## Technologie

- **Backend**: Python, Django, Django REST Framework
- **Frontend**: React, TypeScript, Vite
- **Baza danych**: PostgreSQL
- **Konteneryzacja**: Docker, Docker Compose
- **Inne**: Axios, Django CORS Headers

## Wymagania

- **Docker**: [Instalacja Dockera](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Instalacja Docker Compose](https://docs.docker.com/compose/install/)

## Instalacja

1. **Sklonuj repozytorium na swój lokalny komputer:**

   ```bash
   git clone https://github.com/larekdarek/wdpai_web_app.git
   cd wdpai_web_app
   ```

2. **Upewnij się, że masz zainstalowane Docker i Docker Compose.**

## Uruchamianie aplikacji

Uruchom aplikację za pomocą Docker Compose:

```bash
docker-compose up --build
```

- **`--build`**: Opcja ta wymusza przebudowanie obrazów Dockera, co jest przydatne po zmianach w kodzie.

Aplikacja uruchomi trzy usługi:

- **db**: Baza danych PostgreSQL.
- **backend**: Aplikacja Django dostępna na porcie 8000.
- **frontend**: Aplikacja React dostępna na porcie 80.

Aby uruchomić aplikację w tle (w trybie detached), użyj:

```bash
docker-compose up --build -d
```

## Dostęp do aplikacji

- **Frontend**: [http://localhost](http://localhost)
- **Backend API**: [http://localhost:8000/api/](http://localhost:8000/api/)
- **Panel administracyjny Django**: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Korzystanie z API

Możesz testować API za pomocą narzędzi takich jak **Postman** lub **curl**.

### Przykładowe żądania:

- **Pobierz listę członków zespołu:**

  ```bash
  curl http://localhost:8000/api/members/
  ```

- **Dodaj nowego członka:**

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"first_name": "Anna", "last_name": "Kowalska", "role": "Developer"}' http://localhost:8000/api/members/
  ```

- **Usuń członka o ID 1:**

  ```bash
  curl -X DELETE http://localhost:8000/api/members/1/
  ```

## Logowanie do panelu administracyjnego Django

1. **Utwórz superużytkownika:**

   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```

   Podaj nazwę użytkownika, adres e-mail i hasło zgodnie z instrukcjami.

2. **Zaloguj się do panelu administracyjnego:**

   Przejdź do [http://localhost:8000/admin/](http://localhost:8000/admin/) i zaloguj się używając danych superużytkownika.

3. **Zarządzaj danymi:**

   Po zalogowaniu możesz dodawać, edytować i usuwać członków zespołu oraz zarządzać innymi aspektami aplikacji.

## Ładowanie danych początkowych

Jeśli chcesz załadować przykładowe dane do bazy danych, wykonaj poniższe kroki:

1. **Upewnij się, że migracje zostały zastosowane:**

   ```bash
   docker-compose exec backend python manage.py migrate
   ```

2. **Załaduj dane z pliku `initial_data.json`:**

   ```bash
   docker-compose exec backend python manage.py loaddata initial_data.json
   ```

   Plik `initial_data.json` znajduje się w folderze `backend/team/fixtures` i zawiera przykładowe wpisy członków zespołu.


- **Debugowanie**:

  - Aby wyświetlić logi wszystkich kontenerów:

    ```bash
    docker-compose logs -f
    ```

  - Aby zatrzymać wszystkie usługi:

    ```bash
    docker-compose down
    ```

