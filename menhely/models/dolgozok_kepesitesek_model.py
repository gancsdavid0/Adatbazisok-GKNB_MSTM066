from menhely.models._base import Model
from dataclasses import dataclass

@dataclass
class Dolgozo_kepesites:
    id: int
    dolgozo_id: int
    kepesites_id: int

class Dolgozo_kepesites_model(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {
                  "dolgozo_id": input("Dolgozo ID: "),
                  "kepesites_id": input("Képesítés ID: ")
                }
        return params

    def getByID(self, id) -> Dolgozo_kepesites | None:
        query = "SELECT * FROM dolgozok_kepesitesek WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        return Dolgozo_kepesites(result[0], result[1], result[2]) if result else None

    def create_with_ids(self, dolgozok_id, kepesitesek_id) -> Dolgozo_kepesites:
        params = {
            "dolgozok_id": dolgozok_id,
            "kepesitesek_id": kepesitesek_id
        }
        query = (
            "INSERT INTO dolgozok_kepesitesek (dolgozok_id, kepesitesek_id)"
            " VALUES (:dolgozok_id, :kepesitesek_id)")

        try:
            cursor = self.conn.cursor()
            cursor.execute(query,params)
            new_id = cursor.lastrowid

            self.conn.commit()
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba az új dolgozó-kepesítés létrehozása közben: {e}")
            self.conn.rollback()
            return None

    def create(self) -> Dolgozo_kepesites:
        pass

    def read(self) -> list[Dolgozo_kepesites] | None:
        dk_list = []
        cursor = self.conn.execute("SELECT * FROM dolgozok_kepesitesek")
        rows = cursor.fetchall()
        for result in rows:
            dk_list.append(
                Dolgozo_kepesites(result[0], result[1], result[2]))
        return dk_list

    def update(self) -> None:
        for i in self.read():
            print(i.id, i.dolgozo_id, i.kepesites_id)

        print("Melyiket szeretnéd módosítani?")

        try:
            id_to_update = int(input("ID: "))
        except ValueError as e:
            print("Hibás ID", e)
            return

        current_data = self.getByID(id_to_update)
        if not current_data:
            print("Hiba, nincsen ilyen kapcsolat")
            return

        params = self._get_params()
        params["id"] = id_to_update

        sql = """
              UPDATE dolgozok_kepesitesek \
              SET dolgozo_id        = :dolgozo_id, \
                  kepesites_id      = :kepesites_id
              WHERE id = :id \
              """

        self.conn.execute(sql, params)
        self.conn.commit()

        print(f"\nA(z) {id_to_update} ID-jú dolgozó-képesítés kapcsolat adatai sikeresen frissítve!")

    def delete(self, dolgozok_id, kepesitesek_id) -> None:
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        sql = "DELETE FROM dolgozok_kepesitesek WHERE dolgozok_id = :dolgozok_id AND kepesitesek_id = :kepesitesek_id"

        self.conn.execute(sql, {"id": id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")