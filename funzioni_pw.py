
from main_peewee import *
from classi_pw import *



########################--------------------------Punto 3 PeeWee ---------------------------
def inserisci_immobile_pw():
      # inserire se vuoi la stampa della lista clienti
      s = input("Vuoi la lista dei Clienti per scegliere il ID CLiente? (S/N)")
      if s == "S" or s =="s":
            stampa_anagrafica_cliente_pw()
      id_cliente = input("inserisci Id Cliente del proprietario dell'immobile: ")
      indirizzo = input("inserisci indirizzo dell'immobile : ")
      prezzo = input("inserisci il prezzo dell' immobile: ")
      classe = input("inserisci Classe Energetica dell'immobile: ")
      ImmobileFactory.create_immobile(int(id_cliente), indirizzo, int(prezzo), classe)
      return True

def modifica_immobile_pw():
      """La funzione riceve l' ID immobile da modificare e ne modifica un attibuto scelto dall'utente """
      s = input("Vuoi la lista degli immobili  per scegliere il ID Immobile da modificare? (S/N)")
      if s == "S" or s =="s":
            stampa_immobili_pw()
      s= input("Dammi ID Immobile da modificare -")
      immo = Immobile.select().where(Immobile.id == int(s)).get()
      scel = input("Cosa vuoi modificare?\ni=ID proprietario -\nd=Indirizzo -\np=Prezzo -\nc=ClasseEnergetica ")
      if scel == "i":
            #controllare se immo e' una lista va iterata se oggetto no
            id_cliente = (input("Dammi il nuovo ID Cliente del Proprietario -"))
            immo.cliente_id=int(id_cliente)
      elif scel ==  "d":
            new_indirizzo = input("Dammi il nuovo indirizzo dell'immobile -")
            immo.indirizzo = new_indirizzo
      elif scel == "p":
            new_prezzo = input("Dammi il nuovo prezzo dell'Immobile -")
            immo.prezzo = int(new_prezzo)
      elif scel == "c":
            new_classe = input("Dammi la nuova Classe Energetica dell'Immobile -")
            immo.classe_energ = new_classe
      immo.save()
      return True
      
def cancella_immobile_pw():
      """La funzione riceve ID immobile e cancella l'immobile """
      s = input("Vuoi la lista degli immobili  per scegliere il ID Immobile da cancellare? (S/N)")
      if s == "S" or s =="s":
            stampa_immobili_pw()
      s= input("Dammi ID Immobile da cancellare -")
      immo = Immobile.select().where(Immobile.id == int(s)).get()
      #Ovviamente qui si dovrebbe mettere un controllo prima di cancellare!!!!
      immo.delete_instance()
      return True
def stampa_immobili_pw():  
      """La funzione stampa l'intero catalogo """
      query = Immobile.select()
      print("*******************STAMPA COMPLETA IMMOBILI IN DB ******************")
      for el in query:
            print(f"ID Immobile: {el.id}\nIndirizzo: {el.indirizzo}\nPrezzo: {el.prezzo}\nClasse Energetica: {el.classe_energ}\nProprietario: {el.cliente_id}\n Catalogo: {el.catalogo_id}")
            print("------------------------------------------")
      return True
def inserisci_cliente_pw():
      """La Funzione inserisce il nuovo Cliente con PeeWee CASO 3 esercitazione """
      nome = input("inserisci nome Cliente : ")
      cognome = input("inserisci cognome Cliente : ")
      indirizzo = input("inserisci indirizzo Cliente : ")
      telefono = input(" inserisci il telefono dell'Cliente : ")
      tipo = input("inserisci Tipo Cliente: p=Proprietario a=Affittuario (p/a)")
      ClienteFactory.create_cliente(nome, cognome, indirizzo, telefono, tipo)
      return True
def stampa_anagrafica_cliente_pw():
      """La funzione stampa l'intero DB dei CLienti della agenzia """
      query = Cliente.select()
      print("*********************STAMPA CLIENTI AGENZIA****************************")
      for el in query:
            print(f"ID CLiente: {el.id}\nSig.\Sig.ra {el.nome} {el.cognome}\nIndirizzo: {el.indirizzo}\nTelefono: {el.telefono}\nTipo Cliente: {el.tipo_cliente}")
            print("------------------------------------------")
      return True
def cerca_immobile_pw():
      """La funzione ricerca per indirizzo nel DB l'immobile scelto dall'utente"""
      cerca = input("Quale indirizzo immobile vuoi cercare?? -")
      immo = Immobile.select().where(Immobile.indirizzo == cerca)  # da perfezionare la select
      print("*********************STAMPA RICERCA INDIRIZZO****************************")
      for el in immo:
            print(f"ID Immobile: {el.id}\nIndirizzo: {el.indirizzo}\nPrezzo: {el.prezzo}\nClasse Energetica: {el.classe_energ}\nProprietario: {el.cliente_id}")
            print("------------------------------------------")
      return True
def stampa_catalogo_pw():
      """La funzione stampa a video uno dei cataloghi disponibili scelto dall'utente """
      stampa = input("Quale catalogo vuoi Stampare ? p=Prestigio v=Casa Vacanze o=Popolare (p/v/o)? ")
      if stampa == "p":
            query = Immobile.select().where(Immobile.catalogo_id == "prestigio")
            print("*********************STAMPA IMMOBILI PREGIO****************************")
            for el in query:
                  print(f"ID Immobile: {el.id}\nIndirizzo: {el.indirizzo}\nPrezzo: {el.prezzo}\nClasse Energetica: {el.classe_energ}\nProprietario: {el.cliente_id}")
                  print("------------------------------------------")
      elif stampa == "o":
            query = Immobile.select().where(Immobile.catalogo_id == "casa vacanze")
            print("*********************STAMPA CASE VACANZE****************************")
            for el in query:
                  print(f"ID Immobile: {el.id}\nIndirizzo: {el.indirizzo}\nPrezzo: {el.prezzo}\nClasse Energetica: {el.classe_energ}\nProprietario: {el.cliente_id}")
                  print("------------------------------------------")
      else:
            query = Immobile.select().where(Immobile.catalogo == "popolare")
            print("*********************STAMPA IMMOBILI POPOLARI****************************")
            for el in query:
                  print(f"ID Immobile: {el.id}\nIndirizzo: {el.indirizzo}\nPrezzo: {el.prezzo}\nClasse Energetica: {el.classe_energ}\nProprietario: {el.cliente_id}")
                  print("------------------------------------------")
      return True

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
      clear_sceen()
      x = 1
  print("Hai scelto di uscire, Grazie!")
  return 0


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
        # quindi mi connetto al DB
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

def main():
    """ Funzione principale gestisce le scelte effettuate sul menu"""
    
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
        # chiudo il gas e vengo via!
        db_pw.close()
        exit(222)
    else:
        pass

def clear_sceen():
      """Pulisce lo schermo"""
      # for windows
      if os.name == 'nt':
            _ = os.system('cls')

      # for mac and linux(here, os.name is 'posix')
      else:
            _ = os.system('clear')