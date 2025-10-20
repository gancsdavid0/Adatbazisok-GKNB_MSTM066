CREATE TABLE allatok
(
    id              INTEGER PRIMARY KEY                 AUTOINCREMENT,
    telephelyek_id  INTEGER REFERENCES telephelyek (id) NOT NULL,
    felvetel_datuma TEXT                            NOT NULL
);
