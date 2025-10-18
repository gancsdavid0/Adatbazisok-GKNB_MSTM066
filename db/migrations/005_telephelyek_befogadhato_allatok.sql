CREATE TABLE telephelyek_befogadhato_allatok
(
    id                     INT PRIMARY KEY                         NOT NULL,
    befogadhato_allatok_id INT REFERENCES befogadhato_allatok (id) NOT NULL,
    telephelyek_id         INT REFERENCES telephelyek (id)         NOT NULL,
    max_befogadhatosag     INT                                     NOT NULL
);
