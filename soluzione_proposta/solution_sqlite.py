import sqlite3
conn = sqlite3.connect('immobili.db')
curs = conn.cursor()
try:
    curs.execute("DROP table immobile")
    curs.execute("DROP table catalogo")
except:
    pass

curs.execute("CREATE table immobile (riferimento char(30), proprietario,char(30),indirizzo char(30), citta char(30), prezzo int, catalogo,char(30))")



class Catalogo():
    def __init__(self, nome, cursore):
        self.nome = nome
        self.immobili = list()
        self.cursore = cursore
    def aggiungi_immobile(self, immobile):
        self.immobili.append(immobile)
        row = (immobile.riferimento, immobile.proprietario, immobile.indirizzo,immobile.citta, immobile.prezzo, self.nome)
        self.cursore.execute("insert into immobile values(?, ?, ?, ?, ?, ?)",row)
        print("immobile aggiunto")
    def cancella_immobile(self, immobile):
        if immobile in self.immobili:
            self.immobili.delete(immobile)
            self.cursore.execute("delete from immobile where riferimento = ?",(immobile.riferimento,))
            print("immobile rimosso")
        else:   
            print("immobile non presente")
    def cerca_immobile(self, indirizzo):
        for immobile in self.immobili:
            if immobile.indirizzo == indirizzo:
                print("immobili trovati:")
                immobile.stampa_info()
                print("dal database:")
                self.cursore.execute("SELECT * FROM immobile WHERE indirizzo = ?",(immobile.indirizzo, ))
        for row in self.cursore.fetchall():
            print(row)
    def stampa_catalogo(self):
        for immobile in self.immobili:
            immobile.stampa_info()
            print("dal database:")
            self.cursore.execute("SELECT * FROM immobile")
            for row in self.cursore.fetchall():
                print(row)




