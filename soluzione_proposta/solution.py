class Immobile():
    def __init__(self, riferimento, prezzo, proprietario, indirizzo, citta):
        self.riferimento = riferimento
        self.prezzo = prezzo
        self.citta = citta
        self.indirizzo = indirizzo
        self.proprietario = proprietario
        def modifica_prezzo(self, prezzo):
            self.prezzo = prezzo
            print("prezzo aggiornato")
        def stampa_info(self):
            print("l'immobile in %s, %s costa %d" % (self.citta, self. indirizzo,self.prezzo))

class Catalogo():
    def __init__(self, nome):
        self.nome = nome
        self.immobili = list()
    def aggiungi_immobile(self, immobile):
        self.immobili.append(immobile)
        print("immobile aggiunto")
    def cancella_immobile(self, immobile):
        if immobile in self.immobili:
                self.immobili.delete(immobile)
                print("immobile rimosso")
        else:
            print("immobile non presente")
    def cerca_immobile(self, indirizzo):
        for immobile in self.immobili:
            if immobile.indirizzo == indirizzo:
                print("immobili trovati:")
                immobile.stampa_info()
    def stampa_catalogo(self):
        for immobile in self.immobili:
            immobile.stampa_info()

# creo un nuovo catalogo geenrale che contine tutti gli immobili
generale = Catalogo("generale")
casa1 = Immobile("1a", 200000, "Lelio Campanile", "Via Roma", "Aversa")
casa2 = Immobile("2a", 700000, "Caio", "Via dei Gracchi", "Roma")
generale.aggiungi_immobile(casa1)
generale.aggiungi_immobile(casa2)
generale.stampa_catalogo()
generale.cerca_immobile("Via Roma")


