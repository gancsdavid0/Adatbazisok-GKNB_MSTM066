CREATE TABLE telephelyek
(
    id       INT PRIMARY KEY           NOT NULL,
    cimek_id INT REFERENCES cimek (id) NOT NULL
);
