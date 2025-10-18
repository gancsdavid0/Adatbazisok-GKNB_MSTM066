CREATE TABLE kisallat_egeszsegugyi_konyvek
(
    id                     INT PRIMARY KEY                         NOT NULL,
    allatok_id             INT REFERENCES allatok (id)             NOT NULL,
    befogadhato_allatok_id INT REFERENCES befogadhato_allatok (id) NOT NULL,
    szuletesei_datum       TEXT,
    nev                    TEXT,
    ivar                   TEXT,
    suly                   REAL,
    meret                  TEXT,
    ivartalanitva          INT,
    szin                   TEXT,
    egeszsegi_allapot      TEXT,
    felvetel_datuma        TEXT,
    mikrochip_szama        INT
);
