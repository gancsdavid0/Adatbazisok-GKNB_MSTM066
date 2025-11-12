from menhely.models._base import Model
from dataclasses import dataclass
import datetime


@dataclass
class Dolgozo:
    id: int
    telephelyek_id: int
    keresztnev: str
    vezeteknev: str
    szuletesi_datum: str
    telefonszam: str
    email: str
    pozicio: str
    felvetel_datuma: str

class DolgozokModel(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {
                  "telephelyek_id": input("Telephely ID: "),
                  "keresztnev": input("Keresztnév: "),
                  "vezeteknev": input("Vezeteknev: "),
                  "szuletesi_datum": input("Születési dátum: "),
                  "telefonszam": input("Telefonszám: "),
                  "email": input("Email: "),
                  "pozicio": input("Pozíció: "),
                  "felvetel_datuma": datetime.datetime.now()
                }
        return params


    def getByID(self, id) -> Dolgozo | None:
        query = "SELECT * FROM dolgozok WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        return Dolgozo(result[0], result[1], result[2], result[3], result[4], result[5], result[6],
                result[7], result[8]) if result else None

    def create(self) -> Dolgozo:
        params = self._get_params()

        query = (
            "INSERT INTO dolgozok (telephelyek_id, keresztnev, vezeteknev, szuletesi_datum, telefonszam, email, pozicio, felvetel_datuma)"
            " VALUES (:telephelyek_id, :keresztnev, :vezeteknev, :szuletesi_datum, :telefonszam, :email, :pozicio, :felvetel_datuma)")

        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            new_id = cursor.lastrowid

            self.conn.commit()
            print(f'Dolgozó sikeresen felvéve! ID: {new_id}')
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba a dolgozó létrehozása közben: {e}")
            self.conn.rollback()
            return None

    def read(self) -> list[Dolgozo] | None:
        dolgozok = []
        cursor = self.conn.execute("SELECT * FROM dolgozok")
        rows = cursor.fetchall()
        for result in rows:
            dolgozok.append(
                Dolgozo(result[0], result[1], result[2], result[3], result[4], result[5], result[6],
                             result[7], result[8]))
        return dolgozok

    def update(self) -> None:
        for i in self.read():
            print(i.id, i.telephelyek_id, i.keresztnev, i.vezeteknev, i.szuletesi_datum, i.telefonszam, i.email, i.pozicio, i.felvetel_datuma)

        print("Melyiket szeretnéd módosítani?")

        try:
            id_to_update = int(input("ID: "))
        except ValueError as e:
            print("Hibás ID", e)
            return

        current_data = self.getByID(id_to_update)
        if not current_data:
            print("Hiba, nincsen ilyen dolgozó")
            return

        params = self._get_params()
        params["id"] = id_to_update

        sql = """
              UPDATE dolgozok \
              SET keresztnev            = :keresztnev, \
                  vezeteknev            = :vezeteknev, \
                  telephelyek_id        = :telephelyek_id, \
                  szuletesi_datum       = :szuletesi_datum, \
                  telefonszam           = :telefonszam, \
                  email                 = :email, \
                  pozicio               = :pozicio, \
                  felvetel_datuma       = :felvetel_datuma
              WHERE id = :id \
              """

        self.conn.execute(sql, params)
        self.conn.commit()

        print(f"\nA(z) {id_to_update} ID-jú dolgozó adatai sikeresen frissítve!")

    def delete(self, id) -> None:
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        sql = "DELETE FROM dolgozok WHERE id = :id"

        self.conn.execute(sql, {"id": id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")

    def get_kepesitesek_byid(self, id):
        current_data = self.getByID(id)
        if not current_data:
            print(f'Nem létezik ilyen rekord')
            return
        query = """
                SELECT 
                    kepesitesek.id,
                    kepesitesek.kepesites_neve,
                    kepesitesek.leiras
                FROM kepesitesek
                         INNER JOIN dolgozok_kepesitesek ON kepesitesek.id = dolgozok_kepesitesek.kepesitesek_id
                WHERE dolgozok_kepesitesek.dolgozok_id = ?
                """
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (current_data.id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Hiba a dolgozó képesítéseinek lekérdezése közben: {e}")
            return []
        finally:
            if cursor:
                cursor.close()