from datetime import datetime

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


    def create(self, befogadhato_allatok_id, telephelyek_id):
        most = datetime.now()
        egeszsegugyi_konyvek_create_query = """INSERT INTO kisallat_egeszsegugyi_konyvek
                                            (allatok_id, befogadhato_allatok_id, szuletesei_datum, nev, ivar, suly, meret, ivartalanitva, szin, egeszsegi_allapot, felvetel_datuma, mikrochip_szama) 
                                            VALUES
                                            (:allatok_id, :befogadhato_allatok_id, :szuletesei_datum, :nev, :ivar, :suly, :meret, :ivartalanitva, :szin, :egeszsegi_allapot, :felvetel_datuma, :mikrochip_szama)"""

        allatok_create_query = ("""INSERT INTO allatok 
                 (telephelyek_id, felvetel_datuma)
                 VALUES 
                 (:telephelyek_id, :felvetel_datuma)""")
        try:
            cursor = self.conn.cursor()
            params_allatok = {
                "telephelyek_id" : telephelyek_id,
                "felvetel_datuma" : most
            }
            cursor.execute(allatok_create_query, params_allatok)

            new_id = cursor.lastrowid
            params_konyv = {
                "allatok_id": new_id,
                "befogadhato_allatok_id": befogadhato_allatok_id,
                "szuletesei_datum": input("Születési dátum: "),
                "nev": input("Név: "),
                "ivar": input("Ivar: "),
                "suly": input("Suly: "),
                "meret": input("Méret: "),
                "ivartalanitva": input("Ivartalanítva: "),
                "szin": input("Szín: "),
                "egeszsegi_allapot": input("Egészségi állapot: "),
                "felvetel_datuma": most,
                "mikrochip_szama": input("Mikrochip száma:")
            }

            cursor.execute(egeszsegugyi_konyvek_create_query, params_konyv)
            print("Sikeres létrehozás!")
            self.conn.commit()

        except Exception as e:
            print(f"Hiba az örökbefogadás közben: {e}")
            self.conn.rollback()
            return None



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

    def update(self, id) -> None:
        allat = self.getByID(id)

        if allat is None:
            print("Nem található állat ilyen ID-val.")
            return

        print(f"--- {allat.nev} adatainak szerkesztése ---")
        print("(Ha nem akarsz módosítani egy értéket, csak nyomj ENTER-t!)")
        uj_nev = input(f"Név [{allat.nev}]: ") or allat.nev
        uj_szuletesi_ido = input(f"Születési idő [{allat.szuletesi_ido}]: ") or allat.szuletesi_ido
        uj_ivar = input(f"Ivar [{allat.ivar}]: ") or allat.ivar
        uj_suly_str = input(f"Súly [{allat.suly}]: ")
        uj_suly = float(uj_suly_str) if uj_suly_str else allat.suly
        uj_meret = input(f"Méret [{allat.meret}]: ") or allat.meret
        uj_szin = input(f"Szín [{allat.szin}]: ") or allat.szin
        uj_egeszsegi_allapot = input(f"Egészségi állapot [{allat.egeszsegi_allapot}]: ") or allat.egeszsegi_allapot
        uj_mikrochip_str = input(f"Mikrochip száma [{allat.mikrochip_szam}]: ")
        uj_mikrochip = uj_mikrochip_str if uj_mikrochip_str else allat.mikrochip_szam
        print(f"Jelenleg ivartalanítva: {'Igen' if allat.ivartalanitva else 'Nem'}")
        uj_ivartalanitva_str = input("Ivartalanítva (1=Igen, 0=Nem, Enter=Változatlan): ")

        query = """
                UPDATE kisallat_egeszsegugyi_konyvek
                SET nev               = :nev,
                    szuletesei_datum  = :szuletesei_datum,
                    ivar              = :ivar,
                    suly              = :suly,
                    meret             = :meret,
                    szin              = :szin,
                    ivartalanitva     = :ivartalanitva,
                    egeszsegi_allapot = :egeszsegi_allapot,
                    mikrochip_szama   = :mikrochip_szama
                WHERE allatok_id = :id
                """
        params = {
            "nev": uj_nev,
            "szuletesei_datum": uj_szuletesi_ido,  # Az adatbázisban 'szuletesei' az oszlop neve a kódod alapján
            "ivar": uj_ivar,
            "suly": uj_suly,
            "meret": uj_meret,
            "szin": uj_szin,
            "ivartalanitva": uj_ivartalanitva_str,
            "egeszsegi_allapot": uj_egeszsegi_allapot,
            "mikrochip_szama": uj_mikrochip,
            "id": id
        }
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            print("Sikeres frissítés!")

            # Visszaadjuk a frissített objektumot
            return self.getByID(id)

        except Exception as e:
            print(f"Hiba a frissítés közben: {e}")
            self.conn.rollback()
            return None
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
            allatok.append((
                Allatok(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]),
                Orokbefogado(result[10], result[11], result[12], result[13], result[14], result[15], result[16], result[17], result[18])
            ))
        return allatok if allatok else None

    def orokbefogadas(self, allatok_id , dolgozok_id, orokbefogadok_id, telephelyek_id):
        datum = datetime.now()
        params = {
            'allatok_id': allatok_id,
            'dolgozok_id': dolgozok_id,
            'orokbefogadok_id': orokbefogadok_id,
            'telephelyek_id': telephelyek_id,
            'datum': datum
        }
        query = ("INSERT INTO orokbefogadasok (allatok_id, dolgozok_id, orokbefogadok_id, telephelyek_id, orokbefogadas_datuma)"
                 "VALUES (:allatok_id, :dolgozok_id, :orokbefogadok_id, :telephelyek_id, :datum)")
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            new_id = cursor.lastrowid
            self.conn.commit()
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba az örökbefogadás közben: {e}")
            self.conn.rollback()
            return None