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

def at_startup():
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

def primi_record():
    # Creo Clienti e Immobili di test
    #----------------------
    ClienteFactory.create_cliente("Mario", "Viterbese", "via Naspi 44", "554445", "p")
    ClienteFactory.create_cliente("Ugo", "Intini", "via Naspi 44", "2554445", "p")
    ClienteFactory.create_cliente("Paola", "Antani", "via CassaIntegrazione 4", "2554445", "p")
    ClienteFactory.create_cliente("Ugo", "Merli", "via poracci 124", "2554445", "a")
    ImmobileFactory.create_immobile(2, "via case rotte 77", 19000, "B")
    ImmobileFactory.create_immobile(1, "via case nuove 77", 999000, "G")
    ImmobileFactory.create_immobile(3, "via case alsole 77", 239000, "A")

def stampa_anagrafica_cliente_pw():
      query = Cliente.select()
      for el in query:
            print("Nome:", el.nome)

    
# MAIN
if __name__ == '__main__':
    at_startup()
    # togliere il cancelletto alla riga qui sotto solo se prima installazione del DB 
    # per popolare il DB.
    #primi_record()


    esame_immobili.funzioni_pw.stampa_anagrafica_cliente_pw()

    while True:
        #main()
        pass
        