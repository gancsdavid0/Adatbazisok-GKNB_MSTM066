CREATE TABLE orokbefogadasok
(
    id                   INTEGER PRIMARY KEY                   AUTOINCREMENT,
    allatok_id           INTEGER REFERENCES allatok (id)       NOT NULL,
    dolgozok_id          INTEGER REFERENCES dolgozok (id)      NOT NULL,
    orokbefogadok_id     INTEGER REFERENCES orokbefogadok (id) NOT NULL,
    telephelyek_id       INTEGER REFERENCES telephelyek (id)   NOT NULL,
    orokbefogadas_datuma TEXT                              NOT NULL
);
