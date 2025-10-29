from menhely.models._base import Model
from dataclasses import dataclass

@dataclass
class Kepesites:
    id: int
    kepesites_neve: str
    leiras: str

class KepesitesModel(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {
                  "kepesites_neve": input("Képesítés neve: "),
                  "leiras": input("Leírása: "),
                }
        return params


    def getByID(self, id) -> Kepesites | None:
        query = "SELECT * FROM kepesitesek WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        return Kepesites(result[0], result[1], result[2]) if result else None

    def create(self) -> Kepesites:
        params = self._get_params()

        query = (
            "INSERT INTO kepesitesek (kepesites_neve, leiras)"
            " VALUES (:kepesites_neve, :leiras)")

        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            new_id = cursor.lastrowid

            self.conn.commit()
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba a képesítés létrehozása közben: {e}")
            self.conn.rollback()
            return None


    def read(self) -> list[Kepesites] | None:
        kepesitesek = []
        cursor = self.conn.execute("SELECT * FROM kepesitesek")
        rows = cursor.fetchall()
        for result in rows:
            kepesitesek.append(
                Kepesites(result[0], result[1], result[2]))
        return kepesitesek

    def update(self) -> None:
        for i in self.read():
            print(i.id, i.kepesites_neve, i.leiras)

        print("Melyiket szeretnéd módosítani?")

        try:
            id_to_update = int(input("ID: "))
        except ValueError as e:
            print("Hibás ID", e)
            return

        current_data = self.getByID(id_to_update)
        if not current_data:
            print("Hiba, nincsen ilyen képesítés")
            return

        params = self._get_params()
        params["id"] = id_to_update

        sql = """
              UPDATE kepesitesek \
              SET kepesites_neve            = :kepesites_neve, \
                  leiras                    = :leiras
              WHERE id = :id \
              """

        self.conn.execute(sql, params)
        self.conn.commit()

        print(f"\nA(z) {id_to_update} ID-jú képesítés adatai sikeresen frissítve!")

    def delete(self, id) -> None:
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        sql = "DELETE FROM kepesitesek WHERE id = :id"

        self.conn.execute(sql, {"id": id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")