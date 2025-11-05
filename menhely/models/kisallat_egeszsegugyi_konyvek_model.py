from menhely.models._base import Model
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Kiskonyv:
    id: int
    allatok_id: int
    befogadhato_allatok_id: int
    szuletesi_datum: str
    nev: str
    ivar: str
    suly: float
    meret: str
    ivartalanitva: int
    szin: str
    egeszsegi_allapot: str
    felvetel_datuma: str
    mikrochip_szama: int

class KiskonyvekModel(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        pass


    def getByID(self, id) -> Kiskonyv | None:
        query = "SELECT * FROM kisallat_egeszsegugyi_konyvek WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        return Kiskonyv(result[0], result[1], result[2], result[3], result[4], result[5], result[6],
                result[7], result[8], result[9], result[10], result[11], result[12]) if result else None

    def create(self) -> Kiskonyv:
        params = self._get_params()

        query = (
            "INSERT INTO kisallat_egeszsegugyi_konyvek (allatok_id, befogadhato_allatok_id, szuletesei_datum, nev, ivar, suly, meret, ivartalanitva, szin, egeszsegi_allapot, felvetel_datuma, mikrochip_szama)"
            " VALUES (:allatok_id, :befogadhato_allatok_id, :szuletesei_datum, :nev, :ivar, :suly, :meret, :ivartalanitva, :szin, :egeszsegi_allapot, :felvetel_datuma, :mikrochip_szama)")

        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            new_id = cursor.lastrowid

            self.conn.commit()
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba a kiskönyv létrehozása közben: {e}")
            self.conn.rollback()
            return None

    def read(self) -> list[Kiskonyv] | None:
        konyvek = []
        cursor = self.conn.execute("SELECT * FROM kisallat_egeszsegugyi_konyvek")
        rows = cursor.fetchall()
        for result in rows:
            konyvek.append(
                Kiskonyv(result[0], result[1], result[2], result[3], result[4], result[5], result[6],
                result[7], result[8], result[9], result[10], result[11], result[12]))
        return konyvek

    def update(self) -> None:
        for i in self.read():
            print(i.id, i.allatok_id, i.befogadhato_allatok_id, i.szuletesi_datum, i.nev, i.ivar, i.suly, i.meret, i.ivartalanitva,
                  i.szin, i.egeszsegi_allapot, i.felvetel_datum, i.mikrochip_szama)

        print("Melyiket szeretnéd módosítani?")

        try:
            id_to_update = int(input("ID: "))
        except ValueError as e:
            print("Hibás ID", e)
            return

        current_data = self.getByID(id_to_update)
        if not current_data:
            print("Hiba, nincsen ilyen kiskönyv")
            return

        params = self._get_params()
        params["id"] = id_to_update

        sql = """
              UPDATE kisallat_egeszsegugyi_konyvek \
              SET allatok_id                = :allatok_id, \
                  befogadhato_allatok_id    = :befogadhato_allatok_id, \
                  nev                       = :nev, \
                  ivar                      = :ivar, \
                  suly                      = :suly, \
                  meret                     = :meret, \
                  ivartalanitva             = :ivartalanitva, \
                  szin                      = :szin, \
                  egeszsegi_allapot         = :egeszsegi_allapot, \
                  felvetel_datuma           = :felvetel_datma, \
                 mikrochip_szama            = :mikrochip_szama
              WHERE id = :id \
              """

        self.conn.execute(sql, params)
        self.conn.commit()

        print(f"\nA(z) {id_to_update} ID-jú kiskönyv adatai sikeresen frissítve!")

    def delete(self, id) -> None:
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        sql = "DELETE FROM kisallat_egeszsegugyi_konyvek WHERE id = :id"

        self.conn.execute(sql, {"id": id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")


