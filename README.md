# esame_immobili
NOTE:
Nelle 3 ore a disposizione non  mi e' stato possibile portare a termine l'esercizio (troppo poco tempo)

Al punto 1 interpreto che si richiede un software che funzioni senza salvare i dati su disco 
(di conseguenza ho utilizzato un sistema che si appoggia a liste per registrare i dati in ram)

Al punto 2 converto il sistem a all'uso con sqlite

AL punto 3  per poter estendere quanto gia' prodotto devo usare come ORM  Pickle che mi consente di salvare su disco una lista.
Non ho trovato una forma sufficiente per utilizzare PeeWee con quanto gia' sviluppato. Quindi per utilizzare PeeWee devo riprogettare tutto.

Il punto 4 deve essere fatto prima del punto 1 per poter fare i commit dei punti durante lo sviluppo

____ Per fare i punti 4 - 1 e 2 ho impiegato circa 10,5 h __

Aggiornamento:
Ho terminato anche il 3 punto - Tutto funziona regolarmente. circa  4h
La prossima volta parto da fondo pero'!!!


Testo delll'esame:

“Smart Manufacturing Developer 4.0 2020GL0058”
Testo:
Una agenzia immobiliare ha deciso di informatizzare i propri processi, in particolare vuole gestire il proprio catalogo di immobili. L'agenzia immobiliare ha inoltre manifestato l'esigenza volere anche una manutenzione successiva di detto software. 
Il candidato dovrà pertanto: 

1. progettare e realizzare in python, mediante tecniche di programmazione orientate agli oggetti, tale programma. 
Il programma in oggetto dovrà, in particolare, poter gestire (inserimento, modifica, cancellazione) gli immobili dell'agenzia con tutti i dettagli necessari (riferimento proprietario, indirizzo, prezzo, ecc), consentire una ricerca per indirizzo e una stampa a video di tutti gli immobili presenti nel software. 
Si aggiunga inoltre la possibilità di gestire diversi cataloghi di immobili (di prestigio, casa vacanza, popolari, ecc) in base alle caratteristiche (prezzo min, prezzo max) degli immobili. 
Ogni immobile può appartenere ad una solo catalogo; 

2. estendere il software aggiungendo la possibilità di salvare i dati in maniera permanente su un database locale (sqlite); 

3. estendere il software utilizzando un ORM (Object-relation Mapping: peewee) per agevolare la manutenzione successiva; 
4. creare un repository su github e utilizzarlo per tutte le fasi di lavorazione del software, creando almeno un commit distinto per ogni punto di cui sopra.
