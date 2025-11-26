import datetime
from ._base import Model
from dataclasses import dataclass

@dataclass
class Orokbefogado:
    id: int
    keresztnev: str
    vezeteknev: str
    szuletesi_datum: str
    telefonszam: str
    email: str
    lakcim: str
    felvetel_datuma: str
    azonosito_okmany_szam: str

class OrokbefogadokModel(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {"keresztnev": input("Keresztnév: "), "vezeteknev": input("Vezeteknev: "),
                  "szuletesi_datum": input("Születési dátum: "), "telefonszam": input("Telefonszám: "),
                  "email": input("Email: "), "lakcim": input("Lakcím: "), "felvetel_datuma": datetime.date.today(),
                  "azonosito_okmany_szam": input("Azonosító okmány száma: ")}
        return params

    def getByID(self, id) -> Orokbefogado | None:
        query = "SELECT * FROM orokbefogadok WHERE id = ?"

        result = self.conn.execute(query, (id,)).fetchone()

        return Orokbefogado(result[0], result[1], result[2], result[3], result[4], result[5], result[6],
                                        result[7], result[8]) if result else None

    def create(self) -> Orokbefogado | None:
        params = self._get_params()

        query = ("INSERT INTO orokbefogadok (keresztnev, vezeteknev, szuletesi_datum, telefonszam, email, lakcim, felvetel_datuma, azonosito_okmany_szam)"
                 " VALUES (:keresztnev, :vezeteknev, :szuletesi_datum, :telefonszam, :email, :lakcim, :felvetel_datuma, :azonosito_okmany_szam)")

        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            new_id = cursor.lastrowid

            self.conn.commit()
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba az örökbefogadó létrehozása közben: {e}")
            self.conn.rollback()
            return None

    def read(self) -> list[Orokbefogado]:
        orokbefogado = []
        cursor = self.conn.execute("SELECT * FROM orokbefogadok")
        rows = cursor.fetchall()

        for result in rows:
            orokbefogado.append(Orokbefogado(result[0], result[1], result[2], result[3], result[4], result[5], result[6],
                                        result[7], result[8]))
        return orokbefogado

    def update(self):
        for i in self.read():
            print(i.id, i.keresztnev, i.vezeteknev, i.szuletesi_datum, i.telefonszam, i.email, i.lakcim, i.felvetel_datuma, i.azonosito_okmany_szam)

        print("Melyiket szeretnéd módosítani?")

        try:
            id_to_update = int(input("ID: "))
        except ValueError as e:
            print("Hibás ID", e)
            return

        current_data = self.getByID(id_to_update)
        if not current_data:
            print("Hiba, nincsen ilyen örökbefogadó")
            return

        params = self._get_params()
        params["id"] = id_to_update

        sql = """
              UPDATE orokbefogadok \
              SET keresztnev            = :keresztnev, \
                  vezeteknev            = :vezeteknev, \
                  szuletesi_datum       = :szuletesi_datum, \
                  telefonszam           = :telefonszam, \
                  email                 = :email, \
                  lakcim                = :lakcim, \
                  felvetel_datuma       = :felvetel_datuma, \
                  azonosito_okmany_szam = :azonosito_okmany_szam
              WHERE id = :id \
              """

        self.conn.execute(sql, params)
        self.conn.commit()

        print(f"\nA(z) {id_to_update} ID-jú örökbefogadó adatai sikeresen frissítve!")

    def delete(self, id):
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        sql = "DELETE FROM orokbefogadok WHERE id = :id"

        self.conn.execute(sql, {"id":id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")