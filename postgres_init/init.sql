CREATE TABLE team_members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role VARCHAR(50)
);

INSERT INTO team_members (first_name, last_name, role) VALUES
('Cameron', 'Williamson', 'Manager'),
('Thomas', 'Blue', 'Development Lead'),
('Jack', 'Sparrow', 'Product Designer'),
('Cthulu', 'Rylien', 'CTO');
