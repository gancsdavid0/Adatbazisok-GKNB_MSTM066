CREATE TABLE dolgozok_kepesitesek
(
    id             INT PRIMARY KEY                 NOT NULL,
    dolgozok_id    INT REFERENCES dolgozok (id)    NOT NULL,
    kepesitesek_id INT REFERENCES kepesitesek (id) NOT NULL
);
