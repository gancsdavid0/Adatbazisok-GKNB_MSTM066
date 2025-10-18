CREATE TABLE allatok
(
    id              INT PRIMARY KEY                 NOT NULL,
    telephelyek_id  INT REFERENCES telephelyek (id) NOT NULL,
    felvetel_datuma TEXT                            NOT NULL
);
