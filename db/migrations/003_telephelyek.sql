CREATE TABLE telephelyek
(
    id       INTEGER PRIMARY KEY           AUTOINCREMENT,
    cimek_id INTEGER REFERENCES cimek (id) NOT NULL
);
