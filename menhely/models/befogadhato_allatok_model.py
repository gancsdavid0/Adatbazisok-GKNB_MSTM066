from menhely.models._base import Model
from dataclasses import dataclass


@dataclass
class Befogadhato_Allat:
    id: int
    allat_fajtaja: str
    megjegyzes: str

class Befogadhato_Allatok_Model(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {
                  "allat_fajtaja": input("allat_fajtaja: "),
                  "megjegyzes": input("megjegyzes: "),
                }
        return params


    def getByID(self, id) -> Befogadhato_Allat | None:
        query = "SELECT * FROM befogadhato_allatok WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        return Befogadhato_Allat(result[0], result[1], result[2]) if result else None

    def create(self) -> Befogadhato_Allat:
        params = self._get_params()

        query = (
            "INSERT INTO befogadhato_allatok (allat_fajtaja, megjegyzes)"
            " VALUES (:allat_fajtaja, :megjegyzes)")

        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            new_id = cursor.lastrowid

            self.conn.commit()
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba a létrehozás közben: {e}")
            self.conn.rollback()
            return None

    def read(self) -> list[Befogadhato_Allat] | None:
        lst = []
        cursor = self.conn.execute("SELECT * FROM befogadhato_allatok")
        rows = cursor.fetchall()
        for result in rows:
            lst.append(
                Befogadhato_Allat(result[0], result[1], result[2]))
        return lst

    def update(self) -> None:
        pass


    def delete(self, id) -> None:
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return
        sql = "DELETE FROM befogadhato_allatok WHERE id = :id"
        self.conn.execute(sql, {"id": id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")
