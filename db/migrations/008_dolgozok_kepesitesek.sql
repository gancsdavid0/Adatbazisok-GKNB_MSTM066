CREATE TABLE dolgozok_kepesitesek
(
    id             INTEGER PRIMARY KEY                 AUTOINCREMENT,
    dolgozok_id    INTEGER REFERENCES dolgozok (id)    NOT NULL,
    kepesitesek_id INTEGER REFERENCES kepesitesek (id) NOT NULL
);
