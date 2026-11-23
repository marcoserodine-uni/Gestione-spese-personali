
import sqlite3
import math
from datetime import datetime

def crea_database():
    connessione = sqlite3.connect("spese.db")
    connessione.execute("PRAGMA foreign_keys = ON")
    cursore = connessione.cursor()

    cursore.execute("""
        CREATE TABLE IF NOT EXISTS categorie (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    """)

    cursore.execute("""
        CREATE TABLE IF NOT EXISTS spese (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            importo REAL NOT NULL CHECK(importo > 0),
            categoria_id INTEGER NOT NULL,
            descrizione TEXT,
            FOREIGN KEY (categoria_id) REFERENCES categorie(id)
        )
    """)

    cursore.execute("""
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mese TEXT NOT NULL,
            categoria_id INTEGER NOT NULL,
            importo REAL NOT NULL CHECK(importo > 0),
            UNIQUE(mese, categoria_id),
            FOREIGN KEY (categoria_id) REFERENCES categorie(id)
        )
    """)

    connessione.commit()
    connessione.close()


def gestione_categorie():
    print("\n===== GESTIONE CATEGORIE =====")

    nome = input("Inserisci il nome della categoria: ").strip()

    if nome == "":
        print("Errore: il nome della categoria non può essere vuoto.")
        return

    connessione = sqlite3.connect("spese.db")
    connessione.execute("PRAGMA foreign_keys = ON")
    cursore = connessione.cursor()

    cursore.execute(
    "SELECT * FROM categorie WHERE nome = ? COLLATE NOCASE",
    (nome,)
)

    categoria = cursore.fetchone()

    if categoria:
        print("Questa categoria esiste già.")
    else:
        cursore.execute(
            "INSERT INTO categorie (nome) VALUES (?)",
            (nome,)
        )
        connessione.commit()
        print("Categoria inserita correttamente!")

    connessione.close()

def inserisci_spesa():
    print("\n===== INSERIMENTO SPESA =====")

    data = input("Inserisci la data (AAAA-MM-GG): ")
    try:
        datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        print("Errore: inserisci una data valida nel formato AAAA-MM-GG.")
        return

    importo_testo = input("Inserisci l'importo in euro: ")

    try:
        importo = float(importo_testo.replace(",", "."))
    except ValueError:
        print("Errore: inserisci un importo valido.")
        return

    if not math.isfinite(importo) or importo <= 0:
        print("Errore: l'importo deve essere maggiore di zero.")
        return

    categoria = input("Inserisci la categoria: ").strip()

    connessione = sqlite3.connect("spese.db")
    connessione.execute("PRAGMA foreign_keys = ON")
    cursore = connessione.cursor()

    cursore.execute(
        "SELECT id FROM categorie WHERE nome = ? COLLATE NOCASE",
        (categoria,)
    )

    risultato = cursore.fetchone()

    if risultato is None:
        print("Errore: la categoria non esiste.")
        connessione.close()
        return

    categoria_id = risultato[0]

    descrizione = input("Inserisci una descrizione (facoltativa): ")

    cursore.execute("""
        INSERT INTO spese (data, importo, categoria_id, descrizione)
        VALUES (?, ?, ?, ?)
    """, (data, importo, categoria_id, descrizione))

    connessione.commit()
    connessione.close()

    print("Spesa inserita correttamente!")

def definisci_budget():
    print("\n===== DEFINIZIONE BUDGET MENSILE =====")

    mese = input("Inserisci il mese (AAAA-MM): ")

    try:
        datetime.strptime(mese, "%Y-%m")
    except ValueError:
        print("Errore: inserisci un mese valido nel formato AAAA-MM.")
        return

    categoria = input("Inserisci la categoria: ").strip()

    importo_testo = input("Inserisci il budget in euro: ")

    try:
        importo = float(importo_testo.replace(",", "."))
    except ValueError:
        print("Errore: inserisci un importo valido.")
        return

    if not math.isfinite(importo) or importo <= 0:
        print("Errore: il budget deve essere maggiore di zero.")
        return

    connessione = sqlite3.connect("spese.db")
    connessione.execute("PRAGMA foreign_keys = ON")
    cursore = connessione.cursor()

    cursore.execute(
        "SELECT id FROM categorie WHERE nome = ? COLLATE NOCASE",
        (categoria,)
    )

    risultato = cursore.fetchone()

    if risultato is None:
        print("Errore: la categoria non esiste.")
        connessione.close()
        return

    categoria_id = risultato[0]

    cursore.execute("""
        INSERT INTO budget (mese, categoria_id, importo)
        VALUES (?, ?, ?)
        ON CONFLICT(mese, categoria_id)
        DO UPDATE SET importo = excluded.importo
    """, (mese, categoria_id, importo))

    connessione.commit()
    connessione.close()

    print("Budget mensile salvato correttamente!")

def visualizza_report():
    while True:
        print("\n===== MENU REPORT =====")
        print("1. Totale spese per categoria")
        print("2. Spese mensili vs budget")
        print("3. Elenco completo delle spese ordinate per data")
        print("4. Ritorna al menu principale")

        scelta = input("Inserisci la tua scelta: ")

        if scelta == "1":
            report_totale_categorie()
        elif scelta == "2":
            report_budget()
        elif scelta == "3":
            report_elenco_spese()
        elif scelta == "4":
            break
        else:
            print("Scelta non valida. Riprova.")
def report_totale_categorie():
    print("\n===== TOTALE SPESE PER CATEGORIA =====")

    connessione = sqlite3.connect("spese.db")
    connessione.execute("PRAGMA foreign_keys = ON")
    cursore = connessione.cursor()

    cursore.execute("""
        SELECT categorie.nome, SUM(spese.importo)
        FROM spese
        INNER JOIN categorie
        ON spese.categoria_id = categorie.id
        GROUP BY categorie.id
        ORDER BY categorie.nome
    """)

    risultati = cursore.fetchall()

    if not risultati:
        print("Non sono presenti spese registrate.")
    else:
        print("\nCategoria          Totale Speso")
        print("--------------------------------")

        for categoria, totale in risultati:
            print(f"{categoria:<20} {totale:.2f} euro")

    connessione.close()

def report_budget():
    print("\n===== SPESE MENSILI VS BUDGET =====")

    mese = input("Inserisci il mese da controllare (AAAA-MM): ")

    try:
        datetime.strptime(mese, "%Y-%m")
    except ValueError:
        print("Errore: inserisci un mese valido nel formato AAAA-MM.")
        return

    connessione = sqlite3.connect("spese.db")
    connessione.execute("PRAGMA foreign_keys = ON")
    cursore = connessione.cursor()

    cursore.execute("""
        SELECT
            categorie.nome,
            budget.importo,
            COALESCE(SUM(spese.importo), 0)
        FROM budget
        INNER JOIN categorie
            ON budget.categoria_id = categorie.id
        LEFT JOIN spese
            ON spese.categoria_id = categorie.id
            AND substr(spese.data, 1, 7) = budget.mese
        WHERE budget.mese = ?
        GROUP BY categorie.id, budget.importo
    """, (mese,))

    risultati = cursore.fetchall()

    if not risultati:
        print("Non esistono budget per il mese selezionato.")
    else:
        for categoria, budget, speso in risultati:
            print("\nCategoria:", categoria)
            print(f"Budget: {budget:.2f} euro")
            print(f"Speso: {speso:.2f} euro")

            if speso > budget:
                print("Stato: SUPERAMENTO BUDGET")
            else:
                print("Stato: BUDGET RISPETTATO")

    connessione.close()
def report_elenco_spese():
    print("\n===== ELENCO COMPLETO DELLE SPESE =====")

    connessione = sqlite3.connect("spese.db")
    connessione.execute("PRAGMA foreign_keys = ON")
    cursore = connessione.cursor()

    cursore.execute("""
        SELECT
            spese.data,
            categorie.nome,
            spese.importo,
            spese.descrizione
        FROM spese
        INNER JOIN categorie
            ON spese.categoria_id = categorie.id
        ORDER BY spese.data ASC
    """)

    risultati = cursore.fetchall()

    if not risultati:
        print("Non sono presenti spese registrate.")
    else:
        print("\nData         Categoria       Importo       Descrizione")
        print("----------------------------------------------------------")

        for data, categoria, importo, descrizione in risultati:
            print(f"{data:<12} {categoria:<15} {importo:>8.2f} euro   {descrizione or '-'}")

    connessione.close()

def menu():
    while True:
        print("\n===== SISTEMA DI GESTIONE SPESE PERSONALI =====")
        print("1. Gestione Categorie")
        print("2. Inserisci Spesa")
        print("3. Definisci Budget Mensile")
        print("4. Visualizza Report")
        print("5. Esci")

        scelta = input("Inserisci la tua scelta: ")

        if scelta == "1":
            gestione_categorie()
        elif scelta == "2":
            inserisci_spesa()
        elif scelta == "3":
            definisci_budget()
        elif scelta == "4":
            visualizza_report()
        elif scelta == "5":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")


crea_database()
print("Database creato correttamente!")
print("\nBenvenuto nel Sistema di Gestione delle Spese Personali!")

menu()
