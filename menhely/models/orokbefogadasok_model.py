from menhely.models._base import Model
from dataclasses import dataclass
import datetime

@dataclass
class Orokbedogadas:
    id: int
    allatok_id: int
    dolgozok_id: int
    orokbefogadok_id: int
    telephelyek_id: int
    orokbedogadas_datuma: str

class OrokbedogadasokModel(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {
            "allatok_id": input("Állat ID: "),
            "dolgozok_id": input("Dolgozó ID: "),
            "orokbefogadok_id": input("Örökbefogadó ID: "),
            "telephelyek_id": input("Telephely ID: "),
            "orokbefogadas_datuma": datetime.datetime.now()
        }
        return params

    def getByID(self, id) -> Orokbedogadas | None:
        query = "SELECT * FROM orokbefogadasok WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        return Orokbedogadas(result[0], result[1], result[2], result[3], result[4], result[5]) if result else None

    def create(self, params: dict) -> Orokbedogadas:
            query = (
                "INSERT INTO orokbefogadasok (allatok_id, dolgozok_id, orokbefogadok_id, telephelyek_id, orokbefogadas_datuma)"
                " VALUES (:allatok_id, :dolgozok_id, :orokbefogadok_id, :telephelyek_id, :orokbefogadas_datuma)")

            try:
                cursor = self.conn.cursor()
                cursor.execute(query, params)
                new_id = cursor.lastrowid

                self.conn.commit()
                return self.getByID(new_id)

            except Exception as e:
                print(f"Hiba az örökbefogadás létrehozása közben: {e}")
                self.conn.rollback()
                return None

    def read(self) -> list[Orokbedogadas] | None:
        lst = []
        cursor = self.conn.execute("SELECT * FROM orokbefogadasok")
        rows = cursor.fetchall()
        for result in rows:
            lst.append(
                Orokbedogadas(result[0], result[1], result[2], result[3], result[4], result[5]))
        return lst

    def update(self) -> Orokbedogadas:
        pass

    def delete(self, id) -> None:
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        sql = "DELETE FROM orokbefogadasok WHERE id = :id"

        self.conn.execute(sql, {"id": id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")


