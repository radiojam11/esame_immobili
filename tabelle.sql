create table immobili (
    id            integer primary key autoincrement not null,
    proprietario  text,
    indirizzo     text,
    prezzo        text,
    classe_energ  text
);

create table clienti (
    id            integer primary key autoincrement not null,
    nome          text,
    cognome       text,
    indirizzo     text,
    telefono      text,
    proprieta     text
);