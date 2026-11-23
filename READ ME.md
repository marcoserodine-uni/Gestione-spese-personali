\# **Sistema di gestione delle spese personali e del budget**



\## **1. Come avviare il programma**



\### Requisiti per l'utilizzo



Per utilizzare il programma è necessario:

\- Avere Python 3 installato sul computer.

\- Scaricare la cartella del progetto.

\- Aprire un terminale nella cartella contenente il file `main.py`.



\### Avvio dell'applicazione



Per avviare il programma, aprire il terminale nella cartella del progetto ed eseguire il comando:



python main.py



Su alcuni sistemi potrebbe essere necessario utilizzare:



py main.py



All'avvio, il programma crea automaticamente il database SQLite spese.db.



Successivamente viene visualizzato un messaggio di benvenuto e il menu principale.



\## **2. Come utilizzare il programma**



\### Menu principale



Il programma presenta cinque opzioni:



*1. Gestione Categorie*

*2. Inserisci Spesa*

*3. Definisci Budget Mensile*

*4. Visualizza Report*

*5. Esci*



L'utente può selezionare la funzione desiderata inserendo il numero corrispondente.



Se viene inserito un valore non valido, il programma mostra un messaggio di errore e permette di effettuare una nuova scelta.



\### **2.1 Gestione Categorie**



Questa funzione permette di creare nuove categorie per organizzare le spese.



Dopo aver selezionato l'opzione 1, il programma richiede il nome della categoria.



Esempi:

\- Alimentari

\- Trasporti

\- Casa

\- Svago

\- Salute



Il nome non può essere vuoto. Il programma verifica inoltre che la categoria non sia già presente nel database, evitando duplicati.



<<**Importante**:>> prima di registrare una spesa o definire un budget, è necessario creare la relativa categoria.



\### **2.2 Inserimento Spesa**



Questa funzione consente di registrare una nuova spesa.



Dopo aver selezionato l'opzione 2, il programma richiede:



1\. Data: formato AAAA-MM-GG.

&#x20;  - Esempio: 2026-11-20



2\. Importo: valore della spesa in euro.

&#x20;  - Esempio: 25.50

&#x20;  - È possibile utilizzare anche la virgola: 25,50.

&#x20;  - L'importo deve essere maggiore di zero.



3\. Categoria: nome di una categoria già registrata.

&#x20;  - Esempio: `Alimentari`



4\. Descrizione: breve descrizione della spesa, facoltativa.

&#x20;  - Esempio: Spesa supermercato



Il programma controlla la validità della data, dell'importo e della categoria.



Se tutti i dati sono corretti, la spesa viene salvata nel database e viene visualizzato un messaggio di conferma.



\### **2.3 Definizione Budget Mensile**



Questa funzione permette di stabilire un limite di spesa mensile per ciascuna categoria.



Dopo aver selezionato l'opzione 3, il programma richiede:



1\. Mese: formato AAAA-MM.

&#x20;  - Esempio: 2026-11



2\. Categoria: categoria già presente nel database.

&#x20;  - Esempio: Alimentari



3\. Importo: limite di budget in euro.

&#x20;  - Esempio: 250.00



Il programma verifica che il mese sia valido, che la categoria esista e che l'importo sia maggiore di zero.



Se viene definito un nuovo budget, questo viene registrato nel database.



Se esiste già un budget per la stessa categoria e lo stesso mese, il programma aggiorna automaticamente l'importo precedente con quello nuovo.



\### **2.4 Visualizzazione Report**



Selezionando l'opzione 4 dal menu principale, viene aperto un secondo menu dedicato ai report.



Sono disponibili quattro opzioni.



**1. Totale spese per categoria**



Mostra il totale delle spese registrate per ciascuna categoria.



Gli importi vengono sommati automaticamente e i risultati sono ordinati alfabeticamente per nome della categoria.



**2. Spese mensili vs budget**



Permette di confrontare le spese sostenute con i budget definiti per un determinato mese.



Il programma richiede di inserire il mese nel formato AAAA-MM.



Per ogni categoria con un budget registrato vengono mostrati:

\- Nome della categoria.

\- Importo del budget.

\- Totale delle spese del mese.

\- Stato del budget.



Lo stato può essere:

\- BUDGET RISPETTATO: quando il totale delle spese è inferiore o uguale al budget.

\- SUPERAMENTO BUDGET: quando il totale delle spese supera il budget disponibile.



Se non esistono budget per il mese selezionato, viene visualizzato un messaggio informativo.



**3. Elenco completo delle spese ordinate per data**



Mostra tutte le spese registrate nel database.



Per ogni spesa vengono visualizzati:

*- Data.*

*- Categoria.*

*- Importo.*

*- Descrizione.*



Le spese vengono ordinate cronologicamente, dalla data più vecchia alla più recente.



**4. Ritorna al menu principale**



Permette di uscire dal menu dei report e tornare alla schermata principale.



\### **2.5 Uscita dal programma**



Selezionando l'opzione 5 dal menu principale, il programma termina mostrando il messaggio:



*Uscita dal programma.*



I dati già registrati rimangono salvati nel database SQLite e saranno disponibili al successivo avvio.



\## **3. Descrizione del progetto**



Il progetto consiste nella realizzazione di un programma per la gestione delle spese personali e del budget mensile.



Il software è stato sviluppato in Python e utilizza SQLite come database relazionale per memorizzare categorie, spese e budget.



L'applicazione funziona tramite un'interfaccia a console e permette di registrare le spese, organizzare le categorie, definire limiti di spesa mensili e consultare report riepilogativi.



\## **4. Tecnologie utilizzate**



\- Python 3: linguaggio utilizzato per sviluppare il programma.

\- SQLite: database utilizzato per memorizzare le informazioni.

\- SQL: linguaggio utilizzato per creare e interrogare le tabelle del database.



Non è necessario installare librerie esterne: vengono utilizzati moduli già inclusi in Python.



**## 5. Struttura del database**



Il database SQLite è composto da tre tabelle:



\- categorie: contiene i nomi delle categorie inserite.

\- spese: contiene le spese registrate, con data, importo, categoria e descrizione.

\- budget: contiene i budget mensili associati alle categorie.



Le tabelle sono collegate tramite chiavi esterne (FOREIGN KEY).



Sono inoltre presenti vincoli per garantire la correttezza dei dati, tra cui PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE e NOT NULL.



**## 6. Struttura dei file del progetto**



La cartella del progetto contiene i seguenti file:



\- main.py: codice sorgente dell'applicazione.

\- database.sql: script SQL per la creazione delle tabelle e l'inserimento dei dati di esempio.

\- spese.db: database SQLite generato automaticamente dal programma.

\- README.txt`: guida descrittiva e istruzioni per l'utilizzo.



**## 7. Autore**



Elaborato universitario realizzato da **SERODINE MARCO** matricola **0092500183** per il corso di laurea in Ingegneria Biomedica (L-9), 

Università Telematica San Raffaele Roma.

