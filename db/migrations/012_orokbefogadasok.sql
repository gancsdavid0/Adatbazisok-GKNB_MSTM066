CREATE TABLE orokbefogadasok
(
    id                   INT PRIMARY KEY                   NOT NULL,
    allatok_id           INT REFERENCES allatok (id)       NOT NULL,
    dolgozok_id          INT REFERENCES dolgozok (id)      NOT NULL,
    orokbefogadok_id     INT REFERENCES orokbefogadok (id) NOT NULL,
    telephelyek_id       INT REFERENCES telephelyek (id)   NOT NULL,
    orokbefogadas_datuma TEXT                              NOT NULL
);
