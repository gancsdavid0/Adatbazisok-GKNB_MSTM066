from menhely.models._base import Model
from dataclasses import dataclass

@dataclass
class Cim:
    id: int
    iranyitoszam: int
    telepules: str
    utca: str
    hazszam: str

class CimModel(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {
            "iranyitoszam": input("Irányítószám: "),
            "telepules": input("Település: "),
            "utca": input("Utca: "),
            "hazszam": input("Házszám: "),
        }

        return params

    def getByID(self, id) -> Cim | None:
        query = "SELECT * FROM cimek WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        return Cim(result[0], result[1], result[2], result[3], result[4]) if result else None

    def create(self) -> Cim:
        params = self._get_params()

        query = (
            "INSERT INTO cimek (iranyitoszam, telepules, utca, hazszam)"
            " VALUES (:iranyitoszam, :telepules, :utca, :hazszam)")
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            new_id = cursor.lastrowid

            self.conn.commit()
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba a cím létrehozása közben: {e}")
            self.conn.rollback()
            return None

    def read(self) -> list[Cim] | None:
        cimek = []
        cursor = self.conn.execute("SELECT * FROM cimek")
        rows = cursor.fetchall()
        for result in rows:
            cimek.append(
                Cim(result[0], result[1], result[2], result[3], result[4]))
        return cimek

    def update(self) -> None:
        for i in self.read():
            print(i.id, i.iranyitoszam, i.telepules, i.utca, i.hazszam)

        print("Melyiket szeretnéd módosítani?")

        try:
            id_to_update = int(input("ID: "))
        except ValueError as e:
            print("Hibás ID", e)
            return

        current_data = self.getByID(id_to_update)
        if not current_data:
            print("Hiba, nincsen ilyen cím")
            return

        params = self._get_params()
        params["id"] = id_to_update

        sql = """
              UPDATE cimek \
              SET iranyitoszam          = :iranyitoszam, \
                  telepules             = :telepules, \
                  utca                  = :utca, \
                  hazszam               = :hazszam
              WHERE id = :id \
              """

        self.conn.execute(sql, params)
        self.conn.commit()

        print(f"\nA(z) {id_to_update} ID-jú cím adatai sikeresen frissítve!")

    def delete(self, id) -> None:
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        sql = "DELETE FROM cimek WHERE id = :id"

        self.conn.execute(sql, {"id": id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")
        return


    def _create_cim_trans(self, cursor):
        try:

            params = {
                "iranyitoszam": input("Irányítószám: "),
                "telepules": input("Település: "),
                "utca": input("Utca: "),
                "hazszam": input("Házszám: ")
            }

            query = (
                "INSERT INTO cimek (iranyitoszam, telepules, utca, hazszam)"
                " VALUES (:iranyitoszam, :telepules, :utca, :hazszam)")
            cursor.execute(query, params)

            return cursor.lastrowid
        except Exception as e:
            raise Exception(f'Hiba a cím bekérése közben: {e}')


    def _delete_cim_trans(self, id) -> bool:
        current_data = self.getByID(id)
        if not current_data:
            return False

        sql = "DELETE FROM cimek WHERE id = :id"

        self.conn.execute(sql, {"id": id})

        print(f"{id}. id cím törölve lett.")
        return True

    def _update_cim_trans(self, id) -> bool:

        try:
            id_to_update = id
        except ValueError as e:
            print("Hibás ID", e)
            return False

        current_data = self.getByID(id_to_update)
        if not current_data:
            print("Hiba, nincsen ilyen cím")
            return False

        params = self._get_params()
        params["id"] = id_to_update

        sql = """
              UPDATE cimek \
              SET iranyitoszam          = :iranyitoszam, \
                  telepules             = :telepules, \
                  utca                  = :utca, \
                  hazszam               = :hazszam
              WHERE id = :id \
              """

        self.conn.execute(sql, params)

        print(f"\nA(z) {id_to_update} ID-jú cím adatai sikeresen frissítve!")

