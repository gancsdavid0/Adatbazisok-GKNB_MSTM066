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

    def create(self, new_address_id:int) -> Telephely:
        cursor = None
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO telephelyek (cimek_id) VALUES (?)"
            cursor.execute(query, (new_address_id,))
            new_id = cursor.lastrowid
            self.conn.commit()
            print(f"Új telephely (ID: {new_id}) létrehozva.")
            return self.getByID(new_id)

        except Exception as e:
            self.conn.rollback()
            print(f"Hiba a telephely létrehozása közben: {e}")
            return None

        finally:
            if cursor:
                cursor.close()

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
            for i in rows:
                telephelyek.append([*i])
            return telephelyek
        except Exception as e:
            print(f"Hiba a telephelyek olvasása közben: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def update(self) -> None:
        print(f"{'ID':<4} {'RefID':<6} {'IRSZ':<6} {'Város':<15} {'Utca':<25} {'Házszám'}")
        print("-" * 70)
        for i in self.read():
            print(f"{i[0]:<4} {i[1]:<6} {i[2]:<6} {i[3]:<15} {i[4]:<25} {i[5]}")

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

        try:
            sql = "DELETE FROM telephelyek WHERE id = :id"
            self.conn.execute(sql, {"id": id})
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(f'Hiba a tölés közben: {e}')

            print(f"{id}. rekord törölve lett")

    def get_kapacitasok_by_telephely_id(self, id):
        current_data = self.getByID(id)
        if not current_data:
            print(f'Nem létezik ilyen rekord')
            return -1
        query = """
                SELECT  befogadhato_allatok.id, \
                        befogadhato_allatok.allat_fajtaja,  \
                        telephelyek_befogadhato_allatok.max_befogadhatosag 
                FROM telephelyek_befogadhato_allatok  \
                         INNER JOIN \
                     befogadhato_allatok ON telephelyek_befogadhato_allatok.befogadhato_allatok_id = befogadhato_allatok.id
                WHERE telephelyek_befogadhato_allatok.telephelyek_id = ?
                """
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (current_data.id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Hiba a telephely kapacitásának lekérdezése közben: {e}")
            return -1
        finally:
            if cursor:
                cursor.close()


    def get_befogadato_allatok_byid(self, id):
        current_data = self.getByID(id)
        if not current_data:
            print(f'Nem létezik ilyen rekord')
            return
        query = """
                SELECT befogadhato_allatok.allat_fajtaja, \
                       befogadhato_allatok.megjegyzes
                FROM befogadhato_allatok
                         INNER JOIN telephelyek_befogadhato_allatok ON befogadhato_allatok.id = telephelyek_befogadhato_allatok.befogadhato_allatok_id
                WHERE telephelyek_befogadhato_allatok.telephelyek_id  = ? \
                """
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (current_data.id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Hiba a telephely befogadhatóságának lekérdezése közben: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
