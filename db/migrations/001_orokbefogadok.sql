CREATE TABLE orokbefogadok
(
    id                    INT primary key NOT NULL,
    keresztnev            TEXT            NOT NULL,
    vezeteknev            TEXT            NOT NULL,
    szuletesi_datum       TEXT            NOT NULL,
    telefonszam           TEXT            NOT NULL,
    email                 TEXT            NOT NULL,
    lakcim                TEXT            NOT NULL,
    felvetel_datuma       TEXT            NOT NULL,
    azonosito_okmany_szam TEXT            NOT NULL
);
