from flask import Flask, jsonify, request
from flask_cors import CORS  # Importujemy CORS, aby umożliwić komunikację między domenami

app = Flask(__name__)
CORS(app)  # Umożliwiamy CORS dla całej aplikacji

# Początkowa lista członków zespołu z unikalnymi ID
team_members = [
    {'id': 1, 'firstName': 'Cameron', 'lastName': 'Williamson', 'role': 'Manager'},
    {'id': 2, 'firstName': 'Thomas', 'lastName': 'Blue', 'role': 'Development Lead'},
    {'id': 3, 'firstName': 'Jack', 'lastName': 'Sparrow', 'role': 'Product Designer'},
    {'id': 4, 'firstName': 'Cthulu', 'lastName': 'Rylien', 'role': 'CTO'}
]

# Zmienna przechowująca następny dostępny ID
next_id = 5

# Endpoint GET do pobierania listy członków zespołu
@app.route('/team', methods=['GET'])
def get_team():
    return jsonify(team_members)  # Zwracamy listę w formacie JSON

# Endpoint POST do dodawania nowego członka zespołu
@app.route('/team', methods=['POST'])
def add_team_member():
    global next_id
    new_member = request.get_json()  # Pobieramy dane z żądania
    new_member['id'] = next_id  # Przypisujemy nowy ID
    next_id += 1
    team_members.append(new_member)  # Dodajemy nowego członka do listy
    return jsonify(new_member), 201  # Zwracamy dodanego członka z kodem 201 (Created)

# Endpoint DELETE do usuwania członka zespołu po ID
@app.route('/team/<int:member_id>', methods=['DELETE'])
def delete_team_member(member_id):
    global team_members
    # Filtrujemy listę, usuwając pasującego członka po ID
    team_members = [m for m in team_members if m['id'] != member_id]
    return '', 204  # Zwracamy pustą odpowiedź z kodem 204 (No Content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Uruchamiamy aplikację w trybie debug
