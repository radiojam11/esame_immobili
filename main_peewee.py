#Valerio Tognozzi
# Programma per la gestione Immobiliare
#
############################  PEEWEE   CASO 3 #################################
# Il sistema sviluppato con PeeWee si rivoluziona completamente.
# Lascio l'organizzazione basata su liste e lavoro completamente su DB
# 
# Lascio inalterato il sistema di selezione delle scelte dell'utente
# 
# #

from classi_pw import *
import testo 
import peewee
from funzioni_pw import *
from classi_pw import *
import os

# indirizzo del file di DB peewee
nome_file_db = "immobiliare_pw.db"
db_pw = peewee.SqliteDatabase(nome_file_db)


# Tutte le altre Funzioni sono contenute nel file Funzioni - Qui solo Main
def main():
    """ Funzione principale"""
    
    #ricevo la scelta dal menu
    scelta = menu()
    global clienti
    global immobili

    # gestisco la scelta dell'utente
    if scelta == 1:
        # INSERIMENTO IMMOBILE
        inserisci_immobile_pw()
        input("digita un tasto per continuare.....")
    elif scelta == 2:
        # MODIFICA IMMOBILE
        modifica_immobile_pw()
        input("digita un tasto per continuare.....")
    elif scelta == 3:
        # CANCELLAZIONE IMMOBILE
        cancella_immobile_pw()
        input("digita un tasto per continuare.....")
    elif scelta == 4:
        # STAMPA CATALOGO IMMOBILI
        stampa_immobili_pw()
        input("digita un tasto per continuare.....")
    elif scelta == 5:
        # INSERISCI NUOVO CLIENTE
        inserisci_cliente_pw()
        input("digita un tasto per continuare.....")
    elif scelta == 6:
        # STAMPA ANAGRAFICA CLIENTE
        stampa_anagrafica_cliente_pw()
        input("digita un tasto per continuare.....")
    elif  scelta == 7:
        # CERCA IMMOBILE PER INDIRIZZO
        cerca_immobile_pw()
        input("digita un tasto per continuare.....")
    elif scelta == 8:
        # STAMPA CATALOGO
        stampa_catalogo_pw()
        input("digita un tasto per continuare.....")
    elif scelta == 0:
        exit(222)
    else:
        pass


# MAIN
if __name__ == '__main__':
    # stampo un bannerino pubblicitario!
    print(testo.banner)
    # se il file DB esiste immagino che esistano anche le varie tabelle e record di categoria 
    # - altrimenti li creo ex novo
    if not (os.path.isfile(nome_file_db)):
        # mi connetto al DB e se non esiste peewee lo crea in automatico
        db_pw.connect()
        # creo le tabelle
        db_pw.create_tables([Tipo_Cliente, Catalogo, Cliente, Immobile])
        # creo i record delle categorie
        Tipo_Cliente(tipo_cliente="Proprietario").save()
        Tipo_Cliente(tipo_cliente="Affittuario").save()
        Catalogo(catalogo="prestigio").save()
        Catalogo(catalogo="casa vacanze").save()
        Catalogo(catalogo="popolare").save()
    else:
        # se sono qui il file del DB esiste gia' e do' per scontato 
        # che anche le tabelle ed i record esistano
        db_pw.connect()


    while True:
        #main()
        pass
        