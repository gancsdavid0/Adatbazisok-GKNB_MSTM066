CREATE TABLE telephelyek_befogadhato_allatok
(
    id                     INTEGER PRIMARY KEY                         AUTOINCREMENT,
    befogadhato_allatok_id INTEGER REFERENCES befogadhato_allatok (id) NOT NULL,
    telephelyek_id         INTEGER REFERENCES telephelyek (id)         NOT NULL,
    max_befogadhatosag     INTEGER                                     NOT NULL
);
