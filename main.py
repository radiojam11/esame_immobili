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



def main():
    print(testo.banner)
    print("sono qui")
    scelta = menu()
    if scelta == 1:
        print("scelta 1")
    elif scelta == 2:
        pass
    else:
        pass

if __name__ == '__main__':
	main()