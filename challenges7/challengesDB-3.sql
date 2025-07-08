-- create table Utilisateurs (
-- id_utilisateur serial primary key,
-- nom varchar(100),
-- email varchar(100),
-- role varchar(20) check (role in ('lecteur', 'bibliothecaire', 'admin'))
-- );

-- CREATE TABLE Livre (
--     id_livre SERIAL PRIMARY KEY,
--     titre VARCHAR(150),
--     auteur VARCHAR(100),
--     categorie VARCHAR(50),
--     disponible BOOLEAN
-- );

-- CREATE TABLE Emprunts (
--     id_emprunts SERIAL PRIMARY KEY,
--     id_utilisateur INT REFERENCES Utilisateurs(id_utilisateur),
--     id_livre INT REFERENCES Livre(id_livre),
--     date_emprunt DATE,
--     date_retour_prevue DATE,
--     date_retour_reelle DATE
-- );


-- CREATE TABLE Commentaires (
--     id_commentaire SERIAL PRIMARY KEY,
--     id_utilisateur INT REFERENCES Utilisateurs(id_utilisateur),
--     id_livre INT REFERENCES Livre(id_livre),
--     texte TEXT,
--     note INT CHECK (note >= 1 AND note <= 5)
-- );


-- INSERT INTO Utilisateurs (id_utilisateur, nom, email, role) VALUES
-- (1, 'Alice Martin', 'alice.martin@mail.com', 'lecteur'),
-- (2, 'John Doe', 'john.doe@mail.com', 'bibliothecaire'),
-- (3, 'Sarah Lopez', 'sarah.lopez@mail.com', 'lecteur'),
-- (4, 'Marc Dupont', 'marc.dupont@mail.com', 'admin'),
-- (5, 'Emma Bernard', 'emma.bernard@mail.com', 'bibliothecaire'),
-- (6, 'Thomas Durand', 'thomas.durand@mail.com', 'lecteur');



-- INSERT INTO Livre (id_livre, titre, auteur, categorie, disponible) VALUES
-- (1, 'L''Étranger', 'Albert Camus', 'Roman', TRUE),
-- (2, '1984', 'George Orwell', 'Science-fiction', FALSE),
-- (3, 'Le Petit Prince', 'Antoine de Saint-Ex.', 'Conte', TRUE),
-- (4, 'Dune', 'Frank Herbert', 'Science-fiction', FALSE),
-- (5, 'Les Misérables', 'Victor Hugo', 'Classique', TRUE),
-- (6, 'Sapiens', 'Yuval Noah Harari', 'Histoire', TRUE);


-- INSERT INTO Emprunts (id_emprunts, id_utilisateur, id_livre, date_emprunt, date_retour_prevue, date_retour_reelle) VALUES
-- (1, 1, 2, '2024-06-01', '2024-06-15', NULL),
-- (2, 3, 4, '2024-06-20', '2024-07-05', '2024-07-03'),
-- (3, 6, 2, '2024-05-10', '2024-05-25', '2024-05-24'),
-- (4, 1, 4, '2024-07-01', '2024-07-15', NULL);


-- INSERT INTO Commentaires (id_commentaire, id_utilisateur, id_livre, texte, note) VALUES
-- (1, 1, 2, 'Un classique à lire absolument', 5),
-- (2, 3, 4, 'Très dense, mais fascinant', 4),
-- (3, 6, 2, 'Excellent, mais un peu long', 4),
-- (4, 1, 4, 'Très bon roman de SF', 5),
-- (5, 3, 1, 'Lecture facile et intéressante', 3);


-- SELECT * FROM Livre WHERE disponible = TRUE;

-- SELECT * FROM Utilisateurs WHERE role = 'bibliothecaire';

-- SELECT * FROM Emprunts WHERE date_retour_reelle IS NULL
--   AND date_retour_prevue < CURRENT_DATE;

-- SELECT COUNT(*) AS total_emprunts FROM Emprunts;

-- SELECT c.texte, c.note, u.nom AS utilisateur, l.titre AS livre
-- FROM Commentaires c
-- JOIN Utilisateurs u ON c.id_utilisateur = u.id_utilisateur
-- JOIN Livre l ON c.id_livre = l.id_livre
-- ORDER BY c.id_commentaire DESC
-- LIMIT 5;

-- SELECT u.nom, COUNT(e.id_emprunts) AS nb_emprunts
-- FROM Utilisateurs u
-- LEFT JOIN Emprunts e ON u.id_utilisateur = e.id_utilisateur
-- GROUP BY u.nom;


-- SELECT * FROM Livre l
-- WHERE NOT EXISTS (
--   SELECT 1 FROM Emprunts e
--   WHERE e.id_livre = l.id_livre
-- );


-- SELECT 
--   l.titre, 
--   AVG(
--     COALESCE(e.date_retour_reelle, CURRENT_DATE) - e.date_emprunt
--   ) AS duree_moyenne
-- FROM Livre l
-- JOIN Emprunts e ON l.id_livre = e.id_livre
-- GROUP BY l.titre;


-- SELECT l.titre, AVG(c.note) AS moyenne_note
-- FROM Livre l
-- JOIN Commentaires c ON l.id_livre = c.id_livre
-- GROUP BY l.titre
-- ORDER BY moyenne_note DESC
-- LIMIT 3;

-- SELECT DISTINCT u.nom
-- FROM Utilisateurs u
-- JOIN Emprunts e ON u.id_utilisateur = e.id_utilisateur
-- JOIN Livre l ON e.id_livre = l.id_livre
-- WHERE l.categorie = 'Science-fiction';

-- UPDATE Livre
-- SET disponible = FALSE
-- WHERE id_livre IN (
--   SELECT id_livre
--   FROM Emprunts
--   WHERE date_retour_reelle IS NULL
-- );


-- CREATE VIEW Vue_Emprunts_Actifs AS
-- SELECT *
-- FROM Emprunts
-- WHERE date_retour_reelle IS NULL;




