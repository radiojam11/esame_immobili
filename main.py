#Valerio Tognozzi
# Programma per la gestione Immobiliare
# 
# #
import testo 
from funzioni import *
from classi import *
cont = 0


#SQLite  Creo il file del data base se ancora non esiste e ci costruisco dentro  1 Cliente esempio ed 1 Immobile esempio (si troveranno all' ID 1)
import os
import sqlite3

db_filename = 'sqlite_immobiliare.db'
tabelle = 'tabelle.sql'
db_is_new = not os.path.exists(db_filename)

#Controllo se esiste il file DB - altrimento lo creo -  creo le tabelle dati - creo record di prova uno x tabella
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creo le tabelle del DataBase')
        with open(tabelle, 'rt') as f:
            t = f.read()
        conn.executescript(t)
        # inserimento di un immobile di esempio
        conn.execute("""
        insert into immobili (proprietario, indirizzo, prezzo, classe_energ)
        values ('1', 'via ESEMPIO', '50', 'G')
        """)
        # inserimento di Cliente di esempio
        conn.execute("""
        insert into clienti (nome, cognome, indirizzo, telefono, proprieta)
        values ('Esempio', 'Esempio','via ESEMPIO', '1111', '1')
        """)
    else:
        pass



# Tutte le altre Funzioni sono contenute nel file Funzioni - Qui solo Main
def main():
    """ Funzione principale"""
    #stampo il banner solo 1 volta alla partenza
    global cont
    if cont == 0:
        print(testo.banner)
        cont = 1
    #ricevo la scelta dal menu
    scelta = menu()
    global clienti
    global immobili
    # gestisco la scelta dell'utente
    # INSERIMENTO IMMOBILE
    if scelta == 1:
        inserisci_immobile()
        #ricarico la lista
        sqlite_start()
        input("digita un tasto per continuare.....")
    elif scelta == 2:
        # MODIFICA IMMOBILE
        modifica_immobile()
        sqlite_start()
        print(" modifica con successo")
    elif scelta == 3:
        # CANCELLAZIONE IMMOBILE
        cancella_immobile()
        sqlite_start()
        input("digita un tasto per continuare.....")
        pass
    elif scelta == 4:
        # STAMPA CATALOGO IMMOBILI
        stampa_immobili()
        input("digita un tasto per continuare.....")
    elif scelta == 5:
        # INSERISCI NUOVO CLIENTE
        inserisci_cliente()
        #ricarico la lista pulita ed aggiornata
        sqlite_start()
        input("digita un tasto per continuare.....")
    elif scelta == 6:
        # STAMPA ANAGRAFICA CLIENTE
        stampa_anagrafica_cliente()
        input("digita un tasto per continuare.....")
    elif  scelta == 7:
        # CERCA IMMOBILE PER INDIRIZZO
        cerca_immobile()
        input("digita un tasto per continuare.....")
    elif scelta == 8:
        # STAMPA CATALOGO
        stampa_catalogo()
        input("digita un tasto per continuare.....")
    elif scelta == 0:
        exit(222)
    else:
        pass


# MAIN
if __name__ == '__main__':
    sqlite_start() # carico i dati dal DB
    while True:
        main()