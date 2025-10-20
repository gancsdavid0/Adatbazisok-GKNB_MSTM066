CREATE TABLE kisallat_egeszsegugyi_konyvek
(
    id                     INTEGER PRIMARY KEY                         AUTOINCREMENT,
    allatok_id             INTEGER REFERENCES allatok (id)             NOT NULL,
    befogadhato_allatok_id INTEGER REFERENCES befogadhato_allatok (id) NOT NULL,
    szuletesei_datum       TEXT,
    nev                    TEXT,
    ivar                   TEXT,
    suly                   REAL,
    meret                  TEXT,
    ivartalanitva          INTEGER,
    szin                   TEXT,
    egeszsegi_allapot      TEXT,
    felvetel_datuma        TEXT,
    mikrochip_szama        INTEGER
);
