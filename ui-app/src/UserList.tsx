// src/UserList.tsx
/*
Ten komponent wyświetla listę członków zespołu oraz formularz do dodawania nowych członków.
Komunikuje się z backendowym API, aby pobierać i wysyłać dane.
*/
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles/styles.css';

// Definicja interfejsu dla użytkownika
interface User {
  id: number;
  first_name: string;
  last_name: string;
  role: string;
}

const UserList: React.FC = () => {
  // Stan do przechowywania listy użytkowników
  const [users, setUsers] = useState<User[]>([]);
  // Stan do przechowywania danych formularza
  const [newUser, setNewUser] = useState({
    first_name: '',
    last_name: '',
    role: ''
  });
  const [privacy, setPrivacy] = useState(false);

  // Pobranie adresu API z zmiennych środowiskowych
  const API_URL = `${import.meta.env.VITE_API_URL}/members/`;

  // Wywołanie fetchUsers przy montowaniu komponentu
  useEffect(() => {
    fetchUsers();
  }, []);

  // Funkcja do pobierania użytkowników z API
  const fetchUsers = () => {
    axios.get<User[]>(API_URL)
      .then(response => {
        setUsers(response.data); // Aktualizacja stanu użytkowników
      })
      .catch(error => console.error('Error fetching users:', error));
  };

  // Dodawanie użytkownika
  const handleAddUser = (e: React.FormEvent) => {
    e.preventDefault(); // Zapobiegamy domyślnemu działaniu formularza
    if (!privacy) {
      alert('Musisz zaakceptować politykę prywatności.');
      return;
    }
    axios.post<User>(API_URL, newUser)
      .then(response => {
        setUsers([...users, response.data]);
        setNewUser({ first_name: '', last_name: '', role: '' });
        setPrivacy(false);
      })
      .catch(error => console.error('Error adding user:', error));
  };

  // Usuwanie użytkownika
  const handleDeleteUser = (id: number) => {
    axios.delete(`${API_URL}${id}/`)
      .then(() => {
        setUsers(users.filter(user => user.id !== id));
      })
      .catch(error => console.error('Error deleting user:', error));
  };

  return (
    <div className="body">
      <div className="container">
        {/* Formularz dodawania użytkownika */}
        <div className="form-container">
          <h2 className="title">Let's level up your brand, together</h2>
          <form className="team-form" onSubmit={handleAddUser}>
            <label htmlFor="first-name" className="form-label">First name</label>
            <input
              type="text"
              id="first-name"
              className="input-text"
              placeholder="First name"
              value={newUser.first_name}
              onChange={e => setNewUser({ ...newUser, first_name: e.target.value })}
              required
            />

            <label htmlFor="last-name" className="form-label">Last name</label>
            <input
              type="text"
              id="last-name"
              className="input-text"
              placeholder="Last name"
              value={newUser.last_name}
              onChange={e => setNewUser({ ...newUser, last_name: e.target.value })}
              required
            />

            <label htmlFor="role" className="form-label">Role</label>
            <select
              id="role"
              className="select-role"
              value={newUser.role}
              onChange={e => setNewUser({ ...newUser, role: e.target.value })}
              required
            >
              <option value="" disabled>Role</option>
              <option value="Manager">Manager</option>
              <option value="Product Designer">Product Designer</option>
              <option value="CTO">CTO</option>
              <option value="Development Lead">Development Lead</option>
            </select>

            <label className="privacy-label">
              <input
                type="checkbox"
                className="checkbox-input"
                checked={privacy}
                onChange={e => setPrivacy(e.target.checked)}
                required
              />
              You agree to our friendly&nbsp;<a href="#">privacy policy</a>.
            </label>

            <button type="submit" className="submit-button">SUBMIT</button>
          </form>
        </div>

        {/* Lista użytkowników */}
        <div className="team-list">
          {users.map(user => (
            <div className="team-member" key={user.id}>
              <div className="details">
                <span className="name">{user.first_name} {user.last_name}</span>
                <span className="role">{user.role}</span>
              </div>
              <button className="delete-btn" onClick={() => handleDeleteUser(user.id)}>&times;</button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default UserList;
