// Upewniamy się, że DOM jest w pełni załadowany przed wykonaniem skryptu
document.addEventListener('DOMContentLoaded', function() {
    const teamForm = document.getElementById('team-form');
    const teamList = document.getElementById('team-list');

    // Pobieramy listę członków zespołu po załadowaniu strony
    window.addEventListener('load', function() {
        fetch('/api/team')  // Wysyłamy żądanie GET do endpointu /team
            .then(response => response.json())  // Odbieramy i parsujemy odpowiedź JSON
            .then(data => {
                // Dla każdego członka zespołu wywołujemy funkcję dodającą go do listy
                data.forEach(member => addMemberToList(member));
            })
            .catch(error => {
                console.error('There was a problem with the GET request:', error);
            });
    });

    // Obsługa zdarzenia submit formularza dodawania nowego członka
    teamForm.addEventListener('submit', function(e) {
        e.preventDefault(); // Zapobiegamy domyślnej akcji formularza (przeładowanie strony)

        // Pobieramy wartości z pól formularza
        const firstName = document.getElementById('first-name').value.trim();
        const lastName = document.getElementById('last-name').value.trim();
        const role = document.getElementById('role').value;
        const privacyChecked = document.getElementById('privacy').checked;

        // Walidacja danych formularza
        if (!firstName || !lastName || !role) {
            alert("All fields are required!");
            return;
        }

        if (!privacyChecked) {
            alert("You must agree to the privacy policy.");
            return;
        }

        // Tworzymy obiekt z nowym członkiem zespołu
        const newMember = { firstName, lastName, role };

        // Wysyłamy żądanie POST do endpointu /team z nowym członkiem
        fetch('/api/team', {  
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newMember)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Parsujemy odpowiedź JSON
        })
        .then(data => {
            addMemberToList(data); // Dodajemy nowego członka do listy na stronie
            teamForm.reset();  // Resetujemy formularz po pomyślnym dodaniu
        })
        .catch(error => {
            console.error('There was a problem with the POST request:', error);
        });
    });

    // Funkcja dodająca członka zespołu do listy na stronie
    function addMemberToList(member) {
        // Tworzymy nowy element div dla członka zespołu
        const memberDiv = document.createElement('div');
        memberDiv.classList.add('team-member');
        memberDiv.setAttribute('data-id', member.id); // Przechowujemy ID jako atrybut data-id
        memberDiv.innerHTML = `
            <div class="details">
                <span class="name">${member.firstName} ${member.lastName}</span>
                <span class="role">${member.role}</span>
            </div>
            <button class="delete-btn">🗑</button>
        `;

        // Dodajemy funkcjonalność usuwania członka po kliknięciu ikony kosza
        memberDiv.querySelector('.delete-btn').addEventListener('click', function() {
            const memberId = member.id; // Pobieramy ID członka
            fetch(`/api/team/${memberId}`, {
                method: 'DELETE'
            })            
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                teamList.removeChild(memberDiv); // Usuwamy element z DOM
            })
            .catch(error => {
                console.error('There was a problem with the DELETE request:', error);
            });
        });

        // Dodajemy nowy element do listy członków zespołu
        teamList.appendChild(memberDiv);
    }
});
