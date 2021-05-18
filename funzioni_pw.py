
from main_peewee import *
from classi_pw import *



########################--------------------------Punto 3 PeeWee ---------------------------
def inserisci_immobile_pw():
      # inserire se vuoi la stampa della lista clienti
      s = input("Vuoi la lista dei Clienti per scegliere il ID CLiente? (S/N)")
      if s == "S" or s =="s":
            cli = 1
      ImmobileFactory.create_immobile(2, "via grattaceli 111", 19000, "B")

def modifica_immobile_pw():
      pass
def cancella_immobile_pw():
      pass
def stampa_immobili_pw():
      pass
def inserisci_cliente_pw():
      """La Funzione inserisce il nuovo Cliente con PeeWee CASO 3 esercitazione """
      nome = input("inserisci nome Cliente : ")
      cognome = input("inserisci cognome Cliente : ")
      indirizzo = input("inserisci indirizzo Cliente : ")
      telefono = input(" inserisci il telefono dell'Cliente : ")
      proprieta = input("inserisci ID proprita Cliente")
      #cliente_pw = Proprietario_pw(nome=nome, cognome=cognome, indirizzo= indirizzo, telefono=telefono, proprieta=proprieta)
      pass
def stampa_anagrafica_cliente_pw():
      query = Cliente.select()
      for el in query:
            print("Nome:", el.nome)
def cerca_immobile_pw():
      pass
def stampa_catalogo_pw():
      pass


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

