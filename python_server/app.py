from flask import Flask, jsonify, request
from flask_cors import CORS  # Umożliwia obsługę CORS, co pozwala na komunikację między różnymi domenami
import psycopg2  # Biblioteka do komunikacji z bazą danych PostgreSQL
import os
import time

# Pobieranie danych do połączenia z bazą danych z zmiennych środowiskowych lub ustawianie domyślnych wartości
DB_HOST = os.environ.get('DB_HOST', 'postgres')
DB_PORT = int(os.environ.get('DB_PORT', 5432))
DB_NAME = os.environ.get('DB_NAME', 'mydatabase')
DB_USER = os.environ.get('DB_USER', 'myuser')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'mypassword')

def connect_to_db():
    # Funkcja próbująca połączyć się z bazą danych, ponawiająca próbę co 5 sekund w przypadku niepowodzenia
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            print("Połączono z bazą danych")
            return conn
        except psycopg2.OperationalError:
            print("Błąd połączenia z bazą danych, ponawianie za 5 sekund...")
            time.sleep(5)

# Nawiązanie połączenia z bazą danych
conn = connect_to_db()
# Utworzenie kursora do wykonywania operacji na bazie danych
cursor = conn.cursor()

# Inicjalizacja aplikacji Flask
app = Flask(__name__)
CORS(app)  # Umożliwienie obsługi CORS dla całej aplikacji

# Endpoint GET do pobierania listy członków zespołu
@app.route('/team', methods=['GET'])
def get_team():
    # Wykonanie zapytania SQL pobierającego wszystkich członków zespołu
    cursor.execute('SELECT id, first_name, last_name, role FROM team_members;')
    # Pobranie wszystkich wyników
    team_members = cursor.fetchall()
    # Konwersja wyników na listę słowników
    team_list = []
    for member in team_members:
        team_list.append({
            'id': member[0],
            'firstName': member[1],
            'lastName': member[2],
            'role': member[3]
        })
    # Zwrócenie listy członków zespołu w formacie JSON
    return jsonify(team_list)

# Endpoint POST do dodawania nowego członka zespołu
@app.route('/team', methods=['POST'])
def add_team_member():
    # Pobranie danych nowego członka z żądania JSON
    new_member = request.get_json()
    # Zapytanie SQL wstawiające nowego członka do bazy danych, zwracające nadany przez bazę danych ID
    insert_query = '''
    INSERT INTO team_members (first_name, last_name, role) VALUES (%s, %s, %s) RETURNING id;
    '''
    # Wykonanie zapytania z przekazanymi wartościami
    cursor.execute(insert_query, (new_member['firstName'], new_member['lastName'], new_member['role']))
    # Pobranie nadanego ID
    new_id = cursor.fetchone()[0]
    # Zatwierdzenie transakcji
    conn.commit()
    # Dodanie ID do zwracanego obiektu
    new_member['id'] = new_id
    # Zwrócenie nowego członka z kodem statusu 201 (Created)
    return jsonify(new_member), 201

# Endpoint DELETE do usuwania członka zespołu po ID
@app.route('/team/<int:member_id>', methods=['DELETE'])
def delete_team_member(member_id):
    # Zapytanie SQL usuwające członka o podanym ID
    delete_query = 'DELETE FROM team_members WHERE id = %s;'
    # Wykonanie zapytania z przekazanym ID
    cursor.execute(delete_query, (member_id,))
    # Zatwierdzenie transakcji
    conn.commit()
    # Zwrócenie pustej odpowiedzi z kodem statusu 204 (No Content)
    return '', 204

if __name__ == '__main__':
    # Uruchomienie aplikacji Flask w trybie debug, dostępnej na wszystkich interfejsach sieciowych
    app.run(debug=True, host='0.0.0.0')
