import peewee
db = peewee.SqliteDatabase("immobili_peewee.db")
class CatalogoImmobili(peewee.Model):
    riferimento = peewee.CharField()
    proprietario = peewee.CharField()
    indirizzo = peewee.CharField()
    citta = peewee.CharField()
    prezzo = peewee.IntegerField()
    catalogo = peewee.CharField()

    class Meta:
        database = db
        db_table = 'immobili'

CatalogoImmobili.create_table(CatalogoImmobili)
casa1 = CatalogoImmobili.create(riferimento = "1a",prezzo = 200000,proprietario = "Lelio Campanile",indirizzo= "Via Roma", citta = "Aversa",catalogo = "generale")

casa2 = CatalogoImmobili.create(riferimento="2a",prezzo = 700000, proprietario= "Caio",indirizzo = "Via dei Gracchi", citta= "Roma",catalogo = "generale")
casa1.save()
casa2.save()
immobili = CatalogoImmobili.select()
for immobile in immobili:
    print(immobile.riferimento, immobile.proprietario)  