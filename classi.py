import os
import sqlite3
from funzioni import *
from main import *
#db_filename = 'sqlite_immobiliare.db'

# LE CLASSI
class Immobile():
    """Classe Immobile contiene tutte le informazioni relative all'immobile"""
    def __init__(self, id=None, proprietario=None, indirizzo=None, prezzo=None, classe_energ=None):
        self.id=id
        self.proprietario=proprietario
        self.indirizzo=indirizzo
        self.prezzo=prezzo
        self.classe_energ=classe_energ
        if int(self.prezzo) <=100000:
            cat = "Popolare"
        elif int(self.prezzo) > 100000 and int(self.prezzo) <= 250000:
            cat = "Vacanze"
        else:
            cat = "Prestigio"
        self.catalogo = cat
    def mod_attributo(self, a): # a riceve una tupla(attributo_da_modificare, nuovo_valore_attributo)
        """Modulo per la modifica dei singoli attributi della Classe per operazioni su lista (versione di base del sw) """
        if a[0]=="proprietario":
            self.proprietario = a[1]
        elif a[0]=="indirizzo":
            self.indirizzo = a[1]
        elif a[0]=="prezzo":
            self.prezzo = a[1]
        elif a[0]=="classe_energ":
            self.classe_energ = a[1]
        else:
            return False
        return True
    def mod_sqlite(self, a):
        """Modulo per la modifica dei singoli attributi della Classe - Scelta: modificare direttamente nel DB e ricaricare il DB ogni volta su lista pulita """
        global db_filename
        if a[0]=="proprietario":
            stringa =f'update immobili set proprietario = {a[1]} where id = {a[2]}' 
        elif a[0]=="indirizzo":
            stringa =f'update immobili set indirizzo = "{a[1]}" where id = {a[2]}' 
        elif a[0]=="prezzo":
            stringa =f'update immobili set prezzo = {a[1]} where id = {a[2]}' 
        elif a[0]=="classe_energ":
            stringa =f'update immobili set classe_energ = {a[1]} where id = {a[2]}'
        else:
            return False
        #scrivo la modifica su DB
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute(stringa)
            
        return True

    # Le tre funzioni qui sotto possono essere raggruppate in una soltanto (fanno tutte solo la stampa di qualche dato della classe) - atempo debito!
    def stampa_caratteristiche(self):
        print(f"\nProprietario ID: {self.proprietario} \nsito in : {self.indirizzo} - \nClasse Energetica : {self.classe_energ} - \n Prezzo: {self.prezzo} \n Catalogo : {self.catalogo}")
        return True
    def stampa_catalogo(self, catalogo):
            if self.catalogo == catalogo:
                print(f"\nProprietario ID: {self.proprietario} \nsito in : {self.indirizzo} - \nClasse Energetica : {self.classe_energ} - \n Prezzo: {self.prezzo} \n Catalogo : {self.catalogo}")
            return  True
    def ricerca(self, ricerca):
        if self.indirizzo == ricerca:
            print(f"\nProprietario ID: {self.proprietario} \nsito in : {self.indirizzo} - \nClasse Energetica : {self.classe_energ} - \n Prezzo: {self.prezzo} \n Catalogo : {self.catalogo}")
       
    def salva_in_sqlite(self):
        global db_filename
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute('insert into immobili (proprietario, indirizzo, classe_energ, prezzo) values (?, ?, ?, ?)', (self.proprietario,  self.indirizzo, self.classe_energ, self.prezzo))
    def rem_sqlite(self, id):
            global db_filename
            with sqlite3.connect(db_filename) as conn:
                cursor = conn.cursor()
                cursor.execute(f'delete from immobili where id = {id}') # oppure posso prendere il dato da this:  cursor.execute('delete from immobili where id = {self.id}')

#Immagino di avere come Clienti anche affittuari quindi creo una classe base Cliente e altre classi come Proprietario piu' specifiche
class Cliente():
    """Classe Cliente contiene tutte le informazioni relative alla anagrafica Cliente """
    def __init__(self, id=None, nome=None, cognome=None, indirizzo=None, telefono=None):
        self.id=id
        self.nome=nome
        self.cognome=cognome
        self.indirizzo=indirizzo
        self.telefono=telefono
    def mod_attributo(self, a):
        pass
    def stampa_caratteristiche(self):
        print(f"\nID Cliente: {self.id} \nCliente Sig. {self.nome} {self.cognome} \nIndirizzo: {self.indirizzo} \nTelefono: {self.telefono}")
        return True
    
class Proprietario(Cliente):
    """La Classe Proprietario contiene tutte le info relative al Cliente proprietario di almeno un immobile """
    def __init__(self,id=None, nome=None, cognome=None, indirizzo=None, telefono=None, proprieta=None):
        super().__init__(id=id, nome=nome, cognome=cognome, indirizzo=indirizzo, telefono=telefono)
        self.proprieta = proprieta
    
    def salva_in_sqlite(self):
        global db_filename
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute('insert into clienti (nome, cognome, indirizzo, telefono, proprieta) values (?, ?, ?, ?, ?)', (self.nome, self.cognome, self.indirizzo, self.telefono, self.proprieta))
            
