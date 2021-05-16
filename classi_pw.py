############################ CLASSI PEEWEE   CASO 3 ##################################

# indirizzo del file di DB peewee
db_pw = peewee.SqliteDatabase("immobiliare.db")

# LE CLASSI
class Immobile_pw(peewee.Model):
    """Classe Immobile contiene tutte le informazioni relative all'immobile"""
    proprietario=peewee.CharField()
    indirizzo=peewee.CharField()
    prezzo=peewee.CharField()
    classe_energ=peewee.CharField()
    catalogo = peewee.CharField()
    
    class Meta:
        databese = db_pw
        db_table = "immobili"
    """
    if int(prezzo) <=100000:
        cat = "Popolare"
    elif int(prezzo) > 100000 and int(prezzo) <= 250000:
        cat = "Vacanze"
    else:
        cat = "Prestigio"
    catalogo = cat
    """

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

