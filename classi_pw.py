############################ CLASSI PEEWEE   CASO 3 #################################
# Il sistema sviluppato con PeeWee si rivoluziona completamente.
# Lascio l'organizzazione basata su liste e lavoro completamente su DB
# #
import peewee
from main_peewee import *
from funzioni_pw import *


# indirizzo del file di DB peewee
nome_file_db = "immobiliare_pw.db"
db_pw = peewee.SqliteDatabase(nome_file_db)

# LE CLASSI

class Tipo_Cliente(peewee.Model):
    tipo_cliente = peewee.CharField(unique=True)
    class  Meta():
        database = db_pw

class Catalogo(peewee.Model):
    catalogo = peewee.CharField(unique=True)
    class  Meta():
        database = db_pw

class Cliente(peewee.Model):
    """Classe Cliente contiene tutte le informazioni del cliente della agenzia immobiliare """
    nome = peewee.CharField()
    cognome = peewee.CharField()
    indirizzo = peewee.CharField()
    telefono = peewee.CharField()
    tipo_cliente = peewee.ForeignKeyField(Tipo_Cliente, backref="tipi_cliente")
    class Meta:
        database = db_pw
        #db_table = "clienti"


class Immobile(peewee.Model):
    """Classe Immobile contiene tutte le informazioni relative all'immobile"""
    #proprietario=peewee.CharField()
    cliente_id=peewee.ForeignKeyField(Cliente, backref="clienti")
    indirizzo=peewee.CharField()
    prezzo=peewee.IntegerField()
    classe_energ=peewee.CharField()
    catalogo = peewee.ForeignKeyField(Catalogo, backref="cata")
    class Meta:
        database = db_pw
        #db_table = "immobili"



class ClienteFactory():
    @staticmethod
    def create_cliente(nome, cognome, indirizzo, telefono, tipo):
        if tipo == "p":
            tipo_cliente = Tipo_Cliente.select().where(Tipo_Cliente.tipo_cliente == "Proprietario").get()
        else: 
            tipo_cliente = Tipo_Cliente.select().where(Tipo_Cliente.tipo_cliente == "Affittuario").get()
        cliente = Cliente(nome = nome, cognome = cognome, indirizzo = indirizzo, telefono = telefono, tipo_cliente = tipo_cliente)
        cliente.save()


class ImmobileFactory():
    @staticmethod
    def create_immobile(cliente_id, indirizzo, prezzo, classe_energ):
        if prezzo <= 100000:
            catalogo = "popolare"
        elif prezzo >10000 and prezzo <= 250000:
            catalogo = "casa vacanze"
        else:
            catalogo = "prestigio"
        immobile = Immobile(cliente_id = cliente_id, indirizzo = indirizzo, prezzo = prezzo, classe_energ = classe_energ, catalogo = catalogo)
        immobile.save()

