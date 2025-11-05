from menhely.models._base import Model
from dataclasses import dataclass


@dataclass
class Telephely_Befogadas:
    id: int
    befogadhato_allatok_id: int
    telephelyek_id: int
    max_befogadhatosag: int

class Telephely_Befogadhato_Allatok_Modell(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {
               "befogadhato_allatok_id": int(input("Begadhato allatok id: ")),
                "telephelyek_id": int(input("Telephelyek id: ")),
                "max_befogadhatosag": int(input("Max befogadhatóség: ")),
                }
        return params

    def set_kapacitas(self, telephely_id, allatfajta_id, max_kapacitas):

        query = """
            INSERT OR REPLACE INTO telephelyek_befogadhato_allatok
                (telephelyek_id, befogadhato_allatok_id, max_befogadhatosag)
            VALUES
                (:t_id, :a_id, :max_db)
        """

        params = {
            "t_id": telephely_id,
            "a_id": allatfajta_id,
            "max_db": max_kapacitas
        }

        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)

            self.conn.commit()
            print(f"Kapacitás frissítve: Telephely={telephely_id}, Állat={allatfajta_id}, Max={max_kapacitas}")
            return True

        except Exception as e:
            self.conn.rollback()
            print(f"Hiba a kapacitás beállítása közben: {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def delete_kapcsolat(self, telephely_id, allatfajta_id):
        query = """
                DELETE \
                FROM telephelyek_befogadhato_allatok
                WHERE telephelyek_id = ? \
                  AND befogadhato_allatok_id = ? \
                """
        cursor = None
        try:
            cursor = self.conn.cursor()
            # Itt '?' jeleket használunk, tehát 'tuple'-t adunk át
            cursor.execute(query, (telephely_id, allatfajta_id))
            self.conn.commit()
            print(f"Kapcsolat törölve: Telephely={telephely_id}, Állat={allatfajta_id}")
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Hiba a kapcsolat törlése közben: {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def getByID(self, id) -> Telephely_Befogadas | None:
        query = "SELECT * FROM telephelyek_befogadhato_allatok WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        return Telephely_Befogadas(result[0], result[1], result[2], result[3]) if result else None

    def create(self) -> Telephely_Befogadas:
        params = self._get_params()

        query = (
            "INSERT INTO telephelyek_befogadhato_allatok (befogadhato_allatok_id, telephelyek_id, max_befogadhatosag)"
            " VALUES (:befogadhato_allatok_id, :telephelyek_id, :vezeteknev, :max_befogadhatosag)")

        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            new_id = cursor.lastrowid

            self.conn.commit()
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba a kapcsolat létrehozása közben: {e}")
            self.conn.rollback()
            return None

    def read(self) -> list[Telephely_Befogadas] | None:
        lst = []
        cursor = self.conn.execute("SELECT * FROM telephelyek_befogadhato_allatok")
        rows = cursor.fetchall()
        for result in rows:
            lst.append(
                Telephely_Befogadas(result[0], result[1], result[2], result[3]))
        return lst

    def update(self) -> None:
        pass

    def delete(self, id) -> None:
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        sql = "DELETE FROM telephelyek_befogadhato_allatok WHERE id = :id"

        self.conn.execute(sql, {"id": id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")