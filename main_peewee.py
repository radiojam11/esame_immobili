#Valerio Tognozzi
# Programma per la gestione Immobiliare
#
# Punto n. 3 estensione PeeWee
# #

import testo 
from funzioni_pw import *
from classi_pw import *



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
    print(testo.banner)
    while True:
        main()