CREATE TABLE dolgozok
(
    id              INT PRIMARY KEY                 NOT NULL,
    telephelyek_id  INT REFERENCES telephelyek (id) NOT NULL,
    keresztnev      TEXT                            NOT NULL,
    vezeteknev      TEXT                            NOT NULL,
    szuletesi_datum TEXT                            NOT NULL,
    telefonszam     TEXT                            NOT NULL,
    email           TEXT                            NOT NULL,
    pozicio         TEXT                            NOT NULL,
    felvetel_datuma TEXT                            NOT NULL
);
