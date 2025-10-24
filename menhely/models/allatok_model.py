from typing import Any

from menhely.models._base import Model
from dataclasses import dataclass
from menhely.models.orokbefogadok_model import Orokbefogado

@dataclass
class Allatok:
    id: int
    nev: str
    szuletesi_ido: str
    ivar: str
    suly: float
    meret: str
    szin: str
    ivartalanitva: bool
    egeszsegi_allapot: str
    mikrochip_szam: int


class AllatokModel(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {"nev": input("Név: "), "szuletesi_ido": input("Születési idő: "),
                  "ivar": input("Ivar: "), "suly": input("Suly: "),
                  "meret": input("Méret: "), "szin": input("Szín: "), "ivartalanitva": input("Ivartalanytva: "),
                  "egeszsegi_allapot": input("Egészségi állapot: "), "mikrochip_szam": input("Mikrochip száma:")}
        return params

    def getByID(self, id) -> Allatok | None:
        query = ("""SELECT allatok.id,
                           kisallat_egeszsegugyi_konyvek.nev,
                           kisallat_egeszsegugyi_konyvek.szuletesei_datum,
                           kisallat_egeszsegugyi_konyvek.ivar,
                           kisallat_egeszsegugyi_konyvek.suly,
                           kisallat_egeszsegugyi_konyvek.meret,
                           kisallat_egeszsegugyi_konyvek.szin,
                           kisallat_egeszsegugyi_konyvek.ivartalanitva,
                           kisallat_egeszsegugyi_konyvek.egeszsegi_allapot,
                           kisallat_egeszsegugyi_konyvek.mikrochip_szama
                    FROM allatok
                             INNER JOIN kisallat_egeszsegugyi_konyvek
                                        ON allatok.id = kisallat_egeszsegugyi_konyvek.allatok_id
                    WHERE allatok.id = :id""")

        result = self.conn.execute(query, (id,)).fetchone()

        return Allatok(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]) if result else None

    def create(self) -> Allatok:
        pass

    def read(self) -> list[Allatok] | None:
        allatok = []

        query = ("""SELECT allatok.id,
                           kisallat_egeszsegugyi_konyvek.nev,
                           kisallat_egeszsegugyi_konyvek.szuletesei_datum,
                           kisallat_egeszsegugyi_konyvek.ivar,
                           kisallat_egeszsegugyi_konyvek.suly,
                           kisallat_egeszsegugyi_konyvek.meret,
                           kisallat_egeszsegugyi_konyvek.szin,
                           kisallat_egeszsegugyi_konyvek.ivartalanitva,
                           kisallat_egeszsegugyi_konyvek.egeszsegi_allapot,
                           kisallat_egeszsegugyi_konyvek.mikrochip_szama
                    FROM allatok
                             INNER JOIN kisallat_egeszsegugyi_konyvek
                                        ON allatok.id = kisallat_egeszsegugyi_konyvek.allatok_id""")

        cursor = self.conn.execute(query)
        rows = cursor.fetchall()
        for result in rows:
            allatok.append(Allatok(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]))

        return allatok if allatok else None

    def update(self) -> None:
        pass

    def delete(self, id) -> None:
        pass

    def orokbefogadhato_allatok(self) -> list[Allatok] | None:
        allatok = []
        query = ("""SELECT allatok.id,
                           kisallat_egeszsegugyi_konyvek.nev,
                           kisallat_egeszsegugyi_konyvek.szuletesei_datum,
                           kisallat_egeszsegugyi_konyvek.ivar,
                           kisallat_egeszsegugyi_konyvek.suly,
                           kisallat_egeszsegugyi_konyvek.meret,
                           kisallat_egeszsegugyi_konyvek.szin,
                           kisallat_egeszsegugyi_konyvek.ivartalanitva,
                           kisallat_egeszsegugyi_konyvek.egeszsegi_allapot,
                           kisallat_egeszsegugyi_konyvek.mikrochip_szama
                    FROM allatok 
                        LEFT JOIN orokbefogadasok ON allatok.id = orokbefogadasok.allatok_id 
                        INNER JOIN kisallat_egeszsegugyi_konyvek ON allatok.id = kisallat_egeszsegugyi_konyvek.allatok_id
                    WHERE orokbefogadasok.allatok_id IS NULL""")

        cursor = self.conn.execute(query)
        rows = cursor.fetchall()
        for result in rows:
            allatok.append(Allatok(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]))

        return allatok if allatok else None

    def orokbefogadott_allatok(self) -> tuple[Allatok, Orokbefogado] | None:
        allatok = []
        query = ("""SELECT
                        kisallat_egeszsegugyi_konyvek.id,
                        kisallat_egeszsegugyi_konyvek.nev,
                        kisallat_egeszsegugyi_konyvek.szuletesei_datum,
                        kisallat_egeszsegugyi_konyvek.ivar,
                        kisallat_egeszsegugyi_konyvek.suly,
                        kisallat_egeszsegugyi_konyvek.meret,
                        kisallat_egeszsegugyi_konyvek.szin,
                        kisallat_egeszsegugyi_konyvek.ivartalanitva,
                        kisallat_egeszsegugyi_konyvek.egeszsegi_allapot,
                        kisallat_egeszsegugyi_konyvek.mikrochip_szama,
                        orokbefogadok.id,
                        orokbefogadok.keresztnev,
                        orokbefogadok.vezeteknev, 
                        orokbefogadok.szuletesi_datum, 
                        orokbefogadok.telefonszam,
                        orokbefogadok.email, 
                        orokbefogadok.lakcim,
                        orokbefogadok.felvetel_datuma,
                        orokbefogadok.azonosito_okmany_szam
                    FROM allatok 
                        LEFT JOIN orokbefogadasok ON allatok.id = orokbefogadasok.allatok_id 
                        INNER JOIN kisallat_egeszsegugyi_konyvek ON allatok.id = kisallat_egeszsegugyi_konyvek.allatok_id
                        INNER JOIN orokbefogadok ON orokbefogadok.id = orokbefogadasok.orokbefogadok_id
                    WHERE orokbefogadasok.allatok_id IS NOT NULL""")
        cursor = self.conn.execute(query)
        rows = cursor.fetchall()
        for result in rows:
            print(result[10], result[11], result[12], result[13], result[14], result[15], result[16], result[17])
            allatok.append((
                Allatok(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]),
                Orokbefogado(result[10], result[11], result[12], result[13], result[14], result[15], result[16], result[17], result[18])
            ))
        return allatok if allatok else None

    def orokbefogadas(self) -> tuple[Allatok, Orokbefogado] | None:
        #TODO Telephelyek és dolgozók tábla _base function létrehozása
        pass