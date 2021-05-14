#Valerio Tognozzi
# Programma per la gestione Immobiliare
# 
# #
import testo 
cont = 0
clienti = []
immobili = []


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
            print(self.telefono)
            cursor.execute('insert into clienti (nome, cognome, indirizzo, telefono, proprieta) values (?, ?, ?, ?, ?)', (self.nome, self.cognome, self.indirizzo, self.telefono, self.proprieta))
            


# LE FUNZIONI
def menu():
  """Menu grafico testuale per programma di gestione Immobili """
  x = 1
  while x !=0 :
    print ("                   Menu'")
    print("            Gestione Immobiliare")
    print(" INSERIMENTO IMMOBILE  .........digita 1 --> ")
    print(" MODIFICA IMMOBILE     .........digita 2 --> ")
    print(" CANCELLA IMMOBILE     .........digita 3 --> ")
    print(" STAMPA TUTTI GLI IMMOBILI......digita 4 --> ")
    print(" INSERISCI NUOVO CLIENTE........digita 5 --> ")
    print(" STAMPA ANAGRAFICA CLIENTI......digita 6 --> ")
    print(" CERCA IMMOBILE PER INDIRIZZO...digita 7 --> ")
    print(" STAMPA IMMOBILI PER CATALOGO...digita 8 --> ")
    print("\n")
    print(" PER USCIRE ................digita 0 --> ")
    print("\n\n")
    x = input("scegli cosa vuoi fare digita 0 per uscire............... --> ")
    if x == "1":
      return 1
    elif x == "2":
      return 2
    elif x == "3":
      return 3
    elif x == "4":
      return 4
    elif x == "5":
      return 5
    elif x == "6":
      return 6
    elif x == "7":
      return 7
    elif x == "8":
      return 8
    elif x == "0":
      x = 0
      exit(222)
    else:
      print(" Scelta non valida - solo numeri da 0 a 6")
      x = 1
  print("Hai scelto di uscire, Grazie!")
  return 0
        

def main():
    """ Funzione principale"""
    global cont
    if cont == 0:
        print(testo.banner)
        cont = 1
    scelta = menu()
    global clienti
    global immobili
    # INSERIMENTO IMMOBILE
    if scelta == 1:
        proprietario = input("inserisci ID proprietario : ")
        indirizzo = input("inserisci indirizzo immobile : ")
        prezzo = input(" inserisci il prezzo dell'immobile : ")
        classe_energ = input("inserisci classe energetica dell'immobile (A - B - ..- G) : ")
        immobile = Immobile(proprietario=proprietario, indirizzo= indirizzo, prezzo = prezzo, classe_energ=classe_energ)
        immobili.append(immobile)
        immobile.salva_in_sqlite()
        #ricarico la lista
        sqlite_start()
        input("digita un tasto per continuare.....")
    elif scelta == 2:
        # MODIFICA IMMOBILE
        for n, el in enumerate (immobili):
            print(f"\nElemento Lista: {n} -\nID db: {el.id} - Proprietario: {el.proprietario} -\nIndirizzo: {el.indirizzo} \nPrezzo: {el.prezzo} - Classe En.: {el.classe_energ}\n\n")
        imm = int(input("Quale Elemento Lista immobile vuoi modificare ? : "))
        sel = input("seleziona quale voce modificare p(propietario) - i(indirizzo) - z(prezzo) - c(classe energetica) : ")
        if sel == "p":
            proprietario = input("inserisci ID proprietario : ")
            # La tupla si trasforma rispetto alla versione base - viene aggiunto l'elemento ID x la query corretta
            immobili[imm].mod_sqlite(a=("proprietario", str(proprietario), str(el.id) ))
        elif sel == "i":
            indirizzo = input("inserisci indirizzo immobile : ")
            #immobili[imm].mod_attributo(a=("indirizzo", indirizzo ))
            immobili[imm].mod_sqlite(a=("indirizzo", indirizzo, str(el.id) ))
        elif sel == "z":
            prezzo = input("inserisci il prezzo dell'immobile : ")
            #immobili[imm].mod_attributo(a=("prezzo", prezzo ))
            immobili[imm].mod_sqlite(a=("prezzo", prezzo, str(el.id) ))
        elif sel == "c":
            classe_energ = input("inserisci classe energetica dell'immobile (A - B - ..- G) : ")
            #immobili[imm].mod_attributo(a=("classe_energ", classe_energ ))
            immobili[imm].mod_sqlite(a=("classe_energ", classe_energ, str(el.id) ))
        #Ricarico la lista pulita ed aggiornata
        sqlite_start()
        print(" modifica con successo")

    elif scelta == 3:
        # CANCELLAZIONE IMMOBILE
        for n, el in enumerate (immobili):
            print(f"\nElemento Lista: {n} -\nID db: {el.id} - Proprietario: {el.proprietario} -\nIndirizzo: {el.indirizzo} \nPrezzo: {el.prezzo} - Classe En.: {el.classe_energ}\n\n")
        imm = int(input("Quale immobile vuoi Cancellare ? : "))
        #immobili.pop(imm)
        #Modificato sistema Cancellazione - adesso cancello da DB e ricarico liste a fine operazione
        #chiamo modulo specifico e passo numero id da cancellare
        immobili[imm].rem_sqlite(str(el.id) )
        #ricarico la lista pulita ed aggiornata
        sqlite_start()
        input("digita un tasto per continuare.....")
        pass
        
    elif scelta == 4:
        # STAMPA CATALOGO IMMOBILI
        for el in immobili:
            el.stampa_caratteristiche()
            print("------------------------")
        input("digita un tasto per continuare.....")

    elif scelta == 5:
        # INSERISCI NUOVO CLIENTE
        nome = input("inserisci nome Cliente : ")
        cognome = input("inserisci cognome Cliente : ")
        indirizzo = input("inserisci indirizzo Cliente : ")
        telefono = input(" inserisci il telefono dell'Cliente : ")
        proprieta = input("inserisci ID proprita Cliente")
        cliente = Proprietario(nome=nome, cognome=cognome, indirizzo= indirizzo, telefono=telefono, proprieta=proprieta)
        clienti.append(cliente)
        cliente.salva_in_sqlite()
        #ricarico la lista pulita ed aggiornata
        sqlite_start()
        input("digita un tasto per continuare.....")
    elif scelta == 6:
        # STAMPA ANAGRAFICA CLIENTE
        #print(clienti)
        for num, el in enumerate (clienti):
            el.stampa_caratteristiche()
            print("----------------------")
        input("digita un tasto per continuare.....")
    elif  scelta == 7:
        # CERCA IMMOBILE PER INDIRIZZO
        scel = input("Digita l'indirizzo da ricercare.... ")
        for el in immobili:
            el.ricerca(scel)
        input("digita un tasto per continuare.....")
    elif scelta == 8:
        # STAMPA CATALOGO
        scel = input("Quale catalogo vuoi stampare? o(Popolare) v(Vacanze, p(Prestigio)  ")
        for el in immobili:
            if scel == "o":
                el.stampa_catalogo("Popolare")
            elif scel == "v":
                el.stampa_catalogo("Vacanze")
            elif scel == "p":
                el.stampa_catalogo("Prestigio")
        input("digita un tasto per continuare.....")

    else:
        pass

def sqlite_start():
    """La funzione carica i dati della nostra immobiliare dal DB registrato su disco e li passa alle liste - clienti e immobili """
    global db_filename
    global clienti
    global immobili
    #ripulisco le liste per riempirle ex-novo ogni chiamata della funzione
    clienti = []
    immobili = []
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        # carico tutti i clienti eccetto ID 1 che e' il cliente ESEMPIO
        cursor.execute("""
        select id, nome, cognome, indirizzo, telefono, proprieta from clienti where id > 1
        """)
        #ciclo ogni riga - creo l'oggetto cliente - lo aggiungo alla lista clienti
        for row in cursor.fetchall():
            id, nome, cognome, indirizzo, telefono, proprieta = row
            cliente = Proprietario(id=id, nome=nome, cognome=cognome, indirizzo= indirizzo, telefono=telefono, proprieta=proprieta)
            clienti.append(cliente)

        # carico tutti gli immobili eccetto ID 1 che e' l'immobile di ESEMPIO
        cursor.execute("""
        select id, proprietario,  indirizzo, prezzo, classe_energ from immobili where id > 1
        """)
        #ciclo ogni riga - creo l'oggetto immobile - lo aggiungo alla lista immobili
        for row in cursor.fetchall():
            id, proprietario,  indirizzo, prezzo, classe_energ = row
            immobile = Immobile(id=id, proprietario=proprietario, indirizzo= indirizzo, prezzo = prezzo, classe_energ=classe_energ)
            immobili.append(immobile)


# MAIN
if __name__ == '__main__':
    sqlite_start() # carico i dati dal DB
    while True:
        main()