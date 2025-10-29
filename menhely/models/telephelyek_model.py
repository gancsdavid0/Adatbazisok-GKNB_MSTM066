from menhely.models._base import Model
from dataclasses import dataclass



@dataclass
class Telephely:
    id: int
    cimek_id: int

class TelephelyekModel(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {
            "cimek_id": input("Cím ID: "),
        }
        return params


    def getByID(self, id) -> Telephely | None:
        query = "SELECT * FROM telephelyek WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        return Telephely(result[0], result[1]) if result else None

    def create_with_new_address(self) -> Telephely:
        cursor = None
        try:
            cursor = self.conn.cursor()
            new_address_id = self.cim_model._create_cim_trans(cursor)
            query = "INSERT INTO telephelyek (cimek_id) VALUES (?)"
            cursor.execute(query, (new_address_id,))
            new_id = cursor.lastrowid
            self.conn.commit()
            print(f"Tranzakció sikeres! Új telephely (ID: {new_id}) elmentve.")
            return self.getByID(new_id)

        except Exception as e:
            self.conn.rollback()
            print(f"HIBA! A tranzakció visszavonva. Ok: {e}")
            return None

        finally:
            if cursor:
                cursor.close()


    def create_with_existing_address(self) -> Telephely:
        params = self._get_params()

        cim = self.cim_model.getByID(params["cimek_id"])
        if cim:
            query = (
                "INSERT INTO telephelyek (cimek_id)"
                " VALUES (:cimek_id)")

            try:
                cursor = self.conn.cursor()
                cursor.execute(query, params)
                new_id = cursor.lastrowid

                self.conn.commit()
                return self.getByID(new_id)

            except Exception as e:
                print(f"Hiba a telephely létrehozása közben: {e}")
                self.conn.rollback()
                return None
        else:
            print(f'Hiba! Nem létezik ilyen cím.')

    def create(self) -> Telephely:
        pass


    def read(self) -> list[Telephely] | None:
        telephelyek = []
        query = ("SELECT "
                 "telephelyek.id, "
                 "cimek.id, cimek.iranyitoszam, "
                 "cimek.telepules, "
                 "cimek.utca, "
                 "cimek.hazszam "
                 "FROM telephelyek "
                 "INNER JOIN cimek ON telephelyek.cimek_id = cimek.id")
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Hiba a telephelyek olvasása közben: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def update(self) -> None:
        for i in self.read():
            print(i)

        print("Melyiket szeretnéd módosítani?")

        try:
            id_to_update = int(input("ID: "))
        except ValueError as e:
            print("Hibás ID", e)
            return

        current_data = self.getByID(id_to_update)
        if not current_data:
            print("Hiba, nincsen ilyen telephely")
            return

        updated_cim = self.cim_model._update_cim_trans(current_data.cimek_id)
        if updated_cim:
            try:
                params = self._get_params()
                params["id"] = id_to_update

                sql = """
                      UPDATE telephelyek \
                      SET cimek_id = :cimek_id
                      WHERE id = :id \
                      """

                self.conn.execute(sql, params)
                self.conn.commit()
                print(f"\nA(z) {id_to_update} ID-jú telephely adatai sikeresen frissítve!")
            except Exception as e:
                self.conn.rollback()
                print(f"Hiba a frissítés közben: {e}")


    def delete(self, id):
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        deleted = self.cim_model._delete_cim_trans(current_data.cimek_id)
        if deleted:
            try:
                sql = "DELETE FROM telephelyek WHERE id = :id"
                self.conn.execute(sql, {"id": id})
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(f'Hiba a tölés közben: {e}')

            print(f"{id}. rekord törölve lett")
        else:
            print(f'Hiba a {current_data} id cím törlése közben.')