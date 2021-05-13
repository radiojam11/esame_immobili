#Valerio Tognozzi
# Programma per la gestione Immobiliare
# 
# #
import testo 




def menu():
  """Menu grafico testuale per programma di gestione Immobili """
  x = 1
  while x !=0 :
    print ("                   Menu'")
    print("            Gestione Immobiliare")
    print(" INSERIMENTO IMMOBILE  .....digita 1 --> ")
    print(" MODIFICA IMMOBILE     .....digita 2 --> ")
    print(" CANCELLA IMMOBILE     .....digita 3 --> ")
    print(" STAMPA CATALGO IMMOBIBILI..digita 4 --> ")
    print(" INSERISCI NUOVO CLIENTE....digita 5 --> ")
    print(" STAMPA ANAGRAFICA CLIENTI..digita 6 --> ")
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
    elif x == "0":
      x = 0
    else:
      print(" Scelta non valida - solo numeri da 0 a 6")
      x = 1
  print("Hai scelto di uscire, Grazie!")
  return 0

class Immobile():
    catalogo = "X"
    def __init__(self, proprietario=None, indirizzo=None, prezzo=None, classe_energ=None):
        self.proprietario=proprietario
        self. indirizzo=indirizzo
        self.prezzo=prezzo
        self.classe_energ=classe_energ
    def mod_attributo(self, a): # a riceve una tupla(attributo_da_modificare, nuovo_valore_attributo)
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


#Immagino di avere come Clienti anche affittuari quindi creo una classe base Cliente e altre classi come Proprietario piu' specifiche
class Cliente():
    def __init__(self, nome=None, cognome=None, indirizzo=None, telefono=None):
        self.nome=nome
        self.cognome=cognome
        self.indirizzo=indirizzo
        self.telefono=telefono
    def mod_attributo(self, a):
        pass

class Proprietario(Cliente):
    def __init__(self, nome=None, cognome=None, indirizzo=None, telefono=None, proprieta=None):
        super().__init__(nome=nome, cognome=cognome, indirizzo=indirizzo, telefono=None)
        self.proprieta
        
        

def main():
    cont = 0
    if cont == 0:
        print(testo.banner)
        cont = 1
    scelta = menu()
    immobili=[]
    # INSERIMENTO IMMOBILE
    if scelta == 1:
        proprietario = input("inserisci ID proprietario : ")
        indirizzo = input("inserisci indirizzo immobile : ")
        prezzo = input(" inserisci il prezzo dell'immobile : ")
        classe_energ = input("inserisci classe energetica dell'immobile (A - B - ..- G) : ")
        immobile = Immobile(proprietario=proprietario, indirizzo= indirizzo, prezzo = prezzo, classe_energ=classe_energ)
        immobili.append(immobile)
        input("digita un tasto per continuare.....")
    elif scelta == 2:
        # MODIFICA IMMOBILE
        for n, el in enumerate (immobili):
            print(n, el.proprietario, el.indirizzo)
        imm = input("Quale immobile vuoi modificare ? : ")
        
        sel = input("seleziona quale voce modificare p(propietario) - i(indirizzo) - z(prezzo) - c(classe energetica) : ")
        if sel == "p":
            proprietario = input("inserisci ID proprietario : ")
            immobili[imm-1].mod_attributo(a=("proprietario", proprietario )
        elif sel == "i":
            indirizzo = input("inserisci indirizzo immobile : ")
            immobili[imm-1].mod_attributo(a=("indirizzo", indirizzo ))
        elif sel == "z":
            prezzo = input(" inserisci il prezzo dell'immobile : ")
            immobili[imm-1].mod_attributo(a=("prezzo", prezzo ))
        elif sel == "c":
            classe_energ = input("inserisci classe energetica dell'immobile (A - B - ..- G) : ")
            immobili[imm-1].mod_attributo(a=("classe_energ", classe_energ ))

    elif scelta == 3:
        # CANCELLAZIONE IMMOBILE
        pass
    elif scelta == 4:
        # STAMPA CATALOGO IMMOBILI
        pass

    elif scelta == 5:
        # INSERISCI NUOVO CLIENTE
        pass

    elif scelta == 6:
        # STAMPA ANAGRAFICA CLIENTE
        pass

    else:
        pass

if __name__ == '__main__':
    while True:
    	main()