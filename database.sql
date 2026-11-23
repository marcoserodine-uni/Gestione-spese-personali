
PRAGMA foreign_keys = ON;

-- CREAZIONE TABELLA CATEGORIE
CREATE TABLE IF NOT EXISTS categorie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

-- CREAZIONE TABELLA SPESE
CREATE TABLE IF NOT EXISTS spese (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    importo REAL NOT NULL CHECK(importo > 0),
    categoria_id INTEGER NOT NULL,
    descrizione TEXT,
    FOREIGN KEY (categoria_id) REFERENCES categorie(id)
);

-- CREAZIONE TABELLA BUDGET
CREATE TABLE IF NOT EXISTS budget (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mese TEXT NOT NULL,
    categoria_id INTEGER NOT NULL,
    importo REAL NOT NULL CHECK(importo > 0),
    UNIQUE(mese, categoria_id),
    FOREIGN KEY (categoria_id) REFERENCES categorie(id)
);

-- INSERIMENTO CATEGORIE DI ESEMPIO
INSERT INTO categorie (nome) VALUES
('Alimentari'),
('Trasporti'),
('Svago'),
('Casa');

-- INSERIMENTO SPESE DI ESEMPIO
INSERT INTO spese (data, importo, categoria_id, descrizione) VALUES
('2026-11-01', 45.50, 1, 'Spesa supermercato'),
('2026-11-03', 20.00, 2, 'Abbonamento trasporti'),
('2026-11-05', 15.00, 3, 'Cinema'),
('2026-11-08', 120.00, 4, 'Bolletta');

-- INSERIMENTO BUDGET DI ESEMPIO
INSERT INTO budget (mese, categoria_id, importo) VALUES
('2026-11', 1, 250.00),
('2026-11', 2, 80.00),
('2026-11', 3, 100.00),
('2026-11', 4, 200.00);
