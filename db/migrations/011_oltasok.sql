CREATE TABLE oltasok
(
    id                               INT PRIMARY KEY                                   NOT NULL,
    kisallat_egeszsegugyi_konyvek_id INT REFERENCES kisallat_egeszsegugyi_konyvek (id) NOT NULL,
    oltas_tipusa                     TEXT                                              NOT NULL,
    oltas_idopontja                  TEXT                                              NOT NULL,
    oltas_ervenyessege               TEXT                                              NOT NULL,
    allatorvos_neve                  TEXT                                              NOT NULL,
    megjegyzes                       TEXT                                              NOT NULL
);
