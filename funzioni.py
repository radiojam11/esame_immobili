from classi import *
from main import *

clienti = []
immobili = []

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
      
    else:
      print(" Scelta non valida - solo numeri da 0 a 8")
      x = 1
  print("Hai scelto di uscire, Grazie!")
  return 0


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
    return True

def inserisci_immobile():
    """la Funzione inserisce un nuovo immobile nellal ista (1Caso dell'esame) e inserisce un nuovo utente nel DB (2 caso del'esame)"""
    proprietario = input("inserisci ID proprietario : ")
    indirizzo = input("inserisci indirizzo immobile : ")
    prezzo = input(" inserisci il prezzo dell'immobile : ")
    classe_energ = input("inserisci classe energetica dell'immobile (A - B - ..- G) : ")
    immobile = Immobile(proprietario=proprietario, indirizzo= indirizzo, prezzo = prezzo, classe_energ=classe_energ)
    immobili.append(immobile)
    immobile.salva_in_sqlite()
    return True
def modifica_immobile():
        """ La Funzione e' predisposta per modificare gli attributi dell'immmobile dalla lista (nel 1 caso dell'esame) opppure per modificare gli attributi dell'immobile nel DB (2 caso dell'esame) """
        global clienti
        global immobili
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
        return True


def cancella_immobile():
    """La Funzione e' predisposta per eliminare un utente dalla lista (punto 1 dell'esercizio) o per cancella un utente dal DB (punto 2 del'esercizio)"""
    for n, el in enumerate (immobili):
        print(f"\nElemento Lista: {n} -\nID db: {el.id} - Proprietario: {el.proprietario} -\nIndirizzo: {el.indirizzo} \nPrezzo: {el.prezzo} - Classe En.: {el.classe_energ}\n\n")
    imm = int(input("Quale immobile vuoi Cancellare ? : "))
    #immobili.pop(imm)
    #Modificato sistema Cancellazione - adesso cancello da DB e ricarico liste a fine operazione
    #chiamo modulo specifico e passo numero id da cancellare
    immobili[imm].rem_sqlite(str(el.id) )
    #ricarico la lista pulita ed aggiornata
    return True

def stampa_immobili():
    """La Funzione stampa tutti gli immobili della lista """
    for el in immobili:
        el.stampa_caratteristiche()
        print("------------------------")
    return True

def inserisci_cliente():
    """La Funzione inserisce il nuovo Cliente in lista (per il punto 1 dell'esercizio) e lo salva nel DB (punto 2 dell'esercizio) """
    nome = input("inserisci nome Cliente : ")
    cognome = input("inserisci cognome Cliente : ")
    indirizzo = input("inserisci indirizzo Cliente : ")
    telefono = input(" inserisci il telefono dell'Cliente : ")
    proprieta = input("inserisci ID proprita Cliente")
    cliente = Proprietario(nome=nome, cognome=cognome, indirizzo= indirizzo, telefono=telefono, proprieta=proprieta)
    clienti.append(cliente)
    cliente.salva_in_sqlite()
    return True

def stampa_anagrafica_cliente():
    """La funzione stampa tutti i clienti presenti nella lista """
    for el in clienti:
            el.stampa_caratteristiche()
            print("----------------------")
    return True
        
def cerca_immobile():
    """La funzione cerca i'immobile in funzione dell'indirizzo (l'indirizzo deve essere esatto) """
    scel = input("Digita l'indirizzo da ricercare.... ")
    for el in immobili:
            el.ricerca(scel)
    return True

def stampa_catalogo():
    """La funzione itera la lista degli oggetti immobile e attua la scelta  di stampa dell'utente """
    scel = input("Quale catalogo vuoi stampare? o(Popolare) v(Vacanze, p(Prestigio)  ")
    for el in immobili:
        if scel == "o":
            el.stampa_catalogo("Popolare")
        elif scel == "v":
            el.stampa_catalogo("Vacanze")
        elif scel == "p":
            el.stampa_catalogo("Prestigio")
    return True