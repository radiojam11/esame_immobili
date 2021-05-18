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
# se si modifica il nome ricordarsi di cambiare anche nel file classi_pw.py
nome_file_db = "immobiliare_pw.db"
db_pw = peewee.SqliteDatabase(nome_file_db)


# Tutte le altre Funzioni sono contenute nel file Funzioni - Qui solo Main
# MAIN
if __name__ == '__main__':
    at_startup()
    # togliere il cancelletto alla riga qui sotto 
    # nel caso di prima installazione del DB 
    # per popolare il DB.
    #primi_record()
    while True:
        clear_sceen()
        main()
        #pass
        